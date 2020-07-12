# -*- coding: utf-8 -*-


def get_max_num(nums):
    """
    letcode: 最大子序和
    用动态规划法实现：
     求局部最优解
    :param nums:
    :return:
    """
    compare_num_list = []
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            compare_num = nums[i - 1] + nums[i]
            compare_num_list.append(compare_num)
            nums[i] = compare_num
    return max(nums) if len(nums) > 0 else 0


def del_rep_num(nums):
    """
    letcode: 删除排序数组中的重复项
    快慢指针
    :param nums:
    :return:
    """
    pre_index = 0
    for _back_index in range(1, len(nums)):
        if nums[_back_index] > nums[pre_index]:
            nums[pre_index + 1] = nums[_back_index]
            pre_index += 1
    return pre_index + 1


def reverse_list(k, nums):
    """
    letcode: 反转数组
    快慢指针
    :param nums:
    :return:
    """
    n = len(nums)
    k %= n
    nums[:] = nums[::-1]
    nums[:k] = nums[:k][::-1]
    # print(nums)
    nums[k:] = nums[k:][::-1]
    # print(nums)


if __name__ == "__main__":

    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # max_sum = get_max_num(nums)
    # print(max_sum)

   nums = [1, 1, 2]
   list_num = del_rep_num(nums)
   print(list_num)
