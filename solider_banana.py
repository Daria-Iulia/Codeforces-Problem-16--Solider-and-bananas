k,n,w=map(int, input() .split())
contor=0
num=[]
for i in range(w):
    contor+=1
    cost= k*contor
    num.append(cost)
    total = sum(num)
     

cost_adjusted= total - n
    

if cost_adjusted <= 0:
    print(0)
else:
    print(cost_adjusted)
