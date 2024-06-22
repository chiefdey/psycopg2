from flask import Flask,render_template,redirect,request,url_for
from dbservice import getdata,insert_product,insert_sales,sales_prod,profit,daysales,dayprofit
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
    s_p=sales_prod()
    pname=[]
    psales=[]
    for i in s_p:
        pname.append(i[0])
        psales.append(float(i[1]))
    # profit per product
    pp=profit()
    prof=[]
    for i in pp:
        prof.append(i[0])
    # sales per day
    d_s=daysales()
    dys=[]
    s_d=[]
    for i in d_s:
        dys.append(str(i[1]))
        s_d.append(i[0])
# profit per day
    d_p=dayprofit()
    pd=[]
    for i in d_p:
        pd.append(i[0])
    return render_template('home.html',pname=pname,psales=psales,prof=prof,dys=dys,s_d=s_d,pd=pd)


app.run(debug=True)

