# -*- coding: utf-8 -*-

class Solution(object):
    def permute(self, nums):
        """
        给定一个 没有重复 数字的序列，返回其所有可能的全排列。
        """

        def back_track(self, nums, track):
            """
            回溯法
            """
            # 触发结束条件
            if (len(track) == len(nums)):
                res.append(track)
                return

            for num in nums:
                if num in track:
                    continue
                # 做选择
                track.append(num)
                nums.remove(num)
                back_track(self, nums, track)
                # 撤销选择的路径
                track = []
                # 将该选择加入到选择列表中
                nums.append(num)

        res = []
        track = []
        back_track(self, nums, track)
        return res


class SolutionTest2(object):
    def maxProfit(self, prices):
        """
        给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
        【题解】
              由题意可知，要求卖股票的利润最大，则只要股票上升，则卖，所以只要数组中的
              第i个元素大于第i-1个元素，就在i-1买入股票，i卖出股票，则获取的利润为：
              prices[i] - prices[i-1]

        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                up_money = prices[i] - prices[i - 1]
                max_profit += up_money

        return max_profit
