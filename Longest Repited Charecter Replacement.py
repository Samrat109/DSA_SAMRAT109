#You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
#Return the length of the longest substring containing the same letter you can get after performing the above operations.

class Solution(object):

    def characterReplacement(self, s, k):

        count = {}
        left = 0
        max_count = 0
        answer = 0

        for right in range(len(s)):

            count[s[right]] = count.get(s[right], 0) + 1

            max_count = max(max_count, count[s[right]])

            window_length = right - left + 1
            replacements = window_length - max_count

            while replacements > k:

                count[s[left]] -= 1
                left += 1

                window_length = right - left + 1
                replacements = window_length - max(count.values())

            answer = max(answer, right - left + 1)

        return answer