x,y,z=map(int,input().split())
total_time_req=x*y
available_time=z*1440
if total_time_req <= available_time:
    print("YES")
else:
    print("NO")
