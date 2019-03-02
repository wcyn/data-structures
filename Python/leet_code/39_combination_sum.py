class Solution(object):
    def combinationSumRecursive(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []

        def get_combinations(candidates, target, current_path, combinations, current_sum=0):

            complement = target - current_sum
            valid_complementors = []
            for num in candidates:
                if num <= complement:
                    valid_complementors.append(num)
            # print candidates, target, current_path, combinations, current_sum, valid_complementors
            if not valid_complementors:
                return

            for index, complementor in enumerate(valid_complementors):
                current_path.append(complementor)
                if current_sum + complementor == target:
                    combinations.add(tuple(sorted(current_path)))
                    current_path.pop()
                    return

                get_combinations(
                    candidates,
                    target,
                    current_path,
                    combinations,
                    current_sum + complementor
                )

                current_path.pop()

        combinations = set()
        candidates.sort()
        get_combinations(candidates, target, [], combinations)
        combinations = list(combinations)
        return combinations

    def combinationSum3(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []

        current_sum = 0
        combinations = set()
        complement = target - current_sum
        current_path = []
        candidates.sort()
        valid_stack = [num for num in candidates if num <= complement]
        while valid_stack:
            # print valid_stack, current_path, current_sum
            current_num = valid_stack.pop()
            while current_num == "" and valid_stack:
                current_sum -= current_path.pop()
                current_num = valid_stack.pop()
            current_path.append(current_num)

            if not valid_stack:
                break

            if current_num + current_sum == target:
                combinations.add(tuple(sorted(current_path)))
                current_path.pop()

            else:
                prior_stack_length = len(valid_stack)
                current_sum += current_num
                complement = target - current_sum
                valid_stack.append("")
                for num in candidates:
                    if num <= complement:
                        valid_stack.append(num)

                if prior_stack_length == len(valid_stack) - 1:
                    # print "Nothing: ", current_path, current_sum
                    # Nothing was added
                    current_sum -= current_num
                    current_path.pop()
                    valid_stack.pop()

        return list(combinations)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []

        combinations, num_path = [], []
        candidates.sort()

        def get_combinations(candidates, remainder, num_path, combinations, start):
            if remainder < 0:
                return
            elif remainder == 0:
                combinations.append(list(num_path))
            else:
                for num_index in range(start, len(candidates)):
                    current_num = candidates[num_index]
                    num_path.append(current_num)
                    get_combinations(candidates, remainder - current_num, num_path, combinations, num_index)
                    num_path.pop()

        get_combinations(candidates, target, num_path, combinations, 0)
        return combinations

    def combinationSum5(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        dict = {}  # its value type is List[List[int]]
        return self.search(target, candidates, dict)

    def search(self, current, candidates, dict):
        if current in dict:  # if combinations of this value have been computed, don't do it again
            return dict[current]

        new_combinations = []
        for candidate in candidates:
            if candidate > current:
                break
            elif candidate == current:
                new_combinations.append([current])
            elif candidate * 2 > current:
                continue
            # because if ture, then current - candidate < candidate, means no combinations of current -
            # candidate can meet the condition below: if candidate <= an_old_combination[0]:
            else:
                old_combinations = self.search(current - candidate, candidates, dict)
                for an_old_combination in old_combinations:
                    if candidate <= an_old_combination[0]:  # to make the combinations unique by make the list ascending
                        new_combinations.append([candidate] + an_old_combination)

        dict[current] = new_combinations  # memorize
        return dict[current]

    def combinationSumImprovement(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        combinations = []

        def get_combinations(candidates, remainder, combinations, num_path, current_index):
            num_path.append(candidates[current_index])
            # print candidates, remainder, combinations, num_path, current_index
            if remainder < 0:
                num_path.pop()
                return

            if remainder == 0:
                combinations.append(tuple(num_path))
                num_path.pop()
                return

            for candidate_index in range(current_index, len(candidates)):
                get_combinations(candidates, remainder - candidates[candidate_index], combinations, num_path,
                                 candidate_index)
            num_path.pop()

        for candidate_index in range(len(candidates)):
            num_path = []
            get_combinations(candidates, target - candidates[candidate_index], combinations, num_path, candidate_index)

        return combinations
