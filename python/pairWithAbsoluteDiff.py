#find the no.of pair in a list with the difference k .
import time
start=time.time()
nk=input().rstrip().split()
n=int(nk[0])
k=int(nk[1])
a=list(map(int,input().split()))
#for i in range(n):
#	a.append(int(input()))
f=0
r=1
count=0
a.sort()
while( r <n-1):
	if(f-r == k):
		r=r+1
		count+=1
	elif(r-f<k):
		r+=1
	elif(r-f >k):
		f=f+1
print(count)
end=time.time()
print(end-start)
