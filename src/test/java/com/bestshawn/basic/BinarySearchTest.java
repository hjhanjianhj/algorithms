package com.bestshawn.basic;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

public class BinarySearchTest {
    private BinarySearch binarySearch;

    @BeforeEach
    public void setup() {
        this.binarySearch = new BinarySearch();
    }

    @Test
    public void test_exists() {
        int maxLength = 100;
        int maxValue = 1000;
        for (int i = 0; i < 10000; i++) {
            int[] nums = generateData(maxLength, maxValue);
            int num = (int) ((maxValue + 1) * Math.random());
            Arrays.sort(nums);
            boolean ret = binarySearch.exists(nums, num);
            int expectIndex = Arrays.binarySearch(nums, num);
            assertEquals(expectIndex >= 0, ret);
        }
    }

    @Test
    public void test_nearestLeftIndex() {
        int maxLength = 100;
        int maxValue = 1000;
        for (int i = 0; i < 10000; i++) {
            int[] nums = generateData(maxLength, maxValue);
            int num = (int) ((maxValue + 1) * Math.random());
            Arrays.sort(nums);
            int ret = binarySearch.nearestLeftIndex(nums, num);
            int except = nearestLeftIndex(nums, num);
            assertEquals(except, ret);
        }
    }

    @Test
    public void test_nearestRightIndex() {
        int maxLength = 100;
        int maxValue = 1000;
        for (int i = 0; i < 10000; i++) {
            int[] nums = generateData(maxLength, maxValue);
            int num = (int) ((maxValue + 1) * Math.random());
            Arrays.sort(nums);
            int ret = binarySearch.nearestRightIndex(nums, num);
            int except = nearestRightIndex(nums, num);
            if (ret != except) {
                System.out.println(nums);
                System.out.println(num);
                assertTrue(false);
            }
            assertEquals(except, ret);
        }
    }

    @Test
    public void test_getLocalMin() {
        int maxLength = 100;
        int maxValue = 1000;
        for (int i = 0; i < 10000; i++) {
            int[] nums = generateNearNotEqualsData(maxLength, maxValue);
            int ret = binarySearch.getLocalMin(nums);
            assertGetMinLocalMin(nums, ret);
        }
    }

    private void assertGetMinLocalMin(int[] nums, int index) {
        if (nums.length <=1) {
            return;
        }
        if (index == 0) {
            assertTrue(nums[index] < nums[index + 1]);
            return;
        }
        if (index == nums.length - 1) {
            assertTrue(nums[index] < nums[index - 1]);
            return;
        }

        assertTrue(nums[index] < nums[index + 1] && nums[index] < nums[index - 1]);
    }

    private int[] generateNearNotEqualsData(int maxLength, int maxValue) {
        int length = (int)(Math.random() * (maxLength + 1));
        int[] nums = new int[length];
        for (int i = 0; i < length; i++) {
            do {
                nums[i] = (int) ((maxValue + 1) * Math.random()) - (int) (maxValue * Math.random());
            } while (i > 0 && nums[i-1] == nums[i]);
        }
        return nums;
    }

    private int nearestRightIndex(int[] nums, int num) {
        for (int i = nums.length - 1; i >= 0; i--) {
            if (nums[i] <= num) {
                return i;
            }
        }
        return -1;
    }

    private int nearestLeftIndex(int[] nums, int num) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] >= num) {
                return i;
            }
        }

        return -1;
    }

    private int[] generateData(int maxLength, int maxValue) {
        int length = (int)(Math.random() * (maxLength + 1));
        int[] nums = new int[length];
        for (int i = 0; i < length; i++) {
            nums[i] = (int) ((maxValue + 1) * Math.random()) - (int)(maxValue * Math.random());
        }
        return nums;
    }
}
