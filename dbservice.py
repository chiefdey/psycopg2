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

# write a function to fetch products
# def get_products():
#     pquery='select * from products;'
#     cur.execute(pquery)
#     products=cur.fetchall()
#     print(products)
# get_products()

# # fetch sales
# def getsales():
#     squery='select * from sales;'
#     cur.execute(squery)
#     sales=cur.fetchall()
#     print(sales)
# getsales()
# create one function to fetch all data from db
def getdata(a):
    query=f"select * from {a}"
    cur.execute(query)
    tables=cur.fetchall()
    print(tables)
x=getdata("products,sales")
print(x)
