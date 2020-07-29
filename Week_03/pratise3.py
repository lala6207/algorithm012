# -*- coding: utf-8 -*-

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    根据一棵树的前序遍历与中序遍历构造二叉树。
    【解题思路】
      前根遍历顺序： 根  左子树  右子树
      中根遍历顺序： 左子树  根  右子树
      由前根遍历，可知根节点，则在中跟遍历中可得左子树和右子树，
      将该步得到的左子树和右子树，可以看做是之前的子集，进而按照上一步骤的方法，进行再一次判断。
    """
    def buildTree(self, preorder, inorder):
        def myBuildTree(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right or inorder_left > inorder_right:
                return None

            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index.get(preorder[preorder_root])

            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left,
                                    inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1,
                                     inorder_right)
            return root

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)


class SolutionTest2(object):
    """
    给定一个 没有重复 数字的序列，返回其所有可能的全排列。
    """
    def permute(self, nums):
        """
        给定一个 没有重复 数字的序列，返回其所有可能的全排列。
        """
        def trace_back(nums, path):
            if len(path) == len(nums):
                import copy
                d = copy.deepcopy(path)
                res.append(d)
                return
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                trace_back(nums, path)
                path.remove(num)

        res = []
        path = []
        trace_back(nums, path)
        return res