from flask import Flask, render_template, request, redirect
import mysql.connector
from datetime import datetime

now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mizanshk@92",
  database="boutique"
)
mycursor = mydb.cursor()

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/index")
def index_1():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/products")
def products():
    return render_template("products.html")
@app.route("/products2")
def products2():
    return render_template("products2.html")
@app.route("/singleproducts")
def singleproducts():
    return render_template("singleproducts.html")
@app.route("/women01")
def women01():
    return render_template("women01.html")
@app.route("/women02")
def women02():
    return render_template("women02.html")
@app.route("/women03")
def women03():
    return render_template("women03.html")
@app.route("/women04")
def women04():
    return render_template("women04.html")
@app.route("/women05")
def women05():
    return render_template("women05.html")
@app.route("/women06")
def women06():
    return render_template("women06.html")
@app.route("/women07")
def women07():
    return render_template("women07.html")
@app.route("/women08")
def women08():
    return render_template("women08.html")
@app.route("/women09")
def women09():
    return render_template("women09.html")
@app.route("/women")
def women10():
    return render_template("women10.html")
@app.route("/women11")
def women11():
    return render_template("women11.html")

@app.route("/pop_up")
def pop_up():
    return render_template("pop_up.html")

@app.route("/login_option")
def login_option():
    return render_template("login_option.html")
