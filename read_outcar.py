import sys#引入sys模块，用于获取命令行参数
def get_info(path):
    lines = open(path).readlines()#将文件内容按行读取到列表中
    energies = []#创建一个空列表来存储能量值
    converged = False#初始化收敛标志为False
    for i in range(len(lines)):#遍历每一行，同时记住现在是第几行
        if "FREE ENERGIE OF THE ION-ELECTRON SYSTEM" in lines[i]:#如果这一行包含"FREE ENERGIE OF THE ION-ELECTRON SYSTEM"
            parts = lines[i+2].split()#将下面第二行的内容按空格分割成一个列表
            energies.append(float(parts[-2]))#将倒数第二个元素转换为浮点数并添加到energies列表中
        if "reached required accuracy" in lines[i]:#如果这一行包含"reached required accuracy - stopping structural energy minimisation"
            converged = True
    return energies, converged

if len(sys.argv) < 2:#如果命令行参数少于2个
    print("用法: python read_outcar.py <OUTCAR 路径> [可以给多个]")#打印使用方法
    sys.exit()#退出程序

for path in sys.argv[1:]:
    energies, converged = get_info(path)
    if converged:
        status = "收敛"
    else:
        status = "未收敛"
    print(path,"离子步数:", len(energies), "收敛状态:", status, "最终能量:", energies[-1], "eV")#打印文件路径、离子步数、收敛状态和最终能量