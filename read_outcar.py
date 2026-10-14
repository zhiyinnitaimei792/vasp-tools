import sys#引入sys模块，用于获取命令行参数
path = sys.argv[1]#获取命令行参数中的第一个参数，即文件路径
lines = open(path).readlines()#将文件内容按行读取到列表中
energies = []#创建一个空列表来存储能量值
for i in range(len(lines)):#遍历每一行，同时记住现在是第几行
    if "FREE ENERGIE OF THE ION-ELECTRON SYSTEM" in lines[i]:#如果这一行包含"FREE ENERGIE OF THE ION-ELECTRON SYSTEM"
        parts = lines[i+2].split()#将下面第二行的内容按空格分割成一个列表
        energies.append(float(parts[-2]))#将倒数第二个元素转换为浮点数并添加到energies列表中
print("离子步数:", len(energies))#打印离子步数
print("最终能量:", energies[-1], "eV")#打印最终能量
print("最低能量:", min(energies), "eV")#打印最低能量
print("最高能量:", max(energies), "eV")#打印最高能量
print("总共降了:", energies[0] - energies[-1], "eV")#打印总降幅