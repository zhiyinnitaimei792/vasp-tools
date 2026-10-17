import sys
import matplotlib.pyplot as plt

def get_energies(path):
    lines = open(path).readlines()
    energies = []
    got_energies = False
    for i in range(len(lines)):
        if "free  energy   TOTEN" in lines[i]:
            parts = lines[i].split()
            energies.append(float(parts[4])) 
            got_energies = True
    return energies, got_energies

if len(sys.argv) < 2:
    print("用法: python plot_energies.py <OUTCAR 路径>")
    sys.exit()

for path in sys.argv[1:]:
    energies, got_energies = get_energies(path)

    if got_energies:
        ref = energies[-1]
        delta = []
        for e in energies:
            delta.append(e - ref)
        
        plt.figure()
        plt.plot(range(1, len(energies) + 1), delta, marker="o", label="Delta Energy") 
        plt.axhline(0, color="red", linestyle="--", label="Final Energy") 

        plt.legend()
        plt.xlabel("ionic step")
        plt.ylabel("E - E_final (eV)")
        plt.title(path)

        out = path + "_energies.png"
        plt.savefig(out, dpi=150)
        print(path, "已写出", out)
    else:
        print(path, "一行能量都没找到")