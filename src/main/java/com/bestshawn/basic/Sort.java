package com.bestshawn.basic;

/**
 * 排序
 */
public class Sort {

    /**
     * 插入法排序
     *
     * @param nums 待排序数组
     */
    public void insert(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            for (int j = i; j > 0 && nums[j] < nums[j-1]; j--) {
                swap(nums, j, j - 1);
            }
        }
    }

    /**
     * 选择排序
     * @param nums
     */
    public void select(int[] nums) {
        for (int i=0; i < nums.length - 1; i++) {
            for (int j = i+1; j < nums.length; j++) {
                if (nums[i] > nums[j]) {
                    swap(nums, i, j);
                }
            }
        }
    }

    /**
     * 冒泡排序
     * @param nums
     */
    public void bubble(int[] nums) {
        for (int i = nums.length - 1; i > 0 ; i--) {
            for (int j = 0; j < i; j++) {
                if (nums[j] > nums[j + 1]) {
                    swap(nums, j, j + 1);
                }
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
