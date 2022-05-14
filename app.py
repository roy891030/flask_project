from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)


#############部屬mysql############

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roy891030891030'
app.config['MYSQL_DB'] = 'index_name'
mysql = MySQL(app)
#############部屬mysql############


# 建立路徑/到的處理函式`,使用GET方法
#############根目錄############
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')
#############根目錄############


#############第二個網頁############
@app.route("/page")
def page():
    return render_template("page.html", name="")
#############第二個網頁############


# 處理form(show)
#############顯示form資料############
@app.route("/show", methods=["POST"])
def show():
    # 取得name = email (POST)
    return render_template("hello.html", email="email")
#############顯示form資料############

    # cursor = mysql.connection.cursor()
    # cursor.execute("INSERT INTO names VALUES(%s)", (email))
    # mysql.connection.commit()
    # cursor.close()
#############程式跑起來############
app.run(port=8000)
#############程式跑起來############

# return render_template("page.html", name="")

# print("method of request", request.method)
# print("protocal", request.scheme)
# print("host", request.host)
# print("path", request.path)
# print("the url", request.url)
# print("browser and os", request.headers.get("user-agent"))
# print("peference of language", request.headers.get("accept-language"))

# return "hello "


# dynamic route
# @app.route("/user/<name>")
# def handleUser(name):
#     if name == "roy":
#         return "ddd"+name
#     else:
#         return "f"+name
