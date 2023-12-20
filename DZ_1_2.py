from queue import Queue
from random import randint


class Request:
    counter = 0

    # field 'value' was added in case we will need to store information and process request somehow later
    def __init__(self, value):
        Request.counter += 1
        self.count = Request.counter
        self.value = value


def generate_request(queue):
    request = Request(None)
    queue.put(request)
    print(f"Request # {request.count} is genarated")


def process_request(queue):
    if queue.empty():
        print("Queue is empty")
    else:
        request = queue.get()
        print(f"Request # {request.count} is completed")


q = Queue()

while True:
    user_input = input("if you want to leave the program press 'y', else press any key\n")
    if user_input in ["Y", "y"]:
        print("Good buy")
        break
    else:
        choice = randint(0,1)
        if choice:
            generate_request(q)
        else:
            process_request(q)
