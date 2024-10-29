
# Alexander J. Jackson
# how_many_ts.py

user_input = input("Enter a sentence: ")
string_count = 0
for x in user_input:
    if x == 'T' or x == 't':
        string_count += 1

print(f'The letter T appears {string_count} times.')
