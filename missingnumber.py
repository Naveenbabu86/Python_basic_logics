"""

Input: [1, 2, 3, 5, 6]
Output: 4
"""

nums = [1, 2, 3, 5, 6]

for i in range(len(nums) - 1):
    # Check the gap between consecutive numbers
    if nums[i + 1] - nums[i] > 1:
        print("Missing number is:", nums[i] + 1)
        break


    




