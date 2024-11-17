def unique_elements(n,arr):
    seen=set()
    result=[]
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
n=int(input())
arr=list(map(int,input().split()))
unique_result=unique_elements(n,arr)
print(" ".join(map(str, unique_result)))
