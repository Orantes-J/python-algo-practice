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