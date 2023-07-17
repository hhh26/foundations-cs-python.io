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

def convert_dic_to_json(dictionary):
  json_data = "{"
  for key, value in dictionary.items():
      json_data += f'"{key}": '
      if isinstance(value, dict):
        json_data = convert_dic_to_json(value) + ","
      else:
        json_data += f'"{value}"'
  
  json_data = json_data.rstrip(",") + '}'
  return json_data

def write_dic_to_json(dictionary, filename):
  with open(filename, 'w') as file:
    json_data = convert_dic_to_json(dictionary)
    file.write(json_data)

data = {
    "students": 
    [
      {
      'name': 'Youssef', 
      'age': 31
      },
      {
      'name': 'Antoine',
      'age': 26
      }
    ]
      }

write_dic_to_json(data, 'ex2.json')
