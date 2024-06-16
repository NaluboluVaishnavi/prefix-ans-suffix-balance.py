#5
#1 2 3 4 5
#o/p:[13,9,3,5,15]
a = list(map(int,input().split()))
#sum
ts = 0
ls = 0
rs = 0
cs = 0
ans = []
for i in a:
    ts +=1
#left right diff
for i in a:
    ls +=i
    rs = ts-ls
    cs = abs(rs-ls)
    ans.append(cs)    
print(ans)