file_path = '../files/ex.txt'

f = open(file_path, 'r', encoding='utf8')
contents = f.read()
print(contents)
f.close()
#  with open(file_path, mode='a', encoding='utf8') as f:
#      f.write('11111111111 \n')
#      f.write('ываыфва \n')
# with open(file_path, mode='r',encoding='utf8') as f:
#     for i in f:
#         print(i)
# f.close()