# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

##notes and breaking the problem down

# we have and array of at least 2 int

# we have n inputs in the array
# we have n outputs int eh output array

# Each output is the product of all the inputs, except the input at the index of the outpput.

# [1,2,3,4]

# [24, 12, 8 ,6]

 ### planning ###


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        # for i in nums range(len(nums)):
        #         product = 1
        #         for j in range(len(nums)):
        #             if i != j:
        #                 product *= nums[j]
        #             output.append(product)
        
        # product = 1

        # for i in nums range(len(nums)):
        #     product *= nums[i]

        # output = [product] * len(nums)

        # for i in range(len(output)):
        #     output[i] //= nums[i]



        return output        