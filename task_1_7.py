class DequeClass:
    def __init__(self):
        self.elem = []

    def add_to_rear(self, item):
        self.elem.insert(0, item)


def pal_check(string):
    dc_obj = DequeClass()

    for i in string.replace(' ', ''):
        dc_obj.add_to_rear(i)

    if dc_obj.elem == list(reversed(dc_obj.elem)):
        return True
    else:
        return False

print(pal_check('а роза упала на лапу азора'))