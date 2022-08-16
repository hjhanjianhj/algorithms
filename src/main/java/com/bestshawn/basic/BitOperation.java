package com.bestshawn.basic;

/**
 * 位运算
 */
public class BitOperation {
    /**
     * 一个数组中有一种数出现了奇数次，其它数都出现了偶数次，找到这种数
     * @param arr
     * @return
     */
    public int getOddTimesNum1(int[] arr) {
        int eor = 0;
        for (int num : arr) {
            eor ^= num;
        }
        return eor;
    }

    /**
     * 一个数组中有两种数出现了奇数次，其它数都出现了偶数次，怎么找到这两种数
     * @param arr
     * @return
     */
    public int[] getOddTimesNum2(int[] arr) {
        int eor = 0;
        for (int num : arr) {
            eor ^= num;
        }
        int rightOne = eor & (-eor);
        int[] ret = new int[2];
        for (int num : arr) {
            if ((num & rightOne) != 0) {
                ret[0] ^= num;
            }
        }
        ret[1] = eor ^ ret[0];

        return ret;
    }

    public int getOnlyKTimes(int[] arr, int k, int m) {
        int[] help = new int[32];
        for (int num : arr) {
            for (int i = 0; i < help.length; i++) {
                help[i] += (num >> i) & 1;
            }
        }

        int ret = 0;
        for (int i = 0; i < help.length; i++) {
            if (help[i] % m != 0) {
                ret |= 1 << i;
            }
        }

        return ret;
    }
}
