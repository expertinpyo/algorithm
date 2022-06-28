# Stack, adt -> 실제 코드로 작성하는 것
class Stack:
    # 생성자, 인스턴스가 생성될 때 자동으로 호출
    # 초기화 시켜준다.
    def __init__(self, size):   # self => 인스턴스 자신
        self.items = []         # 요소를 담을 배열
        self.size = size        # 넘겨받는다. 만들 배열의 크기
        self.top = -1           # python에서는 음수 인덱싱을 지원하지만 C와 같은 언어에서는 지원 X. 따라서 어떤 요소의 초깃값을 표현할 때 많이 사용

    def is_empty(self):
        return True if not len(self.items) else False

    def is_full(self):
        return True if len(self.items) == self.size else False

    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full.")
        else:
            # append를 활용해서 추가
            self.items.append(item)
            self.top += 1

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.items[self.top]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            value = self.items[self.top]
            self.items = self.items[:self.top]
            self.top -= 1
            return value

    def __str__(self):
        result = '\n-----'
        for d in self.items:
            result = f'\n| {d} |' + result
        for _ in range(self.size - len(self.items)):
            result = f'\n|   |' + result
        return result
