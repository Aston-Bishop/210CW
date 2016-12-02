input_list = [1,2,3,4,1,5,1,6,7]
output_list = []
placement_list = []                                  # This is to hold the current ascending list

for i in range(0,len(input_list)):
    placement_list.append(input_list[i])
    print(placement_list)
    if input_list[i] > input_list[i+1]:
        if len(placement_list) > len(output_list):
            output_list = placement_list
            placement_list = []
        else:
            placement_list = []
