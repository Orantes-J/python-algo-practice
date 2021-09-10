# REVERSE LIST
a_list = [100, 200, 300, 400, 500]

reversed_list = []

for i in a_list[::-1]:
    reversed_list.append(i)

print(reversed_list)

# CONCATENATE TWO LIST ITEMS

list1 = ['M', 'na', 'i', 'ke']
list2 = ['y', 'me', 's', 'lly']

new_list = []

for i in range(4):
    word = []
    word.append(list1[i])
    word.append(list2[i])
    send_word = "".join(word)
    new_list.append(send_word)

print(new_list)

# SQUARE EACH ITERATION

a_list = [1,2,3,4,5,6,7]

new_list = []

for i in a_list:
    new_num = i*i
    new_list.append(new_num)

print(new_list)

# CONCATENATE TWO LIST IN SPECFIC ORDER ---  Two ways

list1 = ['hello ', 'take ']
list2 = ['dear', 'sir']

new_list = [i+j for i in list1 for j in list2 ]        

new_list1 = []
for i in list1:
    for j in list2:
        word = i+j
        new_list1.append(word)

print(new_list1)


print(new_words)

# CONCATENATE WITH ZIP METHOD

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

x = zip(list1, list2[::-1])

print(tuple(x))
