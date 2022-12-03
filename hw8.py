import sqlite3
from sqlite3 import Error
def create_table(conn, sql_to_create_table):
    try:
        c = conn.cursor()
        c.execute(sql_to_create_table)
        return conn
    except Error as e:
        print(e)
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn
def create_product(conn, product):
    sql = '''INSERT INTO product (product_name, product_title, price, quantity) 
        VALUES (?, ?, ?, ?)'''
    try:
        c = conn.cursor()
        c.execute(sql, product)
        conn.commit()
        return c.lastrowid
    except Error as e:
        print(e)
    return None

def update_quantity(conn, product):
    sql = '''UPDATE product SET quantity = ? WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)



def update_price(conn, product):
    sql = '''UPDATE product SET price = ? WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)

def select_all_products(conn,rows):
    sql = '''SELECT * FROM product'''
    try:
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()

        for r in rows:
            print(r)
    except Error as e:
        print(e)

def select_product_val(conn, limit_for_price,limit_for_quantity):
    sql = '''SELECT * FROM product WHERE price <= ? and quantity <= ?'''
    try:
        c = conn.cursor()
        c.execute(sql, (limit_for_price,limit_for_quantity))
        rows = c.fetchall()

        for r in rows:
            print(r)
    except Error as e:
        print(e)


def search_product(conn,product_name):
    sql = '''SELECT * FROM product WHERE product_name like ?'''
    try:
        c = conn.cursor()
        c.execute(sql, [product_name])
        rows = c.fetchall()

        for r in rows:
            print(r)
    except Error as e:
        print(e)




def delete_product(conn, id):
    sql = '''DELETE FROM product WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)


database = r'hw.db'
conn = create_connection(database)
sql_create_table_product = '''
CREATE TABLE product(
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_name VARCHAR (200) NOT NULL,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (8, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
)
'''
# delete_product(conn, 17)
# update_quantity(conn,(3,15))
# update_price(conn,(60,15))
# select_all_products(conn, database)
# select_product_val(conn,100,5)
# search_product(conn,'%Мыло%')
if conn is not None:
    print('Connected Successfully')
    # create_table(conn, sql_create_table_product)
    # create_product(conn, ("Aple", "fruits", 80.5, 20))
    # create_product(conn, ("cola", "drink", 60, 9))
    # create_product(conn, ("Banana", "fruits", 25.8, 50))
    # create_product(conn, ("Cake", "sweets", 80.5, 20))
    # create_product(conn, ("Orange", "fruits", 80.5, 20))
    # create_product(conn, ("Cake", "sweets", 80.5, 20))
    # create_product(conn, ("Orange", "fruits", 80.5, 20))
    # create_product(conn, ("milk", "drink", 55.5, 10))
    # create_product(conn, ("egg", "fruits", 80.5, 20))
    # create_product(conn, ("Gammy", "soft_toys", 3000.5, 40))
    # create_product(conn, ("NITRO", "Energy drink", 80.5, 50))
    # create_product(conn, ("Fanta", "drink", 45.5, 30))
    # create_product(conn, ("Мыло", "Средства", 80.5, 80))
    # create_product(conn, ("Макасины", "Обувь", 2000, 20))
    # create_product(conn, ("mi", "phone", 8000, 20))
    # create_product(conn,('Мыло_жидкое','Средства',25,15))
    # create_product(conn, ('Мыло_ванильное', 'Средства', 45, 15))