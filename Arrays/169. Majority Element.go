import (
	"math"
 )
 
 func majorityElement(nums []int) int {
	 majority := int(math.Floor(float64(len(nums) / 2)))
 
	 countMap := make(map[int]int)
 
	 for i := 0; i < len(nums); i++ {
		 if _, ok := countMap[nums[i]]; ok {
			 countMap[nums[i]]++
		 } else {
			 countMap[nums[i]] = 1
		 }
	 }
 
	 for k, v := range countMap {
		 if v > majority {
			 return k
		 }
	 }
 
	 return 0
 }