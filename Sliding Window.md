The sliding window technique can only be used if the constraint can be broken by increasing the right pointer and then can be restored by increasing the left pointer. In those problems, if you had a window between left and right that fit the constraint, then all windows from x to right also fit the constraint, where left < x <= right. i.e. 

Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".

However, for questions that don't satisfy this constraint i.e. N. 560 (Subarray sum equals K), we can't use sliding windows. A common solution is to use prefix sum + hashmap count.

For some other questions, i.e. 2260. Minimum Consecutive Cards to Pick Up, although it doesn't fit exactly the requirement to use sliding window, we can still use modified sliding window solution to solve it, although this specific question has many solutions.