import sys
path = sys.argv[1]
lines = open(path).readlines()
energies = []
for i in range(len(lines)):
    if "FREE ENERGIE OF THE ION-ELECTRON SYSTEM" in lines[i]:
        parts = lines[i+2].split()
        energies.append(float(parts[-2]))
print("离子步数:", len(energies))
print("最终能量:", energies[-1], "eV")
print("最低能量:", min(energies), "eV")
print("最高能量:", max(energies), "eV")
print("总共降了:", energies[0] - energies[-1], "eV")