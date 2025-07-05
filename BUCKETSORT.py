from collections import defaultdict
def top_freq(nums:list[int],k:int)->list[int]:
    freq_map=defaultdict(int)
    for num in nums:
        freq_map[num]+=1
    bucket=[[]for _ in range(len(nums)+1)]
    for num,freq in freq_map.items():
        bucket[freq].append(num)
    result=[]
    for i in range(len(bucket)-1,0,-1):
        for num in bucket[i]:
            result.append(num)
            if len(result)==k:
                return result
nums_in=input("enter the list")
nums=list(map(int,nums_in.strip().split()))
k=int(input("enter the value of k:"))
result=top_freq(nums,k)
print(result)
