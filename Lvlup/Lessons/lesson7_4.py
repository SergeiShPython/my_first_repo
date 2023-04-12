import os , pathlib
print(os.listdir())
print(os.listdir('../files/'))

for entry in os.listdir():
    if os.path.isfile(entry):
        print(entry)
try:
    os.mkdir('dir')
except FileExistsError as exc:
    print(exc)
