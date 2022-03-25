file_names_list = ['1.txt', '2.txt', '3.txt']
files_dict = {}

for file_name in file_names_list:
    with open(file_name) as file:
        lines = file.readlines()
        files_dict[file_name] = len(lines)
sorted_dict = dict(sorted(files_dict.items(), key=lambda item: item[1]))
print(sorted_dict)
for key, value in sorted_dict.items():
    lines = None
    with open(key) as file:
        lines = file.read()
    with open('newfile.txt', 'a') as doc:
         doc.write(key)
         doc.write('\n')
         doc.write(str(value))
         doc.write('\n')
         doc.write(lines)
         doc.write('\n')


