'''
设计一个有getMin功能的栈
实现一个特色的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作
'''
class MyStack1:
    """
    关键处理步骤：
    当push一条数据时，如果stack_min当前栈顶数据>=要push的数据，则向stack_min中push该数据
    当pop一条数据时，如果stack_min当前栈顶数据==要pop的数据，则stack_min同时pop该数据
    """
    def __init__(self):
        self.stack_data = []
        self.stack_min = []

    def push(self, data):
        self.stack_data.append(data)
        if not self.stack_min:
            self.stack_min.append(data)
            return
        curr_min_data = self.stack_min[-1]
        if curr_min_data >= data:
            self.stack_min.append(data)

    def pop(self):
        if not self.stack_data:
            raise Exception("No data")
        data = self.stack_data.pop()
        curr_min_data = self.stack_min[-1]
        if data == curr_min_data:
            self.stack_min.pop()
        return data


    def getMin(self):
        if not self.stack_min:
            raise Exception("No data")
        return self.stack_min[-1]


class MyStack2:
    """
    关键处理步骤：
    当push一条数据时，如果stack_min当前栈顶数据>=要push的数据，则向stack_min中push该数据，否则再次push当前栈顶数据
    """
    def __init__(self):
        self.stack_data = []
        self.stack_min = []

    def push(self, data):
        self.stack_data.append(data)
        if not self.stack_min:
            self.stack_min.append(data)
            return
        curr_min_data = self.stack_min[-1]
        if curr_min_data > data:
            self.stack_min.append(data)
        else:
            self.stack_min.append(curr_min_data)

    def pop(self):
        if not self.stack_data:
            raise Exception("No data")
        data = self.stack_data.pop()
        self.stack_min.pop()
        return data

    def getMin(self):
        if not self.stack_min:
            raise Exception("No data")
        return self.stack_min[-1]


if __name__ == '__main__':
    pass