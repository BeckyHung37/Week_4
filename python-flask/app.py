from flask import Flask, request, redirect, render_template, session
app=Flask(
    __name__,
    static_url_path="/"
) #建立app物件
app.config['SECRET_KEY'] = 'becky' #用來解決flask使用session產生的錯誤

#建立路徑/對應的處理函式
@app.route("/")
def index(): #用來回應網站首頁連線的函式
    return render_template("index.html")

@app.route("/member")
def member():
    if session["user_status"] == "signin":
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error")
def error(): 
    return render_template("error.html")

@app.route("/signin", methods=["POST"]) #不寫的話其實預設就是GET
def signin(): 
    username=request.form["username"]
    password=request.form["password"]
    if username == "test" and password == "test":
        session["user_status"]="signin"
        return redirect("/member")
    else:
        return redirect("/error")

@app.route("/signout", methods=["GET"]) 
def signout(): 
    session["user_status"]="signout"
    return redirect("/")



app.run(port=3000) #啟動網站伺服器
