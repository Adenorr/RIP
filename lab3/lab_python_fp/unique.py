class Unique(object):
    # Итератор для удаления дубликатов

    def __init__(self, items, **kwargs):
            self.items = items   # массив или генератор
            self.used_elements = set()
            self.index = 0
            if(kwargs.get('ignore_case') == True):
                self.indicator = True
            else:
                self.indicator = False

    def __next__(self):
        while(True):
            if(type(self.items) is type(generator(5))):
                current = next(self.items)
            elif(type(self.items) == list):
                if self.index >= len(self.items):
                    raise StopIteration
                current = self.items[self.index]
                self.index = self.index + 1
            else:
                raise TypeError
            flag = False
#            if isinstance(current, str) and self.indicator:
#                for elem in self.used_elements:
#                    if current.upper() == elem.upper():
#                       flag = True
#                       break
#                    if not flag:
#                        self.used_elements.add(current)
#                        return current
#                if flag:
#                    self.__next__()

            if(type(current) == str and self.indicator):
                current = current.lower()
            if current not in self.used_elements:
                self.used_elements.add(current)
                return current

    def __iter__(self):
        return self


def generator(x):
    yield x

if __name__ == "__main__":
    from get_random import get_random
else:
    from lab_python_fp.get_random import get_random

def main():
   data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
   print(list(Unique(data)))
   data = get_random(10, 1, 3)
   print(list(Unique(data)))
   data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
   print(list(Unique(data)))
   print(list(Unique(data, ignore_case=True)))

if __name__ == "__main__":
    main()
