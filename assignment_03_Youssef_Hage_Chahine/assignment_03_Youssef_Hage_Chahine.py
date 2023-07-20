# ex 1:

def sumTuples(tup1, tup2):
    sum_tup = ()
    list_sum = list(sum_tup)
    max_len = max(len(tup1), len(tup2))

    for i in range(max_len):
        if i < len(tup1) and i < len(tup2):
            tup_sum = tup1[i] + tup2[i]
            list_sum.append(tup_sum)
    
    sum_tup = tuple(list_sum)
    return sum_tup

tup1 = ()
tup2 = ()

ln = int(input('enter the desire length: '))

for i in range(ln):
  lst1 = list(tup1)
  i = int(input('enter number for tuple 1: '))
  lst1.append(i)
  tup1 = tuple(lst1)

for j in range(ln):
  lst2 = list(tup2)
  j = int(input('enter a number for tuple 2: '))
  lst2.append(j)
  tup2 = tuple(lst2)

print(tup1, tup2)
print(sumTuples(tup1, tup2))


# ex 2:

def write_dic_to_json(dictionary, filename):
  with open(filename, 'w') as file:
    json_data = convert_dic_to_json(dictionary)
    file.write(json_data)

def convert_dic_to_json(dictionary):
  json_data = "{"
  for key, value in dictionary.items():
      json_data += f'"{key}": '
      
      if isinstance(value, dict):
        json_data = convert_dic_to_json(value) + ","
      else:
        json_data += f'"{value}",'
  
  json_data = json_data.rstrip(",") + '}'
  return json_data

data = {
  "name": "Youssef", 
  "age": 31
  }
write_dic_to_json(data, 'assignment_03_Youssef_Hage_Chahine\ex2.json')


# ex 3:

def convert_json_to_dict(filename):
  with open(filename, 'r') as file:
    json_data2 = file.read()
  
  lst2 = []
  while json_data2:
    end_index = json_data2.find('}')
    
    if end_index == -1:
      break
    
    data_dic = json_data2[:end_index + 1]
    convert_to_dic = eval(json_data2, {'true': True, 'false': False, 'null': None})

    lst2.append(convert_to_dic)

    json_data2 = json_data2[end_index + 1:]
  
  return lst2

filename = 'assignment_03_Youssef_Hage_Chahine\ex3.json'
json_to_dict = convert_json_to_dict(filename)
print(json_to_dict)