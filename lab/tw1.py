def enqueue(list):
    item = input("Enter item top be pushed: ")
    list.append(item)
    print("Item Pushed!",end="\n")
    disp(list)


def dequeue(list):
    if len(list) == 0:
        print("Queue empty!")
    list.pop()
    print("Item Popped!")
    disp(list)


def disp(list):
    print("The queue is: ")
    for x in list:
        print(x,end="\t")


def exit(list):
    while True:
        quit()


def main():
    list = []
    while True:
        menu = {"1": enqueue, "2": dequeue, "3": disp, "4": exit}
        print("\nOptions: \n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit")
        choice = input("enter your choice: ")
        menu[choice](list)


if __name__ == "__main__":
    main()
