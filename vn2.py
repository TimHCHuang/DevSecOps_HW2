import pickle
malobj = pickle.load(open('./mybug.pickle', 'rb'))
print("=== It is my test ===")
print(repr(malobj))
