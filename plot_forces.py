import sys
import matplotlib.pyplot as plt  # ① 画图库
from outcar import read_outcar  # 从 outcar.py 中导入 read_outcar 函数

if len(sys.argv) < 2:
    print("用法: python plot_forces.py <OUTCAR 路径>")
    sys.exit()

for path in sys.argv[1:]:
    energies, forces, converged = read_outcar(path)

    if forces:  # 如果找到了力值
        plt.figure()  # ② 开一张新画布
        plt.plot(range(1, len(forces) + 1), forces, marker="o", label="Max Force")  

        plt.axhline(0.05, color="red", linestyle="--", label="EDIFFG")  
        plt.legend()

        plt.xlabel("ionic step")
        plt.ylabel("max force (eV/Angst)")
        plt.title(path)

        out = path + "_forces.png"
        plt.savefig(out, dpi=150)  # ④ 存成图片文件
        print(path, "已写出", out)
    else:
        print(path, "里一行 FORCES 都没找到 —— 这不是一个完整的 OUTCAR吗？")
