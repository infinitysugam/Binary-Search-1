#Time Complexity = O(logn)
#Space Complexity = O(1)
#First we find the search space by increasing the high by times 2.If target is less than the high element 
#We stop and perform the binary search in that.


class Solution:
    def search(reader,target):
        low = 0
        high = 1

        while (reader.get(high) < target):
            low = high
            high = high * 2
        
        while (low<=high):
            mid = low + (high-low)//2
            if target == reader.get(mid):
                return mid
            if reader.get(mid) > target:
                high = mid -1
            else:
                low = mid + 1
            
        return -1