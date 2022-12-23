def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for i in items:
            yield i.get(args[0])
    else:
        for i in items:
            d = {}
            for a in args:
                if i.get(a) is not None:
                    d[a] = i.get(a)
            yield d


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]




