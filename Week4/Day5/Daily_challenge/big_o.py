import random
# bubble sort

def bubble(nums):
    iteration = 0
    right_i = len(nums) - 1
    left_i = 0
    while right_i >= 1:
        pos1 = left_i
        pos2 = left_i + 1
        if nums[pos1] > nums[pos2]:
            nums[pos1], nums[pos2] = nums[pos2], nums[pos1] 
            left_i = pos1
            if left_i == right_i - 1:
                right_i -= 1
                left_i = 0
        elif left_i + 1 != right_i:
            left_i += 1
        else:
            left_i = 0    
        iteration += 1
    print(nums)
    print(iteration) 

def quick(nums):
    pass    

nums = list(range(12))
random.shuffle(nums)
print(nums)
bubble(nums)