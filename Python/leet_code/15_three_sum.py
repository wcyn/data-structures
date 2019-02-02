class Solution:

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            raise ValueError("There must be at least 3 numbers")
        current_pointer = 0
        results_set = set()
        sum_memo = {}
        while current_pointer <= len(nums) - 3:
            print(current_pointer)
            second_pointer = current_pointer + 1
            while second_pointer <= len(nums) - 2:
                third_pointer = second_pointer + 1
                while third_pointer <= len(nums) - 1:
                    if (second_pointer, third_pointer) not in sum_memo:
                        sum_memo[(second_pointer, third_pointer)] = nums[second_pointer] + nums[third_pointer]
                    num_sum = nums[current_pointer] + sum_memo[(second_pointer, third_pointer)]
                    if num_sum == 0:
                        # results_set.add((nums[current_pointer], nums[second_pointer], nums[third_pointer]))
                        results_set.add(
                            tuple(sorted([nums[current_pointer], nums[second_pointer], nums[third_pointer]])))
                    third_pointer += 1
                second_pointer += 1
            current_pointer += 1
        return results_set

    def threeSumFaster(self, nums):
        def binary_search(num_list, start_point, target):
            floor, ceiling = start_point, len(num_list) - 1

            while floor <= ceiling:
                mid = floor + (ceiling - floor) // 2
                if num_list[mid] == target:
                    return mid
                elif num_list[mid] > target:
                    ceiling = mid - 1
                else:
                    floor = mid + 1
            return None

        if len(nums) < 3:
            return []
        nums.sort()
        results = set()
        current_pointer = 0
        while current_pointer <= len(nums) - 3:
            second_pointer = current_pointer + 1
            while second_pointer <= len(nums) - 2:
                two_sum = nums[current_pointer] + nums[second_pointer]
                complement = 0 - two_sum
                complement_index = binary_search(nums, second_pointer + 1, complement)
                if complement_index:
                    results.add((nums[current_pointer], nums[second_pointer], nums[complement_index]))
                second_pointer += 1
            current_pointer += 1

        return results

    def threeSumAnotherOne(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        current_index = -1
        while current_index <= len(nums) - 3:
            current_index += 1
            print(current_index)
            if current_index >= 1 and nums[current_index] == nums[current_index - 1]:
                continue
            complements_map = {}
            second_index = current_index + 1
            while second_index <= len(nums) - 1:
                if nums[second_index] not in complements_map:
                    complements_map[-nums[current_index] - nums[second_index]] = 1
                else:
                    res.add((nums[current_index], -nums[current_index] - nums[second_index], nums[second_index]))
                second_index += 1
        return res

    def threeSumFastest(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i - 1]:
                continue
            d = {}
            for x in nums[i + 1:]:
                if x not in d:
                    d[-v - x] = 1
                else:
                    res.add((v, -v - x, x))
        return map(list, res)

nums = [-1, 0, 1, 2, -1, -4]
soln = Solution()
print(soln.threeSum(nums))
print(soln.threeSumFaster(nums))
print(soln.threeSumFastest(nums))


