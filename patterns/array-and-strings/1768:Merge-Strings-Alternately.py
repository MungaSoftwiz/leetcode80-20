#!/usr/bin/python3

# https://leetcode.com/problems/merge-strings-alternately/description/
# difficulty: easy
# tags: array(list), string, two pointer
# Pattern: String builder pattern. (Allows changes to be made in place)

# Problem
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
# starting with word1. If a string is longer than the other, append the additional
# letters onto the end of the merged string. Return the merged string.

# Approach
# Use a two pinter to keep track of the position in the two strings.
# Use an empty list(string builder) for efficiency.
# After inserting a char in the list increment pointer and change pointeer to other word.
# Repeat process until both words are depleted.
# It would be time consuming to do this in a string so we make a list and then .join the chars to a string.

# Solution: 0(n + m) for both time & space complexity


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len , word2_len = len(word1), len(word2)
        x, y = 0, 0
        merged_string = []
        word_pos = 1

        while x < word1_len and y < word2_len:
            if word_pos == 1:
                merged_string.append(word1[x])
                x += 1
                word_pos = 2
            else:
                merged_string.append(word2[y])
                y += 1
                word_pos = 1

        # Handles cases for larger string
        while x < word1_len:
            merged_string.append(word1[x])
            x += 1
        while y < word2_len:
            merged_string.append(word2[y])
            y += 1

        return "".join(merged_string)
