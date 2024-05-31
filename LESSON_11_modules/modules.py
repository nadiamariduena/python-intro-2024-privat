# different way of how to import modules
import math
import sys
import random
#
from enum import Enum

print(math.pi)
#result: 3.141592653589793
#

#
#--------
# another way
from math import pi
print(pi)
# result:   3.141592653589793

#
#--------
# another way

import random as rdm
print(dir(rdm))

# result

# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_fabs', '_floor', '_index', '_inst', '_isfinite', '_lgamma', '_log', '_log2', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

print('---------')
#
#--------
# another way
# make it more readable

for item in dir(rdm):
    print(item)
    # result
#     BPF
# LOG4
# NV_MAGICCONST
# RECIP_BPF
# Random
# SG_MAGICCONST
# SystemRandom
# TWOPI
# _ONE
# _Sequence
# __all__
# __builtins__
# __cached__
# __doc__
# __file__
# __loader__
# __name__
# __package__
# __spec__
# _accumulate
# _acos
# _bisect
# _ceil
# _cos
# _e
# _exp
# _fabs
# _floor
# _index
# _inst
# _isfinite
# _lgamma
# _log
# _log2
# _os
# _pi
# _random
# _repeat
# _sha512
# _sin
# _sqrt
# _test
# _test_generator
# _urandom
# _warn
# betavariate
# binomialvariate
# choice
# choices
# expovariate
# gammavariate
# gauss
# getrandbits
# getstate
# lognormvariate
# normalvariate
# paretovariate
# randbytes
# randint
# random
# randrange
# sample
# seed
# setstate
# shuffle
# triangular
# uniform
# vonmisesvariate
# weibullvariate

# check the purpose of the  modules
#https://docs.python.org/3/py-modindex.html