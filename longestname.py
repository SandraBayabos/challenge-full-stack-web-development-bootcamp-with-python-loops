names = ['Sheng', 'Kevin', 'Audrey', 'KJ', 'Delilah', 'Josh', 'Mack', 'Rey']
longest_name = ""
for name in names:
    if len(name) > len(longest_name):
        longest_name = name

print(longest_name)
