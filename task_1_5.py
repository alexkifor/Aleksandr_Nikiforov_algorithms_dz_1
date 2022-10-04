class PlateStack:
    def __init__(self, max_size):
        self.elem = [[]]
        self.max_size = max_size

    def __str__(self):
        return str(self.elem)

    def push_in(self, el):
        if len(self.elem[len(self.elem)-1]) < self.max_size:
            self.elem[len(self.elem) - 1].append(el)
        else:
            self.elem.append([])
            self.elem[len(self.elem) - 1].append(el)

    def pop_out(self):
        result = None
        if len(self.elem) == 1:
            if len(self.elem[0]) == 0:
                result = [[]]
            else:
                result = self.elem[0].pop()
        if len(self.elem) > 1:
            result = self.elem[len(self.elem) - 1].pop()
            if len(self.elem[len(self.elem) - 1]) == 0:
                self.elem.remove([])
        return result

    def max(self):
        result = []
        for i in self.elem:
            for j in i:
                result.append(j)
        if len(result) == 0:
            return None
        return max(result)

    def get_val(self):
        if len(self.elem) == 0:
            return None
        return self.elem[len(self.elem) - 1]

    def is_empty(self):
        return self.elem == [[]]

    def stack_size(self):
        elem_sum = 0
        for stack in self.elem:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        return len(self.elem)


stack_1 = PlateStack(3)
for i in range(1, 8):
    stack_1.push_in(i)

stack_1.pop_out()
stack_1.pop_out()


print(stack_1.elem)
print(stack_1.max())
print(stack_1.get_val())
print(stack_1.is_empty())
print(stack_1.stack_size())
print(stack_1.stack_count())
