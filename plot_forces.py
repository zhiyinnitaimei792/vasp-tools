import sys
import matplotlib.pyplot as plt  # ① 画图库


def get_forces(path):
    lines = open(path).readlines()
    forces = []
    for i in range(len(lines)):
        if "FORCES: max atom, RMS" in lines[i]:  # 跟抠能量同一个套路
            parts = lines[i].split()
            forces.append(float(parts[-2]))  # 空1：最大力在第几个位置？
    return forces


if len(sys.argv) < 2:
    print("用法: python plot_forces.py <OUTCAR 路径>")
    sys.exit()

for path in sys.argv[1:]:
    forces = get_forces(path)

    plt.figure()  # ② 开一张新画布
    plt.plot(
        range(1, len(forces) + 1), forces, marker="o", label="Max Force"
    )  # 空2、空3：横轴？纵轴？

    plt.axhline(0.05, color="red", linestyle="--", label="EDIFFG")  # ③ 见下面
    plt.legend()

    plt.xlabel("ionic step")
    plt.ylabel("max force (eV/Angst)")
    plt.title("RuO2 slab  168 O + 80 Ru")

    plt.savefig("forces.png", dpi=150)  # ④ 存成图片文件
    print("已写出 forces.png")

plt.show()  # ⑤ 弹窗看一眼（可选）