@app.route("/sizechart")
def sizechart():
    return render_template("sizechart.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        sql = "INSERT INTO contact(name, email, message) VALUES (%s, %s, %s)"
        val = (name, email, message)
        mycursor.execute(sql, val)
        mydb.commit()
        if mycursor.rowcount == 1:
            return render_template('contact.html')
        
    return render_template('contact.html')

@app.route("/admin_register", methods=["POST", "GET"])
def admin_register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        sql = "INSERT INTO admin_detail (username, email, password) VALUES (%s, %s, %s)"
        val = (username, email, password)
        mycursor.execute(sql, val)
        mydb.commit()
        if mycursor.rowcount == 1:
           return render_template("admin_login.html") 

    return render_template("admin_register.html")

@app.route("/admin_login", methods=["POST", "GET"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        sql = "select * from admin_detail where username=%s and password=%s"
        val = (username, password)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        print(mycursor.rowcount)
        if int(mycursor.rowcount) == 1:
           return redirect("admin_dashboard") 
        
    return render_template("admin_login.html")

@app.route("/admin_dashboard", methods=["POST", "GET"])
def admin_dashboard():
    mycursor.execute("SELECT id, username, email FROM admin_detail")
    myresult = mycursor.fetchall()
    print(list(myresult))
    return render_template("admin_dashboard.html", myresult=list(myresult))

@app.route("/admin_view_user", methods=["POST", "GET"])
def admin_view_user():
    mycursor.execute("SELECT id, username, email FROM user_detail")
    myresult = mycursor.fetchall()
    print(list(myresult))
    return render_template("admin_view_user.html", myresult=list(myresult))

@app.route("/admin_order_detail", methods=["POST", "GET"])
def admin_order_detail():
    mycursor.execute("SELECT id, username, category, fabric, measurement FROM user_order")
    myresult = mycursor.fetchall()
    print(list(myresult))
    return render_template("admin_order_detail.html", myresult=list(myresult))

@app.route("/admin_queries_view", methods=["POST", "GET"])
def admin_queries_view():
    mycursor.execute("SELECT * FROM contact")
    myresult = mycursor.fetchall()
    print(list(myresult))
    return render_template("admin_queries_view.html", myresult=list(myresult))


@app.route("/user_acc", methods=["POST", "GET"])
def user_acc():
    sql = "SELECT * FROM user_order where username=%s"
    val = (client_user,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    print(list(myresult))
    return render_template("user_acc.html", myresult=list(myresult))

@app.route("/user_shoe_view", methods=["POST", "GET"])
def user_shoe_view():
    sql = "SELECT * FROM shoe where username=%s"
    val = (client_user,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    print(list(myresult))
    return render_template("user_shoe_view.html", myresult=list(myresult))

@app.route("/admin_tshirt_view", methods=["POST", "GET"])
def admin_tshirt_view():
    mycursor.execute("SELECT * FROM tshirt")
    myresult = mycursor.fetchall()
    print(list(myresult))
    return render_template("admin_tshirt_view.html", myresult=list(myresult))

@app.route("/admin_shoe_view", methods=["POST", "GET"])
def admin_shoe_view():
    mycursor.execute("SELECT * FROM shoe")
    myresult = mycursor.fetchall()
    print(list(myresult))
    return render_template("admin_shoe_view.html", myresult=list(myresult))

@app.route("/user_tshirt_view", methods=["POST", "GET"])
def user_tshirt_view():
    sql = "SELECT * FROM tshirt where username=%s"
    val = (client_user,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    print(list(myresult))
    return render_template("user_tshirt_view.html", myresult=list(myresult))

@app.route("/user_register", methods=["POST", "GET"])
def user_register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        sql = "INSERT INTO user_detail (username, email, password) VALUES (%s, %s, %s)"
        val = (username, email, password)
        mycursor.execute(sql, val)
        mydb.commit()
        if mycursor.rowcount == 1:
           return render_template("user_login.html") 

    return render_template("user_register.html")

@app.route("/user_login", methods=["POST", "GET"])
def user_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        global client_user
        client_user = username
        
        sql = "select * from user_detail where username=%s and password=%s"
        val = (username, password)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        print(mycursor.rowcount)
        if int(mycursor.rowcount) == 1:
           return redirect("user_acc") 

    return render_template("user_login.html")

@app.route("/user_dashboard", methods=["POST", "GET"])
def user_dashboard():
    return render_template("user_dashboard.html", client_user=client_user)


@app.route("/user_cat", methods=["POST", "GET"])
def user_cat():
    if request.method == "POST":
        i1 = request.form.get("i1")
        # i2 = request.form.get("i2")
        # i3 = request.form.get("i3")
        # i4 = request.form.get("i4")
        return render_template("user_fab.html",i1=i1,username=client_user)

@app.route("/user_order", methods=["POST", "GET"])
def user_order():
    if request.method == "POST":
        username = request.form.get("username")
        category = request.form.get("i1")
        measurement = request.form.get("measurement")
        # payment = request.form.get("payment")
        fabric = request.form.get("f1")
        # fabric = request.form.get("f2")
        # fabric = request.form.get("f3")
        # fabric = request.form.get("f4")
        # fabric = request.form.get("f1,f2,f3,f4")
        sql = "INSERT INTO user_order (username,category,fabric,measurement) VALUES (%s,%s, %s,%s)"
        val = (username,category,fabric,measurement)
        mycursor.execute(sql, val)
        mydb.commit()


    return render_template("checkout.html")

@app.route("/tshirt_print", methods=["POST", "GET"])
def tshirt_print():
    if request.method == "POST":
        username = request.form.get("username")
        text = request.form.get("text")
        color = request.form.get("c")
        size = request.form.get("s")
        # fabric = request.form.get("f2")
        # fabric = request.form.get("f3")
        # fabric = request.form.get("f4")
        # fabric = request.form.get("f1,f2,f3,f4")
        sql = "INSERT INTO tshirt (username,text,color,size) VALUES (%s,%s,%s, %s)"
        val = (username,text,color,size)
        mycursor.execute(sql, val)
        mydb.commit()
        
    return render_template("tshirt_print.html",username=client_user)

@app.route("/shoe_print", methods=["POST", "GET"])
def shoe_print():
    if request.method == "POST":
        username = request.form.get("username")
        text = request.form.get("text")
        color = request.form.get("c")
        size = request.form.get("s")
        # fabric = request.form.get("f2")
        # fabric = request.form.get("f3")
        # fabric = request.form.get("f4")
        # fabric = request.form.get("f1,f2,f3,f4")
        sql = "INSERT INTO shoe (username,text,color,size) VALUES (%s,%s,%s, %s)"
        val = (username,text,color,size)
        mycursor.execute(sql, val)
        mydb.commit()
        
    return render_template("shoe_print.html",username=client_user)

@app.route("/inv_delete", methods=["POST", "GET"], endpoint='inv_delete')
def inv_delete():
    id = request.args.get("id")
    mycursor.execute("DELETE FROM user_order where id=%s",(id,))
    mydb.commit()
    
    return redirect("admin_order_detail")

@app.route("/user_delete", methods=["POST", "GET"], endpoint='user_delete')
def user_delete():
    id = request.args.get("id")
    mycursor.execute("DELETE FROM user_detail where id=%s",(id,))
    mydb.commit()
    
    return redirect("admin_view_user")

@app.route("/shoe_delete", methods=["POST", "GET"], endpoint='shoe_delete')
def shoe_delete():
    id = request.args.get("id")
    mycursor.execute("DELETE FROM shoe where id=%s",(id,))
    mydb.commit()
    
    return redirect("admin_shoe_view")

@app.route("/tshirt_delete", methods=["POST", "GET"], endpoint='tshirt_delete')
def tshirt_delete():
    id = request.args.get("id")
    mycursor.execute("DELETE FROM tshirt where id=%s",(id,))
    mydb.commit()
    
    return redirect("admin_tshirt_view")

@app.route("/inv1_delete", methods=["POST", "GET"], endpoint='inv1_delete')
def inv1_delete():
    id = request.args.get("id")
    mycursor.execute("DELETE FROM user_order where id=%s",(id,))
    mydb.commit()
    
    return redirect("user_acc")

@app.route("/shoe1_delete", methods=["POST", "GET"], endpoint='shoe1_delete')
def shoe1_delete():
    id = request.args.get("id")
    mycursor.execute("DELETE FROM shoe where id=%s",(id,))
    mydb.commit()
    
    return redirect("user_shoe_view")

@app.route("/tshirt1_delete", methods=["POST", "GET"], endpoint='tshirt1_delete')
def tshirt1_delete():
    id = request.args.get("id")
    mycursor.execute("DELETE FROM tshirt where id=%s",(id,))
    mydb.commit()
    
    return redirect("user_tshirt_view")

@app.route("/query_delete", methods=["POST", "GET"], endpoint='query_delete')
def query_delete():
    id = request.args.get("id")
    mycursor.execute("DELETE FROM contact where id=%s",(id,))
    mydb.commit()
    
    return redirect("admin_queries_view")

@app.route("/admin_payment_details", methods=["POST", "GET"])
def admin_payment_details():
    # id = request.args.get("id")
    mycursor.execute("SELECT pt.name,pt.ccnumber,pt.exp,pt.cvv,pt.upiid,pt.cod, del.address,del.state,del.zip FROM payment_type as pt,delivery as del where pt.name=del.username")
    myresult = mycursor.fetchall()
    print(list(myresult))
    return render_template("admin_payment_details.html", myresult=list(myresult))

@app.route("/user_payment_detail", methods=["POST", "GET"])
def user_payment_detail():
    # id = request.args.get("id")
    mycursor.execute("SELECT pt.name,pt.ccnumber,pt.exp,pt.cvv,pt.upiid,pt.cod, del.address,del.state,del.zip FROM payment_type as pt,delivery as del where pt.name=del.username and pt.name=%s" ,(client_user,))
    myresult = mycursor.fetchall()
    print(list(myresult))
    return render_template("user_payment_detail.html", myresult=list(myresult))

@app.route("/checkout", methods=["POST", "GET"])
def checkout():
    if request.method == 'POST':
        username = request.form.get("name")
        email = request.form.get("email")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        zip = request.form.get("zip")
        sql = "INSERT INTO delivery(username, email, address,city,state,zip) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (username, email, address, city, state, zip)
        mycursor.execute(sql, val)
        mydb.commit()
        if mycursor.rowcount == 1:
            return render_template('checkout1.html')
        
    return render_template('checkout.html')

@app.route("/checkout1", methods=["POST", "GET"])
def checkout1():
    if request.method == 'POST':
        name = request.form.get("cardname")
        ccnumber = request.form.get("cardnumber")
        exp = request.form.get("exp")
        cvv = request.form.get("cvv")
        upiid = request.form.get("upiid")
        cod = request.form.get("cod")
        sql = "INSERT INTO payment_type(name, ccnumber, exp, cvv, upiid, cod) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (name, ccnumber, exp, cvv, upiid, cod)
        mycursor.execute(sql, val)
        mydb.commit()
        if mycursor.rowcount == 1:
            return render_template('pop_up.html')
        
    return render_template('checkout1.html')

if __name__=="__main__":
    app.run(debug=True)