# 1. Two Sum (Easy)

# Inputs
nums = [3,2,4]
target = 6

# Solution 1: Two loops (O(n^2)) runtime

# def TwoSum(nums, target):
#     ans = []
#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 ans = [i, j]
#                 return ans
    
#     return ans
            
# Solution 2: Using Hashmap (O(n)) runtime

def TwoSum(nums, target):
    ans = []
    # key = number, value = index
    d = {}
    
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in d:
            ans = [d[complement], i]
            return ans
        else:
            # todo
            d[nums[i]] = i
    
    
    for k,v in d.items():
        print(k,v)
    return ans

print(TwoSum(nums, target))
            