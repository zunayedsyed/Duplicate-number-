# find duplicate
def find_duplicate():
	x=[1,1,2,2,3]
	z=[]
	for b in x:
		if b not in z:
			z.append(b)
	for c in z:
		x.remove(c)
	print(x)
# function_call
find_duplicate() 
