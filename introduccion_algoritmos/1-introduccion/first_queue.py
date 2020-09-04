"""
Creating the first queue. Not working right now, need to fix...
"""
SIZE = 5
REAR = -1
FRONT = -1
VALUES = []


def enQueue(value):
    global FRONT
    global REAR
    if REAR == SIZE - 1:
        print('Our Queue is full. \n')
    else:
        if FRONT:
            FRONT = 0
        REAR += 1
        value = VALUES.append([REAR])
        print(f'Value {value} inserted. \n')


def deQueue():
    global FRONT
    global REAR
    if FRONT:
        print('Our Queue is empty.')
    else:
        print(f'Value {VALUES[FRONT]} removed')
        FRONT += 1
        if FRONT > REAR:
            FRONT = REAR = -1


if __name__ == "__main__":
    
    deQueue()
    enQueue(4)
