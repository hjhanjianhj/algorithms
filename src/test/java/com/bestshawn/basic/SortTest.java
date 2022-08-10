package com.bestshawn.basic;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.function.Consumer;
import java.util.function.Function;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class SortTest {
    private Sort sort;

    @BeforeEach
    public void setup() {
        this.sort = new Sort();
    }

    @Test
    public void test_select() {
        test_sort(sort::select);
    }

    @Test
    public void test_insert() {
        test_sort(sort::insert);
    }

    @Test
    public void test_bubble() {
        test_sort(sort::bubble);
    }

    public void test_sort(Consumer<int[]> fn) {
        int maxLength = 100;
        int maxValue = 1000;
        for (int i = 0; i < 10000; i++) {
            int[] nums1 = generateData(maxLength, maxValue);
            int[] nums2 = Arrays.copyOf(nums1, nums1.length);
            fn.accept(nums1);
            Arrays.sort(nums2);
            assertArrayEquals(nums2, nums1);
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
