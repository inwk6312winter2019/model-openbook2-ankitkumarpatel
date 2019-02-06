# model openbook 2 :   task 1

# Easy: A tuple of (STR_NAME,FULL_NAME,FROM_STR,TO_STR) 

def tuple_required(filename):
	fin = open(filename,'r')
	for line in fin:
		line = line.split(",")
		tup = (line[2],line[4],line[6],line[7])
		print(tup)
    
# A histogram of the different types of maintenance. [Result has to be a dictionary with key as Maintenance  and number of streets as values] ["MAINTENANCE"]

def maintenance_histogram(filename):
	maintenance_types = dict()
	fin = open(filename,'r')
	for line in fin:
		line = line.split(",")
		maintenance_types[line[12]]=maintenance_types.get(line[12],0)+1
	return(maintenance_types)














fin = open('Street_Centrelines.csv','r')

print(tuple_required('Street_Centrelines.csv'))

print(maintenance_histogram('Street_Centrelines.csv'))

