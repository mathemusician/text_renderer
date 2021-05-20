'''
has functions to help speed up the work

'''

import os
import pickle as pl
import time


class getpath(str):
    '''
If file lives in .../MtgFi/a/b/c.txt, just write:

getpath("a","b","c.txt")

this returns the path: .../MtgFi/a/b/c.txt


On Windows, both give you the same result:


getfile(r"\a\b\c.txt")
getfile("a","b","c.txt")

    '''
    def __new__(cls, *args, recursive=False):
        if recursive:
            paths = []
        else:   
            paths = [os.path.dirname(os.path.realpath(__file__))]
        
        for arguments in args:
            paths.append(arguments)
        
        path = os.sep.join(paths)
        return str.__new__(cls, path)
    
    def __init(self):
        super().__init__(self)
    
    def add(self, *args):
        paths = []
        for arguments in args:
            paths.append(arguments)
        
        path = os.sep.join([self.__str__(), os.sep.join(paths)])
        return getpath(path, recursive=True)


def pickle(data, path):
    '''
pickle(data, 'path/to/pickled/file')


    '''

    with open(path, 'wb') as file_handler:
        pl.dump(data,file_handler)


def unpickle(path):
    '''
unpickle('path/to/pickled/file')

    '''
    with open(path, 'rb') as file_handler:
        return pl.load(file_handler)


class Timer(object):
    '''

Useful for timing stuff

timer = Timer()

# first process
timer.start()
process1()
timer.stop()
print(timer.elapsed())

# second process
timer.start()
process2()
timer.stop()
print(timer.elapsed())

    '''
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()
    
    def stop(self):
        self.end_time = time.time()
        print(self.elapsed())
    
    def elapsed(self):
        return self.end_time - self.start_time


if __name__ == '__main__':
    #print(getfile('path', 'to', 'file'))
    pickle(2,getfile('test','fine.txt'))
    print(3*unpickle(getfile('test', 'fine.txt')))