package com.bestshawn.basic;

public class BinarySearch {
    /**
     * 二分法查找
     * @param sortedArr
     * @param num
     * @return
     */
    public boolean exists(int[] sortedArr, int num) {
        if (sortedArr == null || sortedArr.length == 0) {
            return false;
        }
        int left = 0;
        int right = sortedArr.length - 1;
        int mid = 0;
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

        return false;
    }

    /**
     * 给定一个有序数组，查找满足arr[i]>=value最左边i的值
     * @param arr
     * @param value
     * @return
     */
    public int nearestLeftIndex(int[] arr, int value) {
        int left = 0;
        int right = arr.length - 1;
        int mid = 0;
        int index = -1;

        while (left <= right) {
            mid = left + ((right - left) >> 1);
            if (arr[mid] >= value) {
                index = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return index;
    }

    public int nearestRightIndex(int[] arr, int value) {
        int left = 0;
        int right = arr.length - 1;
        int mid = 0;
        int index = -1;
        while (left <= right) {
            mid = left + ((right - left) >> 1);
            if (arr[mid] <= value) {
                left = mid + 1;
                index = mid;
            } else {
                right = mid - 1;
            }
        }

        return index;
    }

    /**
     * 返回数组中的局部最小数的index，局部最小定义arr[i-1]>arr[i]<arr[i+1]
     * arr数组特色要求：相邻的两个数不相等arr[i-1] != arr[i]
     * @param arr
     * @return
     */
    public int getLocalMin(int[] arr) {
        if (arr == null || arr.length == 0) {
            return -1;
        }
        if (arr.length == 1 || arr[0] < arr[1]) {
            return 0;
        }
        if (arr[arr.length - 1] < arr[arr.length - 2]){
            return arr.length - 1;
        }

        int left = 1;
        int right = arr.length - 2;
        int mid = 0;
        while (left <= right) {
            mid = left + ((right - left) >> 1);
            if (arr[mid - 1] < arr[mid]) {
                right = mid - 1;
            } else if (arr[mid + 1] < arr[mid]) {
                left = mid + 1;
            } else {
                return mid;
            }
        }

        return left;
    }
}
