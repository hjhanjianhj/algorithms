package com.bestshawn.basic;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class BitOperationTest {
    private BitOperation bitOperation;

    @BeforeEach
    public void setup() {
        this.bitOperation = new BitOperation();
    }
    @Test
    public void test_getOddTimesNum1() {
        int kinds = 5;
        int range = 300;
        int testTimes = 100000;
        int max = 9;
        for (int i = 0; i < testTimes; i++) {
            int oddCounts = (int)(Math.random() * max);
            if ((oddCounts & 1) == 0) {
                oddCounts += 1;
            }
            int evenCounts = (int)(Math.random() * max);
            if ((evenCounts & 1) == 1) {
                evenCounts += 1;
            }
            int[] arr = generateData(kinds, range, oddCounts, evenCounts);
            int ret = this.bitOperation.getOddTimesNum1(arr);
            int expect = expectGetOddTimesNum1(arr);
            assertEquals(expect, ret);
        }
    }

    @Test
    public void test_getOddTimesNum2() {

    }

    private int expectGetOddTimesNum1(int[] arr) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : arr) {
            Integer times = map.getOrDefault(num, 0);
            map.put(num, times + 1);
        }
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if ((entry.getValue() & 1) == 1) {
                return entry.getKey();
            }
        }
        return 0;
    }

    private int[] generateData(int kinds, int range, int k, int m) {
        int kTimeNum = randomNumber(range);
        int[] nums = new int[k + (kinds - 1) * m];
        int index = 0;
        for (int i = 0; i < k; i++) {
            nums[index++] = kTimeNum;
        }
        int remindKinds = kinds - 1;
        Set<Integer> set = new HashSet<>();
        set.add(kTimeNum);
        while (remindKinds > 0) {
            int curNum = 0;
            do {
                curNum = randomNumber(range);
            } while (set.contains(curNum));
            remindKinds -= 1;
            for (int i = 0; i < m; i++) {
                nums[index++] = curNum;
            }
        }
        for (int i = 0; i < nums.length; i++) {
            int randomIndex = (int)(Math.random() * nums.length);
            swap(nums, i, randomIndex);
        }
        return nums;
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    private int randomNumber(int range) {
        return (int)(Math.random()*(range + 1)) - (int)(Math.random()*range);
    }
}
