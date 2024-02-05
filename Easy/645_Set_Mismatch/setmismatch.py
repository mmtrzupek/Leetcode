# 645. Set Mismatch (Easy)
# You have a set of integers s, which originally contains all the numbers from 1 to n. 
# Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

nums = [1,5,3,2,2,7,6,4,8,9]

# print(sorted(nums))
# print(len(nums))

def findErrorNums(nums):
    # Keep track of unique numbers
    seen = set()
        
    # Find Repetitive Number
    for i in range(len(nums)):
        if nums[i] not in seen:
            seen.add(nums[i])
        # Repitive Number Found
        else:
            duplicated_number = nums[i]
    
    # Find Missing Number
    n = len(nums)
    expected_sum = (n*(n+1))//2
    actual_sum = sum(nums)
    missing_number = (expected_sum - actual_sum) + duplicated_number                        
    
    return [duplicated_number, missing_number]

print(findErrorNums(nums))
