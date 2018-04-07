#相邻元素两两相比较，大的往后放。第一次完毕后，最大值就出现在了最大索引出。同理，继续，即可得到一个排序好的数组

def bubble(l):
    for i in range(0, len(l)):
        for j in range(0, len(l) - 1):
            if l[j] < l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l

if __name__ == '__main__':
    score = [23, 33, 41, 21, 12, 45]
    print("冒泡排序前:",score)
    score = bubble(score)
    print("冒泡排序后:",score)
    
