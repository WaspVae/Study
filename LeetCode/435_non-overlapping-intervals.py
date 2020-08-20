class Solution:
    def erase_overlap_intervals(self, intervals):
        n = len(intervals)
        if n == 0:
            return 0
        # # 使用动态规划(此问题可以转化为最长上升子序列问题)
        # intervals.sort()
        # # memo[i] 表示使用 intervals[0...i] 的区间能构成的最长不重叠子区间
        # memo = [1] * n
        # for i in range(1, n):
        #     for j in range(i):
        #         if intervals[i][0] >= intervals[j][-1]:
        #             memo[i] = max(memo[i], 1 + memo[j])
        # return n - max(memo)
        # 使用贪心算法
        intervals.sort(key=lambda x: x[-1])
        res = 1
        pre = 0
        for i in range(1, n):
            if intervals[i][0] >= intervals[pre][-1]:
                res += 1
                pre = i
        return n - res
