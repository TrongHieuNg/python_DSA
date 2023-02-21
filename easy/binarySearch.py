  """
  Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
  If target exists, then return its index. Otherwise, return -1.
  
  Time complexity: O(logn)
  
  Space complextiy: O(1)
  """
  
  # recursive approach
  def search(nums):

      def rec(nums, target, low, high):
          while high >= low:

              mid = (low + high) // 2

              if nums[mid] == target:
                  return mid
              elif nums[mid] > target:
                  return rec(nums, target, low, mid - 1)
              else:
                  return rec(nums, target, mid + 1, high)

          return -1

      return rec(nums, target, 0, len(nums) - 1)
    
  # iterative approach
  def search(self, nums: List[int], target: int) -> int:

      start, end = 0, len(nums) - 1

      while start <= end:
          mid = (start + end) // 2
          if target == nums[mid]:
              return mid

          elif target < nums[mid]:
              end = mid - 1

          else:
              start = mid + 1

      return -1
