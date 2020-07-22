# -*- coding: utf-8 -*-


class Solution(object):
    def twoSum(self, nums, target):
        """
        给定一个整数数组 nums 和一个目标值 target，
        请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
        你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

        示例:
           给定 nums = [2, 7, 11, 15], target = 9

           因为 nums[0] + nums[1] = 2 + 7 = 9
           所以返回 [0, 1]
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        【解题思路】
           求数组中x,y两个数之和等于给定的值，则 y = target - x
           法1：双层for循环，则可以得到x,y ,进而满足条件 时间复杂度O(n) 空间复杂度O(1)
           法2：遍历数组，如果在数组中找到y,则返回x,y对应的下标，如果没有找到，则将其放入到
           key为数组元素，value为元素对应下标的字典

           时间复杂度O(n) 空间复杂度为O(n)
        """

        num_dict = dict()
        index_list = list()
        for _index, _num in enumerate(nums):
            temp = target - _num
            if num_dict.has_key(temp):
                index_list.append(_index)
                index_list.append(num_dict.get(temp))
                return index_list
            else:
                num_dict[_num] = _index

        return index_list


class ListNode(object):
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionTest(object):
    def deleteDuplicates(self, head):
        """
        给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
        示例 1:
        输入: 1->1->2
        输出: 1->2
        :type head: ListNode
        :rtype: ListNode
        【解题思路】
        根据题意可知：该链表有序，说明只要找到了重复元素，则后面不会间隔出现。
        所以遍历循环该链表，如果找到重复元素，则当前节点指向下下一个节点，
        否则，继续遍历下一个元素

        时间复杂度O(n) 空间复杂度O(1)
        """
        node = head
        while(node and node.next):
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head


class SolutionTest1(object):
    """
            给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
            【题目意思】
                两个字符串长度相同，字母相同，顺序无所谓。
            【解题思路】
               1.对连个字符串排序，如果相同，则为True,否则为False  时间复杂度 O(log n) 空间O(1)
               2.
    """

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return True if sorted(s) == sorted(t) else False

    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return True if sorted(s) == sorted(t) else False
