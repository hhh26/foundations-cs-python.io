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
