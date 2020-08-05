# 归并排序的 merge 操作
class Solution:
    def merge_sorted_array(self, nums1, m, nums2, n):
        # 时间复杂度: O(n + m)
        # 空间复杂度: O(m)
        # nums1_copy = nums1[:m]
        # nums1[:] = []
        # i, j = 0, 0
        # while i < m and j < n:
        #     if nums1_copy[i] < nums2[j]:
        #         nums1.append(nums1_copy[i])
        #         i += 1
        #     else:
        #         nums1.append(nums2[j])
        #         j += 1
        # if i < m:
        #     nums1.extend(nums1_copy[i:])
        # if j < n:
        #     nums1.extend(nums2[j:])
        # 时间复杂度: O(n + m)
        # 空间复杂度: O(1)
        # 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
        i, j = m - 1, n - 1  # 指向 nums1 和 nums2 满足要求的最后一个元素
        p = m + n - 1  # 指向添加元素位置
        while i >= 0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[p] = nums2[j]
                j -= 1
            else:
                nums1[p] = nums1[i]
                i -= 1
            p -= 1
        nums1[: j + 1] = nums2[:j + 1]
