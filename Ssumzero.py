def closest_to_zero(nums):
    nums.sort()  # Step 1: Sort the array
    left, right = 0, len(nums) - 1
    min_sum = float('inf')
    pair = (0, 0)

    # Step 2: Use two pointers
    while left < right:
        curr_sum = nums[left] + nums[right]

        # Step 3: Update if closer to zero
        if abs(curr_sum) < abs(min_sum):
            min_sum = curr_sum
            pair = (nums[left], nums[right])

        # Step 4: Move pointers logically
        if curr_sum < 0:
            left += 1
        else:
            right -= 1

    return pair


closest_to_zero( [1, 60, -10, 70, -80, 85])
