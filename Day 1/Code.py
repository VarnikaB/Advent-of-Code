file1 = open("input.txt","r")
lines = file1.readlines()
first_list = []
second_list = {}
for line in lines:
    first, second = map(int, line.split())
    first_list.append(first)
    if second not in second_list:
        second_list[second] = 1
    else:
        second_list[second] += 1

total_distance = 0
for i in range(len(first_list)):
    if first_list[i] in second_list:
        total_distance += second_list[first_list[i]] * first_list[i]
print(total_distance)