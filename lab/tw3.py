import csv
from tabulate import tabulate as t

header = ['bookNo', 'title', 'Author', 'Price']


class NoBooks(Exception):
    pass


def insert():
    file = open("sample.csv", "a", newline="\n")
    file_writter = csv.writer(file)
    temp = []
    a = int(input("Enter the BookNumber\n"))
    temp.append(a)
    b = input("Enter the Title\n")
    temp.append(b)
    c = input("Enter the Author\n")
    temp.append(c)
    d = int(input("Enter the Price\n"))
    temp.append(d)
    file_writter.writerow(temp)
    file.close()


def search(name):
    data = []
    file = open("sample.csv", "r")
    file_reader = csv.reader(file)
    for i in file_reader:
        if name in i[2]:
            data.append(i)
    if data:
        print(t(data, header))
        data.clear()
    else:
        print("No Book Found")
    file.close()


def searchPrice(a):
    data1 = []
    file = open("sample.csv", "r")
    file_reader = csv.reader(file)
    try:
        if a <= 0:
            raise NoBooks("No Records For Free")
        else:
            for i in file_reader:
                if a >= int(i[3]):
                    data1.append(i)
            if data1:
                print(t(data1, header))
                data1.clear()
            else:
                print("No record")
    except NoBooks as v:
        print(v)

    file.close()


def searchTitle():
    name0 = input("Enter the Title :")
    data2 = []
    file = open("sample.csv", "r")
    file_reader = csv.reader(file)
    for i in file_reader:
        if i[1].__contains__(name0):
            data2.append(i)
    if data2:
        print(t(data2, header))
        data2.clear()
    else:
        print("No Record")
    file.close()


if __name__ == '__main__':
    while True:
        print("Enter\n1:Insert Book\n2:Search Book By Author\n3:Search Book by Price\n4:Search by Title\n5:exit")
        a = int(input())
        if a == 1:
            insert()
            print()
        elif a == 2:
            name = input("Enter the AutHor Name: ")
            search(name)

        elif a == 3:
            price = int(input("Enter the Price : "))
            searchPrice(price)
        elif a == 4:

            searchTitle()
        else:
            exit(0)