def find_lines(path,keywords):
    f = open(path)
    for line in f:
        if keywords in line:
            print(line)
    f.close()
find_lines("sample_OUTCAR.txt","TOTEN")  
find_lines("sample_OUTCAR.txt","ENERGIE")