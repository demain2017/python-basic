#选择排序相较冒泡排序不稳定，时间复杂度也是。
#从0索引开始，依次和后面元素比较，小的往前放，第一次完毕，最小值出现在了最小索引处。其他的同理既可以得到一个排序好的数组

def selection(l):
    for i in range(0, len(l)):
        index = i
        for j in range(i + 1, len(l)):
            if l[index] > l[j]:
                index = j
        l[i], l[index] = l[index], l[i]
    return l

if __name__ == '__main__':
    score = [12,23,43,32,45,21,6]
    print("选择排序前:",score)
    score = selection(score)
    print("选择排序后:",score)
    
