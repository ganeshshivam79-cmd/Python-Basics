class Solution(object):

    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        l1 = nums

        def BinarySearch(target, left, right, l1):

            if left > right:
                return -1

            mid = (right + left) // 2

            if l1[mid] == target:
                return mid
            elif l1[mid] > target:
                return BinarySearch(target, left, mid - 1, l1)
            else:
                return BinarySearch(target, mid + 1, right, l1)

        return BinarySearch(target, left, right, l1)