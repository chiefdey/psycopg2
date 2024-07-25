from flask import Flask,render_template,redirect,request,url_for,flash,session
from dbservice import getdata,insert_product,insert_sales,sales_prod,profit,daysales,dayprofit,recent,insert_users,verify,check_ep
# create the flask instance
app=Flask(__name__)
app.secret_key="muriithi"
# first route
@app.route('/')
def layout():
    emils=None
    if 'email' in session:
        emils=session['email']

    return render_template('layout.html',emils=emils)

# routes connect url with the function
@app.route('/products')
def products():
    if "email" in session:
        prods=getdata("products")
    else:
        flash("log in to access this page","error")
        return redirect(url_for("login"))
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
    if "email" in session:
        sale=getdata("sales")
        products=getdata("products")
    else:
        flash("login to access this page","error")
        return redirect(url_for("login"))
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
    if "email" in session:
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
        # recent sales
        recents=recent()
        return render_template('home.html',pname=pname,psales=psales,prof=prof,dys=dys,s_d=s_d,pd=pd,recents=recents)
    else:
        flash("Login to access this page","error")
        return redirect(url_for("login"))


@app.route('/register', methods=['POST',"GET"])
def register():
    if request.method=="POST":
        fname=request.form['first_name']
        lname=request.form['last_name']
        email=request.form['email']
        pword=request.form['password']
        user=(fname,lname,email,pword)
        verification=verify(email)
        # print(verification)
        if len(verification) == 0:
            insert_users(user)
            flash("registration successful login to continue:","success")
            return redirect(url_for("login"))
        else:
            flash("user already exist","error")
            return redirect(url_for("register"))
    return render_template('register.html')
@app.route('/login',methods=["POST","GET"])
def login():
    if request.method=="POST":
        eml=request.form["email"]
        psw=request.form["password"]
        emails=verify(eml)
        if len(emails)==1:
            check=check_ep(eml,psw)
            if len(check)==1:
                session['email']=eml
                flash("login successful","success")
                return redirect(url_for("dashboard"))
            else:
                flash("wrong email and password","error")
                # return redirect(url_for(""))
        else:
            flash("email does not exist","error")
            return redirect(url_for("register"))

    return render_template("login.html")
@app.route("/logout")
def logout():
    session.pop("email",None)
    flash("logged out successfully","success")
    return redirect(url_for("login"))




app.run(debug=True)

