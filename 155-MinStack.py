class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack_index = []
        self.stack_index_top = 0
        self.min_stack_index_top = 0
        self.min_value = 2**31 - 1  # max value int
        self.min_value_index = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.min_value >= val:
            self.min_value = val
            self.min_value_index = self.stack_index_top
            self.min_stack_index.append(self.stack_index_top)
            self.min_stack_index_top = self.min_stack_index_top + 1

        self.stack.append(val)
        self.stack_index_top = self.stack_index_top + 1

    def pop(self):
        """
        :rtype: None
        """
        self.top_ = self.top()
        self.min_ = self.getMin()

        if self.top_ == self.min_:
            self.min_stack_index_top = self.min_stack_index_top - 1
            self.min_stack_index.pop()
            self.min_value = self.getMin()

        self.stack_index_top = self.stack_index_top - 1
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return 2**31 - 1

        return self.stack[self.stack_index_top - 1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_stack_index) == 0:
            return 2**31 - 1

        return self.stack[self.min_stack_index[self.min_stack_index_top - 1]]


# stack = [2, 3, 1, 4, 5, 0]
# min_stack_index = [0, 2, 5]


[
    "MinStack",
    "push",
    "getMin",
    "top",
    "getMin",
    "push",
    "push",
    "getMin",
    "push",
    "getMin",
    "pop",
    "push",
    "push",
    "getMin",
    "push",
]

[
    [],
    [395],
    [],
    [],
    [],
    [276],
    [29],
    [],
    [-482],
    [],
    [],
    [-108],
    [-251],
    [],
    [-439],
    [],
    [370],
]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(val=395)
param_1 = obj.getMin()
top_1 = obj.top()
param_1 = obj.getMin()
obj.push(val=276)
obj.push(val=29)
param_2 = obj.getMin()
obj.push(val=-482)
param_3 = obj.getMin()
obj.pop()
obj.push(val=-108)
obj.push(val=-251)
param_4 = obj.getMin()
obj.push(val=-439)
print("end")

# param_3 = obj.top()
# param_4 = obj.getMin()
# print(param_3)
# print(param_4)
