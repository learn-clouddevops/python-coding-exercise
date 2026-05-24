my_list = ["apple", "banana","banana","apple","orange"]


new_count = {}

for count in my_list:
    new_count[count] = new_count.get(count,0) + 0
    new_count[count] += 1

print(new_count)    
