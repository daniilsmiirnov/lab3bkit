class Unique(object):
    def __init__(self, items, ignore_case=False, **kwargs):

        self.items = items
        self.case = ignore_case
        self.kwargs = kwargs
        self.MySet = set()

        pass

    def __next__(self):
        iterator = iter(self.items)
        while(True):
            try:
                obj = next(iterator)
            except StopIteration:
                raise
            # else:
            #     if obj not in self.MySet and self.case==False:
            #         self.MySet.add(obj)
            #         return obj
            #     elif self.case==True:
            #         a = str(obj)
            #         if a.lower() not in self.MySet:
            #             self.MySet.add(a)
            #             return a

            else:
                if self.case == True and isinstance(obj, str):
                    a = str(obj)
                    if a.lower() not in self.MySet:
                        self.MySet.add(a.lower())
                        return obj
                elif obj not in self.MySet:
                    self.MySet.add(obj)
                    return obj
    def __iter__(self):
        return self