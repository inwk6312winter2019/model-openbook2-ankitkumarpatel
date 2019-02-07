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

# List of unique owners for the streets ["OWN"]
def unique_owners(filename):
	lst = []
	fin = open(filename,'r')
	for line in fin:
		line = line.split(",")
		lst.append(line[11])
	lst=list(dict.fromkeys(lst))
	return(lst)

# Different types of Street classes ["ST_CLASS"] and a list of streets undereach class
def street(filename):
	street_class_dict = dict()
	fin = open(filename, 'r')
	for line in fin:
		line = line.split(",")
		if line[10] not in street_class_dict:
			street_class_dict[line[10]] = [line[2]]
		else:
			street_class_dict[line[10]].append(line[2])
	return (street_class_dict)

fin = open('Street_Centrelines.csv','r')
print("\nResult of subtask 1: ")
print(tuple_required('Street_Centrelines.csv'))


print("\nResult of subtask 2: ")
print(maintenance_histogram('Street_Centrelines.csv'))

print("\nResult of subtask 3: ")
print(unique_owners('Street_Centrelines.csv'))

print("\nResult of subtask 4: ")
print(street('Street_Centrelines.csv'))
