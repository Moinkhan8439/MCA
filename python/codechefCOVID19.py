t=int(input())
for i in range(t):
	n=int(input())
	l=input().split()
	res=[]
	count=1
	flag=False
	for i in range(1,n):
		 if(int(l[i])-int(l[i-1])>2):
		 	flag=True	
		 else:count+=1
		 if(flag==True and i==n-1):
		 	res.append(1)
		 if(flag==True or i==n-1):
		 	res.append(count)
		 	flag=False
		 	count=1	 
	print(*res)
	print(min(res),max(res))
	 	
	
