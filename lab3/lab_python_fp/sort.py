

def sort(arg):
    result = sorted(arg, key=abs, reverse=True)
    return result

def sort_with_lambda(arg):
    result_with_lambda = sorted(arg, key=lambda x: abs(x), reverse=True)
    return result_with_lambda

def main():
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    print("Исходный: {}".format(data))
    print(sort(data))
    print(sort_with_lambda(data))

if __name__ == '__main__':
    main()
