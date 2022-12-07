def duplicate(input_list):
    new_dict, new_list = {}, []
 
    for i in input_list:
        if not i in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1
 
    for key, values in new_dict.items():
        if values > 1:
            new_list.append(key)
 
    return new_list
 
if __name__ == '__main__':
    input_list = [12,54,68,759,24,15,12,68,987,758,25,69]
    print(duplicate(input_list))
 