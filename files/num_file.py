import sys
file = open("population.txt")
file_list = file.readlines()
file.close()

year = int(sys.argv[1])
start_year = int(file_list[0])
idx = (year - start_year) + 1

print(file_list[idx])