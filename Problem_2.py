#Time Complexity = O(logn)
#Space Complexity = O(n)
# In this we perform modified binary search where we first check which half is sorted and then if the element is in the sorted half then we perform 
# same operation untill element is found else we return -1 
class Solution:
    def search(self, nums, target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low+(high-low)//2

            if nums[mid] == target:
                return mid
            elif nums[low]<=nums[mid]:
                if nums[low]<=target and nums[mid]>target:
                    high= mid -1
                else:
                    low = mid + 1           
            else:
                if nums[mid] < target and nums[high] >= target:
                    low = mid+1
                else:
                    high = mid - 1
        return -1
        
        