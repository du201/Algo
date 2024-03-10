class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        temp_decreasing_stack = []

        for idx, temp in enumerate(temperatures):
            removed_idx = idx - 1
            while len(temp_decreasing_stack) > 0 and temperatures[temp_decreasing_stack[-1]] < temp:
                pop_idx = temp_decreasing_stack.pop()
                ans[pop_idx] = idx - pop_idx

            temp_decreasing_stack.append(idx)

        return ans