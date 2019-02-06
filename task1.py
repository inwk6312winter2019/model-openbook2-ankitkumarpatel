# model openbook 2 :   task 1

# Easy: A tuple of (STR_NAME,FULL_NAME,FROM_STR,TO_STR) 

def tuple_required(filename):
	fin = open(filename,'r')
	for line in fin:
		line = line.split(",")
		tup = (line[2],line[4],line[6],line[7])
		print(tup)
    
















fin = open('Street_Centrelines.csv','r')

print(tuple_required('Street_Centrelines.csv'))



