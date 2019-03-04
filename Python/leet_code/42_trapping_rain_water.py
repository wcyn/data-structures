class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # At least 3 bar heights needed to hold water
        if len(height) < 3:
            return 0

        cumulative_water = 0

        def calculate_water_contained(start_index, stop_index, height):
            return height * (stop_index - start_index - 1)

        def get_max_index(heights):
            max_index = 0
            for index in range(len(heights)):
                if heights[index] > heights[max_index]:
                    max_index = index
            return max_index

        max_height_block_index = get_max_index(height)
        next_block_index = 0

        for block_index in range(max_height_block_index):
            if block_index < next_block_index:
                cumulative_water -= height[block_index]
            else:
                for second_index in range(block_index + 1, max_height_block_index + 1):
                    if height[second_index] >= height[block_index]:
                        cumulative_water += calculate_water_contained(
                            block_index, second_index, height[block_index]
                        )
                        next_block_index = second_index
                        break

        next_block_index = len(height) - 1
        for block_index in range(len(height) - 1, max_height_block_index - 1, -1):
            if block_index > next_block_index:
                cumulative_water -= height[block_index]
            else:
                for second_index in range(block_index - 1, max_height_block_index - 1, -1):
                    if height[second_index] >= height[block_index]:
                        cumulative_water += calculate_water_contained(
                            second_index, block_index, height[block_index]
                        )
                        next_block_index = second_index
                        break
        return cumulative_water

