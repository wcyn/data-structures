# https://leetcode.com/problems/median-of-two-sorted-arrays/
def merge_lists(l1, l2):
            merge = []
            len_1 = len(l1)
            len_2 = len(l2)

            if len_1 > len_2: big_list, small_list = l1, l2
            else: big_list, small_list = l2, l1

            big = small = 0
            while small < len(small_list) and big < len(big_list):
                print(small)
                print(big, end="\n\n")
                if small_list[small] < big_list[big]:
                    merge.append(small_list[small])
                    small += 1
                elif small_list[small] > big_list[big]:
                    merge.append(big_list[big])
                    big += 1
                else:
                    merge.append(small_list[small])
                    merge.append(big_list[big])
                    small += 1
                    big += 1

            if len(big_list) > big:
                merge += big_list[big:]
            elif len(small_list) > small:
                merge += small_list[small:]
            return merge

print(merge_lists([3], [-2, -1]))