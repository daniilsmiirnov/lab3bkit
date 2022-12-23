from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.print_result import test_1,test_2,test_3,test_4
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.fieldd import field
from lab_python_fp.process_data import f1,f2,f3,f4
from contextlib import contextmanager
import json
import time



def main():
    print("1.Field:")
    goods = [
            {'title': 'Ковер', 'price': 2000, 'color': 'green'},
            {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}]


    print(*field(goods, 'title'))
    print(*field(goods, 'title', 'price'))


    print("2.Gen_Random:", *gen_random(10, 2, 100))

    print("3.Unique:")
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data1 = ["a", "A", "b", "B", "a", "A", "b", "B"]
    data3 = gen_random(10, 1, 4)
    print(*Unique(data))
    print(*Unique(data1))
    print(*Unique(data1, True))
    print(*Unique(data3))

    print("4.Sort:")
    data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
    result = sorted(data, key=abs, reverse=True)

    result_with_lambda = sorted(data,key = lambda a: a if a > 0 else -a, reverse=True)

    print(result)
    print(result_with_lambda)

    print("5.Print_result:")
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()

    #print("6.Cm_timer:")
    #with cm_timer_1():
     #   time.sleep(5.5)

    #print("7.process_data:")
    path = 'data_light2.json'

    path2 = 'data_light.json'
    with open(path2, encoding="utf-8") as f:
        data_j = json.load(f)

    #F1=f1(data_j)
    #f3(f2(f1(data_j)))
    with cm_timer_1():
        f4(f3(f2(f1(data_j))))



if __name__ == '__main__':
    main()
