import pickle
data = set(x for x in range(123))

with open('files/first.pickle', 'wb') as file:
    pickle.dump(data,file)

with open('files/first.pickle', 'rb') as file:
    x = pickle.load(file)
    print(x)