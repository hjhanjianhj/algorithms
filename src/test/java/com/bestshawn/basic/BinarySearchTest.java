package com.bestshawn.basic;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

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

    private int[] generateData(int maxLength, int maxValue) {
        int length = (int)(Math.random() * (maxLength + 1));
        int[] nums = new int[length];
        for (int i = 0; i < length; i++) {
            nums[i] = (int) ((maxValue + 1) * Math.random()) - (int)(maxValue * Math.random());
        }
        return nums;
    }
}
