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

# Create a function that takes the above text and returns a dictionary which has words as it's keys and their frequency as it's values.`
zen_python = '''

The Zen of Python, by Tim Peters


Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Flat is better than nested.

Sparse is better than dense.

Readability counts.

Special cases aren't special enough to break the rules.

Although practicality beats purity.

Errors should never pass silently.

Unless explicitly silenced.

In the face of ambiguity, refuse the temptation to guess.

There should be one-- and preferably only one --obvious way to do it.

Although that way may not be obvious at first unless you're Dutch.

Now is better than never.

Although never is often better than *right* now.

If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea.

Namespaces are one honking great idea -- let's do more of those!

'''
# import string

# def find_frequency(input_string):
#     return_dictionary = {}
#     input_list = ' '.join([c for c in input_string if c not in string.punctuation])
#     lis = input_string.split()
#     for word in lis:
#         if return_dictionary[word]:
#             return_dictionary[word] += 1
#         else:
#             return_dictionary[word] = 1
#     print(return_dictionary)

# find_frequency('hey hows it going hey im ok hey ok')
#try using a set that has unique values and add the frequency