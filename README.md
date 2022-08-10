# 算法学习
## 对数器
### 问题：
1. 选择，插入，冒泡排序，并做对数器

## 二分法查找
1. 基本二分法查找核心代码:
```java
while (left <= right) {
    mid = left + ((right - left) >> 1);
    if (sortedArr[mid] == num) {
        return true;
    } else if (sortedArr[mid] > num) {
        right = mid - 1;
    } else {
        left = mid + 1;
    }
}
```
其中需要注意的细节：
* 需注意left <= right和left < right，当没有等号时，需注意最后一个数字可能没有比较，需要在循环之后单独处理
* mid = left + ((right - left) >> 1)，不用（left + right)/2是为了避免(left + right)越界
2. 二分法的变种:
    1. 在arr上，找满足>=value的最左位置
    2. 在arr上，找满足>=value的最右位置
    3. 在无序的arr上，任意两个相邻的数不相等，返回数组上任意一个局部最小的数，局部最小满足arr[i-1]>arr[i]<arr[i+1]

## 位运算

## 栈和队列

## 链表

## 二叉树

## 字符串

## 递归和动态规划

## 其它问题
