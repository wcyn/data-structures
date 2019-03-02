class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        if not s or not words:
            return []

        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

        word_counts_check = {}
        word_length = len(words[0])

        start_indices = []
        start_index, end_index = 0, word_length - 1
        word_count = 0
        number_of_words = len(words)
        while end_index < len(s):
            current_word = s[start_index: end_index + 1]
            # print current_word
            word_counts_check[current_word] = word_counts_check.get(current_word, 0) + 1
            start_index = end_index + 1
            end_index += word_length
            word_count += 1

            if word_count == number_of_words:
                if word_counts == word_counts_check:
                    start_indices.append(start_index - (number_of_words * word_length))
                # Reset word counts check and word count
                word_counts_check = {}
                word_count = 0
                start_index = start_index - (word_length * number_of_words) + 1
                end_index = start_index + word_length - 1
        return start_indices
