def read_outcar(path):
    lines = open(path).readlines()
    energies = []
    forces = []
    converged = False
    for i in range(len(lines)):
        if "free  energy   TOTEN" in lines[i]:
            parts = lines[i].split()
            energies.append(float(parts[4])) 
        if "FORCES: max atom, RMS" in lines[i]:
            parts = lines[i].split()
            forces.append(float(parts[-2]))
        if "reached required accuracy" in lines[i]:
            converged = True
    return energies, forces, converged