class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        combinations = []
        paths = {}
        candidates.sort()
        num_path = []

        def get_combinations(candidates, remainder, combninations, num_path, num_index, paths):
            num_path.append(candidates[num_index])
            path = tuple(num_path)
            # print candidates, remainder, combninations, num_path, num_index, paths
            if path in paths:
                # print("Path! ", path)
                num_path.pop()
                return paths[path]

            if remainder < 0:
                num_path.pop()
                paths[path] = None
                return

            if remainder == 0:
                num_path.pop()
                paths[path] = None
                combinations.append(path)
                return

            for index in range(num_index + 1, len(candidates)):
                paths[path] = get_combinations(
                    candidates, remainder - candidates[index], combinations,
                    num_path, index, paths
                )
            num_path.pop()

        for num_index in range(len(candidates)):
            get_combinations(
                candidates, target - candidates[num_index], combinations,
                num_path, num_index, paths
            )
        return combinations
