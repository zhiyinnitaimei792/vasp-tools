import sys#引入sys模块，用于获取命令行参数
from outcar import read_outcar#从outcar模块中导入read_outcar函数

if len(sys.argv) < 2:#如果命令行参数少于2个
    print("用法: python read_outcar.py <OUTCAR 路径> [可以给多个]")#打印使用方法
    sys.exit()#退出程序

for path in sys.argv[1:]:
    energies, forces, converged = read_outcar(path)
    if converged:
        status = "收敛"
    else:
        status = "未收敛"
    print(path,"离子步数:", len(energies), "收敛状态:", status, "最终能量:", energies[-1], "eV")#打印文件路径、离子步数、收敛状态和最终能量