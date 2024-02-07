# brute force solution

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        init_remain_gas_arr = []

        for i in range(len(gas)):
            remain_gas = gas[i] - cost[i]
            if remain_gas >= 0:
                init_remain_gas_arr.append({"idx": i, "remain_gas": remain_gas}) 

        def sortByGas(gas_obj):
            return gas_obj["remain_gas"]

        init_remain_gas_arr.sort(reverse=True, key=sortByGas)

        for i in range(len(init_remain_gas_arr)):
            start_idx = init_remain_gas_arr[i]["idx"]
            remain_gas = init_remain_gas_arr[i]["remain_gas"]

            if start_idx == len(gas) - 1:
                moving_idx = 0
            else:
                moving_idx = start_idx + 1

            while moving_idx != start_idx:
                remain_gas += gas[moving_idx]
                remain_gas -= cost[moving_idx]

                if remain_gas < 0:
                    break

                if moving_idx == len(gas) - 1:
                    moving_idx = 0
                else:
                    moving_idx += 1

            # success
            if moving_idx == start_idx:
                return start_idx


        return -1