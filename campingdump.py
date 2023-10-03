import pickle

parkStatus = {}
try:
    with open('parks.pickle', 'rb') as handle:
        parkStatus = pickle.load(handle)
except FileNotFoundError:
    pass

for value in parkStatus.values():
    if value != "":
        print(value)
