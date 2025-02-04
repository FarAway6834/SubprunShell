from subprocess import run as _r
from os import chdir as cd
from martialaw.martialaw import *


s = shell = partial(_r, shell = True)
cmds = {
    "exit" : exit,
    "cd" : cd,
    "shell" : shell
}

compv = lambda f, *argv : (f, argv)
isexit = lambda v : v == 'exit'
iscd = lambda v : v[:3] == 'cd '
exitv = lambda v : compv(v)
cdvc = lambda v : ('cd', v[3:])
shellvc = lambda v : ('shell', v)
cmpl_elsesc = lambda v : cdvc(v) if iscd(v) else shellvc(v)
cmpl_elses = lambda v : compv(*cmpl_elsesc(v))
compline = lambda v : exitv(v) if isexit(v) else cmpl_elses(v)

pysrcv = lambda f, argv : f'{f}{argv}'
py_compline = lambda v : pysrcv(*compline(v))

ignorlast = lambda x : x[:-1]
lastnewline = lambda x : f'{x}\n'
lamp = lmap = lambda f, i : list(map(f, i))

runlinec = lambda f, argv : lambda : cmds[f](*argv)
subpr = runlinef = lambda v : runlinec(*compline(v))