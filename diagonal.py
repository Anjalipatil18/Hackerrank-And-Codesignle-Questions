diagonal_list=[[8,3,4],[1,5,9],[6,7,2]]
i=0
new_list=[]
sum=0
j=0
while i<len(diagonal_list):
	new_list.append(diagonal_list[i][j])
	sum=sum+new_list[i]
	i=i+1
	j=j+1
	k=-1
	sum=0
	m=0
	new_list1=[]
	while k>=(-len(diagonal_list)):
		new_list1.append(diagonal_list[k][m])
		sum=sum+new_list1[m]
		k=k-1
		m=m+1
print new_list
print new_list1
print sum