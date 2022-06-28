"""
문제2. 기본 Queue 구현 - 클래스 구현 (가변)
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력)
"""


class Queue:
    def __init__(self):
        """
        인스턴스 생성 시에 새로운 Queue 생성
        """
        self.queue = []
        self.front = -1
        self.rear = -1

    def is_empty(self):
        """
        Queue에 비어있는지 여부를 True / False로 반환
        """
        return True if self.front == self.rear else False

    def enqueue(self, num):
        """
        Queue에 원소 삽입
        """
        self.queue.append(num)
        self.rear += 1

    def dequeue(self):
        """
        Queue에서 원소 삭제 후 반환
        """
        self.front += 1
        return self.queue.pop(0)

    def size(self):
        """
        Queue의 길이 반환
        """
        return len(self.queue)


a = Queue()
num_list = [1, 2, 3]
print(a.is_empty())
for i in num_list:
    a.enqueue(i)
print(a.queue, a.size(), a.is_empty())
if not a.is_empty():
    q = a.dequeue()
    print(q, a.size())

# 1. Queue 인스턴스 생성

# 2. Queue가 비었는지 확인

# 3. 1, 2, 3 원소를 Queue 삽입

# 4. 원소가 정상적으로 삽입되었는지 확인 / 사이즈 확인 / 비었는지 여부 확인

# 5. Queue에서 원소 삭제 후 반환 & 원소 확인 / 사이즈 확인