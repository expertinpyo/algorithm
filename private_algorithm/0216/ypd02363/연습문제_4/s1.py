def atoi_while(my_str):
    i = 0
    new_num = 0
    while i < len(my_str):
        str_num = ord(my_str[i]) - ord('0')
        new_num = new_num * 10 + str_num
        i += 1
    return new_num

# atoi (ASCII to Integer) - for

def atoi_for(num_str):
    new_num = 0
    for i in range(len(num_str)):
        str_num = ord(num_str[i]) - ord('0')
        new_num = new_num * 10 + str_num
    return new_num

my_str = '123'
print(my_str, type(my_str))   # 123, str

my_int0 = atoi_for(my_str)
print(my_int0, type(my_int0))   # 123, int

my_int1 = atoi_while(my_str)
print(my_int1, type(my_int1)) # 123, int

my_int2 = int(my_str)
print(my_int2, type(my_int2)) # 123, int
