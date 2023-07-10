def find_common_elements(n, m):
    set1 = set()
    set2 = set()
    print("Введите элементы первого множества:")
    for _ in range(n):
        element = int(input())
        set1.add(element)
    print("Введите элементы второго множества:")
    for _ in range(m):
        element = int(input())
        set2.add(element)
    common_elements = sorted(set1.intersection(set2))
    if len(common_elements) == 0:
        print("Нет общих элементов")
    else:
        print("Общие элементы в обоих множествах (в порядке возрастания):")
        for element in common_elements:
            print(element)


n = int(input("Введите количество элементов в первом множестве: "))
m = int(input("Введите количество элементов во втором множестве: "))


find_common_elements(n, m)