word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []

for item in word_list:
    if char in item:
        new_list.append(item)
    else:
        continue

print new_list
