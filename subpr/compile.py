from .lib import *
from functools import wraps as _smart_deco_wraps
from sys import argv as _a

o = open
w = lambda f : o(f, 'w')
fmot = lambda f, g : lambda *argv, **kargv : f(g(*argv, **kargv))

def wither(opener = o):
    def with_deco(func):
        @_smart_deco_wraps(func)
        def with_opener(name, *argv, **kargv):
            with opener(name) as man:
                return func(man, *argv, **kargv)

def simple_fixer(read):
    reads = martialaw(wither()(read))
    def simple_fixer_deco(write):
        writes = martialaw(wither(w)(write))
        def nameget(name):
            return fmot(reads(name), write(name))
        
        def simple_fix(name, *argv, **kargv):
            return nameget(name)(*argv, **kargv)
        return simple_fix
    return simple_fixer_deco

every = lamp(lambda f, x : f(x), zip(map(martialaw, (lmap, map, map)), (lastnewline, py_compline, ignorlast)))

@simple_fixer
def subpr_compiler(fp):
    return every[0](every[1](every[2](fp.readlines())))

@subpr_compiler
def compile_subpr(fp, v):
    v.append('from subpr.lib import *\n')
    return fp.writelines(v)

def main(*argv, _a = _a):
    L = len(argv)
    if L - 1: compile_subpr(argv)
    elif L: main(None, input('WARN : no param\ninput argument : '))
    else: main(*_a)

if __name__ == "__main__" : main()