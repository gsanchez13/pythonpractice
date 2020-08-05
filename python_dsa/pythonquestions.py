def count_string(raw_string, string_to_count):
    return raw_string.lower().count(string_to_count.lower())

# print(count_string('Welcome to nyc. NYC is the best!', 'nyc'))
# print(count_string('Welcome to nyc!', 'NYC'))

def reverse_string_by_word(raw_string):
    slist = raw_string.split()
    print(slist)
    slist.reverse()
    print(slist)
    return ' '.join(slist)
# print(reverse_string_by_word('Reversing Strings is Confusing says: Yoda'))

# def find_special_numbers(start_num, end_num):
#     all_nums = [n for n in range(start_num, end_num + 1) if n % 7 == 0 if n % 5 != 0]
#     return all_nums
# print(find_special_numbers(0,20))

def find_special_numbers(start_num, end_num):
    l = [ str(i) for i in range(start_num, end_num +1) if(i % 7 == 0 and i % 5 != 0)]
    print(l)
    return ', '.join(l)
# print(find_special_numbers(0,20))

