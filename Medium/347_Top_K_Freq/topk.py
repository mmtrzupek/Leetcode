# 347. Top K Frequent Elements (Medium)
# O(nlog(n)) because we are sorting a dict

nums = [1,1,2,5,4,4,3,4,4,1,2,1,4]
k = 3

def topKFrequent(nums, k):
    d = {}
    ans = []
    
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = 1
        else:
            d[nums[i]] += 1
    
    # Figure out how to do this problem without using lambda or sorting
    for key_, _ in sorted(d.items(), key=lambda index: index[1], reverse=True)[:k]:
        ans.append(key_)
        
    return ans
        
        
print(topKFrequent(nums, k))