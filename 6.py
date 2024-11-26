import os
def find(path, filename):
    '''funkcja znajduje rekurencyjnie pliki o podanej nazwie startując od zadanej ścieżki
        input : path - ścieżka, od której funkcja szuka plików
                filename - nazwa szukanych plików
        output : lista ścieżek do plików o podanej nazwie'''
    tab = []

    files = os.listdir(path)
    for i in files:
        a = os.path.join(path, i)
        if os.path.isdir(a):
            tab += find(a, filename)
        elif os.path.isfile(a):
            if filename in i:
                tab.append(a)
    return tab

print(find(r'C:\Users\lenovo\Desktop\maria\l2_z6_dir','howareyou.txt'))

