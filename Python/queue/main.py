queue = [0, 0, 0, 0, 0]
front = rear = -1

def enqueue(elm):
    global front, rear
    if rear == -1:
        front = rear = 0
        queue[rear] = elm

    elif rear == 4:
        print("queue is full")
        exit()

    else:
        rear += 1
        queue[rear] = elm

def dequeue():
    global rear, front

    if front == -1:
        print("queue is empty")
        exit()

    elm = queue[front]

    if front == rear:
        front = rear = -1

    else:
        front += 1 

    return elm

enqueue(10)
enqueue(20)
enqueue(30)
print(dequeue())
print(dequeue())
print(dequeue())
