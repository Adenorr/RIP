import sys
import math
import getopt

def discr(a, b, c):
    return b**2 - 4*a*c

def calc_root(a, b, c, d):
    return (-b + d)/2*a

def calc_roots(a, b, c):
    d = discr(a, b, c)
    if d < 0:
        return []
    elif d == 0:
        return [calc_root(a, b, c, d)]
    else:
        d = math.sqrt(d)
        return [calc_root(a, b, c, d), calc_root(a, b, c, -d)]

def bi_root(root):
    if root < 0:
        return []
    elif root == 0:
        return [root]
    else:
        return [math.sqrt(root), -math.sqrt(root)]

def solution(a, b, c):
    answer = []
    if a == b == c == 0:
        print("Решений бесконечно много")
    elif a == b == 0:
        pass
    elif a == 0:
        a, b = b, 0
        answer = calc_roots(a, b, c)
    else:
        roots = calc_roots(a, b, c)
        for root in roots:
            answer = answer + bi_root(root)
    return answer

def input_args():
    args = []
    for i in range(3):
        args.append(input('{} = '.format(chr(ord('A')+i))))
    return args

def parse_args(argv):
    params = []
    for arg in argv:
        try:
            params.append(float(arg))
        except ValueError:
            print('Параметры не удаётся привести к типу float')
            return None
    return params

def main():
    print('Aletvans IU5-44')
    argv = sys.argv[1:]
    if len(argv) != 3:
        print('Нужно ввести три параметра')
        argv = input_args()

    while True:
        params = parse_args(argv)
        if params != []:
            break
        argv = input_args()

    answer = solution(params[0], params[1], params[2])
    if answer == []:
        if not (params[0] == params[1] == params[2]):
            print("Действительных корней нет")
    else:
        print(answer)
#    argv = sys.argv[1:]
#    try:
#    options, args = getopt.getopt(argv, "a:b:c")
#    except:
#        print("Ошибка в аргументах командной строки ")
#    if options:
#        for name, value in options:
#            if name in ['-a']:
#                a = value
#            elif name in ['-b']:
#                b = value
#            elif name in ['-c']:
#                c = value

if __name__ == "__main__":
    main()
