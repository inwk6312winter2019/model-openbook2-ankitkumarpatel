# model openbook 2 :   task 2

def readingfile(filename):
    lst = [] 
    fin = open(filename, 'r')
    for line in fin:
        line= line.strip().split(',')
        lst.append(line) 
    return(lst)


def busstops(street_data,busstop_data):
    count_arterial_access = 0
    count_local_non = 0
    count_minor_inacess = 0


    for line in street_data:
        if 'ARTERIAL' in line[10]:
            for data in busstop_data:
                if 'Accessible' in data[7]:
                    if line[23] == data[9]:
                        count_arterial_access += 1

        elif 'LOCAL STREET' in line[10]:
            for data in busstop_data:
                if 'Non-Standard'in data[7]:
                    if line[23] == data[9]:
                        count_local_non += 1

        elif 'MINOR COLLECTOR' in line[10]:
            for data in busstop_data:
                if 'Inaccessible'in data[7]:
                    if line[23] == data[9]:
                        count_minor_inacess += 1

    return (count_arterial_access,count_local_non,count_minor_inacess)


street_list = readingfile('Street_Centrelines.csv')
busstop_list = readingfile('Bus_Stops.csv')
print("Bus stop data ::\n\nAccessible and in a ARTERIAL road: %d \nNon-Standard and in a LOCAL STREET: %d \nInaccessible and in a MINOR COLLECTOR: %d"% busstops(street_list,busstop_list))
