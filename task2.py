# model openbook 2 :   task 2

#- Accessible and in a ARTERIAL road
def access_arter(file1,file2):
	bus_stop = dict()
	fin1 = open(file1, 'r')
	fin2 = open(file2, 'r')
	for line_f1 in fin1:
		for line_f2 in fin2:
			line_f1 = line_f1.split(",")
			line_f2 = line_f2.split(",")
			if 'Accessible'in line_f2[9]:
				if 'ARTERIAL' in line_f1[12]:
					bus_stop[line_f2[3]] = bus_stop.get(line_f2[3],0)+1
		
	return (bus_stop)


#- Non-Standard and in a LOCAL STREET








#- Inaccessible and in a MINOR COLLECTOR








print(access_arter('Street_Centrelines.csv','Bus_Stops.csv'))
