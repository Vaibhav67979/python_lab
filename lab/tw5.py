import sqlite3


class ProductsClass:
    def __init__(self, dbName):
        self.dbName = dbName

    def dbCreate(self, conn):
        cursorObj = conn.cursor()
        cursorObj.execute(
            'CREATE TABLE if not exists Products(prodID INTEGER, name TEXT,qty INTEGER,price INTEGER,PRIMARY KEY(prodID))')

    def dbInsert(self, conn):
        n = int(input("Enter no. of records:"))
        for i in range(n):
            prodID = int(input("Enter prodID: "))
            name = input("Enter name: ")
            qty = int(input("Enter quantity: "))
            price = int(input("Enter price: "))
            entities = (prodID, name, qty, price)
            cursorObj = conn.cursor()
            cursorObj.execute('INSERT INTO Products(prodID,name,qty,price) values (?,?,?,?)', entities)
            conn.commit()

    def dbDisplayALL(self, conn):
        cursorObj = conn.cursor()
        cursorObj.execute("Select * from Products")
        rs = cursorObj.fetchall()
        for row in rs:
            for col in row:
                print(f"{col} ", end="")
            print()

    def dbDelete(self, conn):
        prodID = int(input("Enter the product ID to be deleted: "))
        cursorObj = conn.cursor()
        sqlstr = f"DELETE from Products where prodID= {prodID} "
        cursorObj.execute(sqlstr)
        conn.commit()

    def dbUpdate(self, conn):
        cursorObj = conn.cursor()
        cursorObj.execute('UPDATE Products SET price=price+price * 0.1 where price<5000')
        conn.commit()

    def dbDispProd(self, conn):
        cursorObj = conn.cursor()
        cursorObj.execute("SELECT * from Products where qty < 40")
        rs = cursorObj.fetchall()
        for row in rs:
            for col in row:
                print(f"{col} ", end="")
            print()


try:
    dbc = ProductsClass("Products.sqlite")
    conn = sqlite3.connect(dbc.dbName)
    conn.row_factory = sqlite3.Row
    dbc.dbCreate(conn)
    dbc.dbInsert(conn)
    dbc.dbUpdate(conn)
    dbc.dbDisplayALL(conn)
    dbc.dbDelete(conn)
    dbc.dbDispProd(conn)

except sqlite3.Error as err:
    print(f"DB Error: {err}")
finally:
    conn.commit()
    conn.close()
