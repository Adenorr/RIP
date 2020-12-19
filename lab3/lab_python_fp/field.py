def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for dict in items:
            yield dict[args[0]]
    else:
        new_dict = {}
        for dict in items:
            for key in args:
                try:
                    new_dict[key] = dict[key]
                except KeyError:
                    continue
            yield new_dict
            new_dict.clear()

def main():
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
 ]
    print(goods)
    print("title: ")
    for i in field(goods, 'title'):
        print(i)
    print("title, price: ")
    for i in field(goods, 'title','price'):
        print(i)

if __name__ == "__main__":
    main()
