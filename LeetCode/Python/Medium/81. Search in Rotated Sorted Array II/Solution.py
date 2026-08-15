class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        low = 0 
        high = len(nums)-1

        while low<=high:
            mid = (low + high)//2
            if nums[mid] == target:
                return True

            if nums[mid] == nums[low] == nums[high]:
                low +=1
                high -=1
                continue

            #check if left part is sorted or not
            if nums[mid]>=nums[low]:
                if target>=nums[low] and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            #else right part is sorted        

            else:
                if target <= nums[high] and target >= nums[mid]:
                    low = mid +1
                else:
                    high = mid - 1

        return False


