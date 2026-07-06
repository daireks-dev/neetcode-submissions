class MinStack:

    def __init__(self):
        self.Stack = []
        self.MinStack = []
        self.MinElement = float("inf")

    def push(self, val: int) -> None:
        self.Stack.append(val)
        self.MinElement = min(self.MinElement, val)
        self.MinStack.append(self.MinElement)

    def pop(self) -> None:
        self.Stack.pop()
        self.MinStack.pop()
        
        if len(self.MinStack) == 0:
            self.MinElement = float("inf")
        else:
            self.MinElement = self.MinStack[len(self.MinStack)-1]

    def top(self) -> int:
        return self.Stack[len(self.Stack)-1]

    def getMin(self) -> int:
        return self.MinElement
        
