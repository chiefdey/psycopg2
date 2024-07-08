import psycopg2
# connect to database
conn=psycopg2.connect(
    dbname="myduka",
    user="postgres",
    host="localhost",
    port=5432,
    password="4321"
)
# cursor to perform database operation
cur=conn.cursor()

# # write a function to fetch products
# def get_products():
#     pquery='select * from products;'
#     cur.execute(pquery)
#     products=cur.fetchall()
#     print(products)
# get_products()

# # # fetch sales
# def getsales():
#     squery='select * from sales;'
#     cur.execute(squery)
#     sales=cur.fetchall()
#     print(sales)
# getsales()
# # create one function to fetch all data from db
def getdata(a):
    query=f"select * from {a}"
    cur.execute(query)
    tables=cur.fetchall()
    return(tables)
getdata("products")
# getdata('sales')

# inserting into db
# def  insert_sales():
#     query="insert into sales(productid,quantity,created_at) values(50,10,now())"
#     cur.execute(query)
#     conn.commit()
# insert_sales()
# getdata("sales")

# def insert_products():
#     query="insert into products(name,buying_price,selling_price,stock_quantity) values('pombe',1000,1200,139)"
#     cur.execute(query)
#     conn.commit()
# insert_products()
# getdata('products')

# def insert_products(a,b,c,d):
#     query=f"insert into products(name,buying_price,selling_price,stock_quantity) values('{a}',{b},{c},{d})"
#     cur.execute(query)
#     conn.commit()
# insert_products("food",100,130,50)
# getdata('products')

# using one parameter and placeholders
def insert_product(values):
    query="insert into products(name,buying_price,selling_price,stock_quantity) values(%s,%s,%s,%s)"
    cur.execute(query,values)
    conn.commit()
x=("biscuits",100,150,55)
insert_product(x)


def insert_sales(values):
    query="insert into sales(productid,quantity,created_at) values(%s,%s,now())"
    cur.execute(query,values)
    conn.commit()
y=(31,109)
insert_sales(y)
getdata("sales")

# SALES PER PRODUCT
def sales_prod():
    query="SELECT products.name ,SUM(sales.quantity * products.selling_price) from products \
        INNER JOIN sales on (products.id=sales.productid) GROUP BY products.name ORDER BY SUM DESC;"
    cur.execute(query)
    s_p=cur.fetchall()
    return s_p
sales_prod()

# # PROFIT PER PRODUCT
def profit():
    query=" SELECT SUM(sales.quantity * (products.selling_price-products.buying_price)),products.name from products \
        INNER JOIN sales on (products.id=sales.productid) GROUP BY products.name ORDER BY SUM DESC;"
    cur.execute(query)
    pr=cur.fetchall()
    return pr
profit()
# # SALES PER DAY
def daysales():
    query="Select SUM(sales.quantity * products.selling_price),date(sales.created_at) from products\
          INNER JOIN sales on (products.id=sales.productid) GROUP BY date(sales.created_at) ORDER BY SUM DESC;"
    cur.execute(query)
    day=cur.fetchall()
    return day
daysales()

# PROFIT PER DAY
def dayprofit():
    query="Select SUM(sales.quantity * (products.selling_price-products.buying_price)),date(sales.created_at) from products\
          INNER JOIN sales on (products.id=sales.productid) GROUP BY date(sales.created_at) ORDER BY date(sales.created_at);"
    cur.execute(query)
    day=cur.fetchall()
    return day
dayprofit()
# display total sales 
def totalsales():
    query="Select SUM(sales.quantity * products.selling_price) from products  INNER JOIN sales on (products.id=sales.productid);"
    cur.execute(query)
    ts=cur.fetchall()
    return ts
totalsales()
# display todays sales
def todaysales():
    query="Select SUM(sales.quantity * products.selling_price),date(sales.created_at) AS salesday from products INNER JOIN sales on (products.id=sales.productid) GROUP BY salesday ORDER BY salesday DESC LIMIT 1;"
    cur.execute(query)
    t_s=cur.fetchall()
    return t_s
todaysales()
# display total profit
def totalprofit():
    query="Select SUM(sales.quantity * (products.selling_price-products.buying_price)) from products\
          INNER JOIN sales on (products.id=sales.productid);"
    cur.execute(query)
    ttl=cur.fetchall()
    return ttl
totalprofit()
# display todays profit
def todayprofit():
    query="Select SUM(sales.quantity * products.selling_price-products.buying_price),date(sales.created_at) AS salesday from products\
          INNER JOIN sales on (products.id=sales.productid) GROUP BY salesday ORDER BY salesday DESC LIMIT 1;"
    cur.execute(query)
    t_p=cur.fetchall()
    return t_p
todayprofit()
# display recent sales
def recent():
    query="Select SUM(sales.quantity * products.selling_price-products.buying_price),date(sales.created_at) AS salesday from products\
          INNER JOIN sales on (products.id=sales.productid) GROUP BY salesday ORDER BY salesday DESC LIMIT 10;"
    cur.execute(query)
    r_s=cur.fetchall()
    return r_s
recent()
# insert users
def insert_users(values):
    query="insert into users(first_name,last_name,email,password) values(%s,%s,%s,%s);"
    cur.execute(query,values)
    conn.commit()

def verify(email):
    query = "select * from users WHERE email=(%s);"
    cur.execute(query,(email,))
    user=cur.fetchall()
    return user
def check_ep(e,p):
    query="select * from users WHERE email=(%s) and password=(%s)"
    cur.execute(query,(e,p,))
    data=cur.fetchall()
    return data


