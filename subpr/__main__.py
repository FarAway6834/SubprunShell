from .compile import *
from traceback import print_exc as _print_exc

class main:
    def __new__(cls, *argv, _a = a):
        cls.__init__(*argv) if len(argv) else cls.__new__(*_a)
    
    def __init__(self, *argv):
        self.__do_while_condition = True
        self(*argv)

    def __call__(self, *argv):
        L = len(argv)
        if L:
            self.__runfile(*argv)
        else:
            while self.__do_while_condition:
                cmd = input('$ ')
                self.__do_while_condition = (cmd != 'exit')
                runlinef(cmd)()
    
    def __runfile(self, file):
        with open(file) as fp:
            for f in map(runlinef, map(ignorlast, fp.readline())):
                f()

if __name__ == "__main__" : main()