"""
插入排序总结：

1.当前需要排序的元素(array[i])，跟已经排序好的最后一个元素比较(array[i-1])，如果满足条件继续执行后面的程序，否则循环到下一个要排序的元素。
2.缓存当前要排序的元素的值，以便找到正确的位置进行插入。
3.排序的元素跟已经排序号的元素比较，比它大的向后移动(升序)。
4.要排序的元素，插入到正确的位置。
"""

def insert_sort(l):
    for i in range(1, len(l)):
        if l[i - 1] > l[i]:
            temp = l[i]    # 当前需要排序的元素
            index = i      # 用来记录排序元素需要插入的位置
            while index > 0 and l[index - 1] > temp:
                l [index] = l[index - 1]    # 把已经排序好的元素后移一位，留下需要插入的位置
                index -= 1
            l[index] = temp #把需要排序的元素，插入到指定位置
    return l
if __name__ == '__main__':
    score = [1,34,23,54,56,33,67,89,22]
    print("插入排序前:", score)
    score = insert_sort(score)
    print("插入排序后:", score)
