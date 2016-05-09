N = int(raw_input())
list = map(int, raw_input().split())

def bubble_sort(list, cnt):
    for start_index in range(len(list)-1):
        for index in range(1, len(list) - start_index):
            if list[index - 1] > list[index]:
                temp = list[index - 1]
                list[index - 1] = list[index]
                list[index] = temp
                cnt += 1
    print cnt

bubble_sort(list, 0)