class person:
    def __init__(self, first, last, email):
        self.firstname = first
        self.lastname = last
        self.email = email

    def fullname(self):
        return self.firstname + " " + self.lastname

    def display(self):
        print("Full Name : " + self.firstname + " " + self.lastname)
        print("Email : " + self.email)


class customer(person):
    def __init__(self, custnum, first, last, email):
        super().__init__(first, last, email)
        self.customernum = custnum

    def display(self):
        super().display()
        print("Customer Num: " + str(self.customernum))


class employee(person):
    def __init__(self, pan, first, last, email):
        super().__init__(first, last, email)
        self.pannum = pan

    def display(self):
        super(employee, self).display()
        print("Pan Number : " + self.pannum)


if __name__ == '__main__':
    a = customer(123, "Varun", "Bogulla", "varunub1505@gmail.com")
    if isinstance(a, customer):
        a.display()
        print()

    b = employee("PYM123", "Rohit", "Bogulla", "rohitub222@gmail.com")

    if isinstance(b, employee):
        b.display()
        print()

    c = employee("GDFGD566", "Vaibhav", "P", "vaibhav@gmail.com")

    if isinstance(c,employee):
        c.display()
        print()
