import json
import sys
from lab_python_fp.print_result import print_result
from lab_python_fp.fieldd import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.print_result import test_1,test_2,test_3,test_4
from lab_python_fp.cm_timer import cm_timer_1
from contextlib import contextmanager



@print_result
def f1(arg):
    return sorted(list(Unique(list(field(arg, "job-name")), True)), key=lambda x: x.lower())


@print_result
def f2(arg):
    return list(filter(lambda x: x[:11].lower() == "программист", arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    zarplata = list(gen_random(len(arg), 100000, 200000))
    return ['{}, зарплата {} руб.'.format(proffesion, zarplata) for proffesion, zarplata in zip(arg, zarplata)]


