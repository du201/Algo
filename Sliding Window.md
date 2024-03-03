The sliding window technique can only be used if the constraint can be broken by increasing the right pointer and then can be restored by increasing the left pointer. In those problems, if you had a window between left and right that fit the constraint, then all windows from x to right also fit the constraint, where left < x <= right. i.e. 

Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".

However, for 