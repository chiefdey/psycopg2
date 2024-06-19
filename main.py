from flask import Flask,render_template,redirect,request,url_for
from dbservice import getdata,insert_product,insert_sales
# create the flask instance
app=Flask(__name__)

# first route
@app.route('/')
def layout():
    return render_template('layout.html')

# routes connect url with the function
@app.route('/products')
def products():
    prods=getdata("products")
    return render_template('products.html',products=prods)
@app.route("/add_products",methods=['POST','GET'])
def addproducts():
    if request.method=="POST":
    # get form data using the name and request function inside flask
        pname=request.form['productname']
        buyingprice=request.form["B_P"]
        sellingprice=request.form["S_P"]
        stkquantity=request.form["STK"]
        newprod=(pname,buyingprice,sellingprice,stkquantity)
        insert_product(newprod)
    return redirect(url_for('products'))


@app.route('/sales')
def sales():
    sale=getdata("sales")
    products=getdata("products")
    return render_template('sales.html',sales=sale,products=products)
@app.route("/add_sales",methods=["POST","GET"])
def addsales():
    if request.method=="POST":
        prodid=request.form["prod_id"]
        quantity=request.form["quantity"]
        newsales=(prodid,quantity)
        insert_sales(newsales)
        # redirect you to the function of sales
    return redirect(url_for('sales'))




@app.route('/home')
def dashboard():
    return render_template('home.html')


app.run(debug=True)

