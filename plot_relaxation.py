import sys
import matplotlib.pyplot as plt

def get_info(path):
    lines = open(path).readlines()
    energies = []
    forces = []
    got_energies = False
    got_forces = False
    for i in range(len(lines)):
        if "free  energy   TOTEN" in lines[i]:
            parts = lines[i].split()
            energies.append(float(parts[4])) 
            got_energies = True
        if "FORCES: max atom, RMS" in lines[i]:
            parts = lines[i].split()
            forces.append(float(parts[-2]))
            got_forces = True
    return energies, forces, got_energies, got_forces

if len(sys.argv) < 2:
    print("用法: python plot_relaxation.py <OUTCAR 路径>")
    sys.exit()

for path in sys.argv[1:]:
    energies, forces, got_energies, got_forces = get_info(path)

    if not got_energies and not got_forces:
        print(path, "里一行能量和 FORCES 都没找到 —— 这不是一个完整的 OUTCAR吧？")
        continue

    fig,(ax1,ax2) = plt.subplots(2,1,sharex=True,figsize=(6,8))
    x = range(1, len(energies) + 1)

    if got_energies:
        ref = energies[-1]
        delta = []
        for e in energies:
            delta.append(e - ref)
        
        ax1.plot(x, delta, marker="o", label="Delta Energy") 
        ax1.axhline(0, color="red", linestyle="--", label="Final Energy") 
        ax1.set_ylabel("E - E_final (eV)")
        ax1.legend()
    else:
        print(path, "一行能量都没找到")

    if got_forces:
        ax2.plot(x, forces, marker="o", label="Max Force")  
        ax2.axhline(0.05, color="red", linestyle="--", label="EDIFFG")  
        ax2.legend()
        ax2.set_xlabel("ionic step")
        ax2.set_ylabel("max force (eV/Angst)")
    else:
        print(path, "里一行 FORCES 都没找到")

    plt.tight_layout()
    out = path + "_relaxation.png"
    plt.savefig(out, dpi=150)
    print(path, "已写出", out)