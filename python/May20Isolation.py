for i in range(int(input())):
	n,q=(int(x) for x in input().split())
	s=input()
	l=[0]*26
	for i in s:
		l[ord(i)-97]+=1
	for i in range(q):
		t=int(input())
		count=0
		for i in l:
			if(i > t):
				count+=i-t
		print(count)
		
	
	
