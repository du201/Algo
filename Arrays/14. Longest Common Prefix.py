class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        first_word = strs[0]

        shared_char_count = 0

        for idx, first_word_char in enumerate(first_word):
            do_all_words_have_this_char = True
            for word in strs[1:]:
                if len(word) > idx and first_word_char == word[idx]:
                    pass
                else:
                    do_all_words_have_this_char = False
                    break

            if not do_all_words_have_this_char:
                shared_char_count = idx
                break

            if idx == len(first_word) - 1:
                shared_char_count = idx + 1

        return first_word[0:shared_char_count]

            
                
            

