# vasp-tools

处理 VASP 输出文件的小工具集。能一次读取多个结构优化算例的 OUTCAR，提取每个算例的离子步数和最终能量，并判断结构优化是否收敛。

## 为什么需要它

OUTCAR 里打印的能量值非常多，全混在一起。其中只有一部分是**离子步**的能量（真正在优化结构的那一步），剩下的属于**电子步**（每一步内部的中间产物）。

人工去数是很容易数错的。例如作者手上的一个 RuO2 算例：`grep -c TOTEN` 会给出 **171** 行，而真正的离子步只有 **10** 个。

## 怎么用

在包含 OUTCAR 的文件夹中运行：

```
python read_outcar.py sample_OUTCAR.txt
```

一次给多个文件也可以，会依次处理：

```
python read_outcar.py OUTCAR1 OUTCAR2 OUTCAR3
```

命令行里什么都没给时，会打印用法提示，而不是默默退出：

```
python read_outcar.py
```

### 想看“未收敛”的情况长什么样？

仓库里的 `sample_OUTCAR.txt` 是收敛的。要造一个没收敛的样本，把它里面那行收敛标志删掉即可（需要 `grep`，Linux / macOS / Git Bash 都有）：

```
grep -v "reached required accuracy" sample_OUTCAR.txt > notconv.txt
```

再跑：

```
python read_outcar.py sample_OUTCAR.txt notconv.txt
```

## 输出

`sample_OUTCAR.txt` 一个文件：

```
sample_OUTCAR.txt 离子步数: 5 收敛状态: 收敛 最终能量: -18092.44087654 eV
```

`sample_OUTCAR.txt` 和 `notconv.txt` 一起：

```
sample_OUTCAR.txt 离子步数: 5 收敛状态: 收敛 最终能量: -18092.44087654 eV
notconv.txt 离子步数: 5 收敛状态: 未收敛 最终能量: -18092.44087654 eV
```

一个文件一条结果，开头是文件名。`收敛状态` 判断的是**结构优化是否收敛**（VASP 的判据是力，由 INCAR 里的 `EDIFFG` 设定），**不是**能量是否收敛。

不带参数运行：

```
用法: python read_outcar.py <OUTCAR 路径> [可以给多个]
```

## 环境

Python 3.11，无第三方依赖。
