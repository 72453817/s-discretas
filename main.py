import sys, matplotlib.pyplot as plt, networkx as nx
from matplotlib.patches import FancyArrowPatch

# === Definición del DFA ===
states = {"hhhhhhhh","llllllllll","q2","q3","q4"}
alphabet = {"aaaa","bfff"}


q0, F = "q0", {"q4"}



def draw_step(current, idx, sym=None):
    plt.clf(); nodes=list(G.nodes())
    nx.draw_networkx_nodes(G,pos,nodelist=nodes,node_size=[900 if n==current else 600 for n in nodes],linewidths=[3 if n in F else 1 for n in nodes],edgecolors="black")
    nx.draw_networkx_edges(G,pos)
    seen={}
    for u,v,k,d in G.edges(keys=True,data=True):
        if u == v:
            x, y = pos[u]
            j = seen.get((u, u), 0); seen[(u, u)] = j + 1

            rad  = 0.5 if j % 2 == 0 else -0.6    # curva más compacta
            dx   = 0.08                           # menos ancho de arco
            offy = 0.22 if j % 2 == 0 else -0.22  # etiqueta más cerca

            loop = FancyArrowPatch((x - dx, y), (x + dx, y),
                connectionstyle=f"arc3,rad={rad}",
                arrowstyle='-|>', mutation_scale=18, linewidth=1.2,
                shrinkA=6, shrinkB=6, zorder=5, clip_on=False)
            plt.gca().add_patch(loop)

            plt.text(x, y + offy, d["label"], fontsize=10, ha="center", va="center")
            continue
        i=seen.get((u,v),0); seen[(u,v)]=i+1; rad = 0.18 if i % 2 == 0 else -0.18
        nx.draw_networkx_edges(G,pos,edgelist=[(u,v)],connectionstyle=f"arc3,rad={rad}",arrows=True,arrowstyle='-|>',arrowsize=20)
        lx,ly=_mid(pos[u],pos[v],0.10 if i%2==0 else -0.10); plt.text(lx,ly,d['label'],fontsize=11,ha='center',va='center')
    plt.axis('off'); plt.title(f"Paso {idx}: {current}" + (f" | '{sym}'" if sym else "")); plt.pause(1.0)

# === main ===
if __name__=='__main__':
    s = sys.argv[1] if len(sys.argv)>1 else input("Cadena (a/b): ").strip()
    try:
        steps, ok = run(s); print("ACEPTA" if ok else "RECHAZA", f"(estado final: {steps[-1]})")
        plt.ion(); draw_step(steps[0],0)
        for i,ch in enumerate(s,1): draw_step(steps[i],i,ch)
        plt.ioff(); plt.show()
    except Exception as e:
        print("RECHAZA:", e)