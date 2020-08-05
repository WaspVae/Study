class Solution:
    def max_area(self, height):
        # 时间复杂度为 O(n)
        # 空间复杂度为 O(n)
        # i = 0
        # j = len(height) - 1
        # area_list = []
        # while i < j:
        #     if height[i] < height[j]:
        #         area_list.append(height[i] * (j - i))
        #         i += 1
        #     else:
        #         area_list.append(height[j] * (j - i))
        #         j -= 1
        # return max(area_list)
        # 时间复杂度为 O(n)
        # 空间复杂度为 O(1)
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            if height[i] < height[j]:
                max_area = max(max_area, height[i] * (j - i))
                i += 1
            else:
                max_area = max(max_area, height[j] * (j - i))
                j -= 1
        return max_area
