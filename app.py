from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username != "12341234" or password != "12341234":
            error = "[사용자 ID]를 올바르게 입력해 주십시오!"

        else:
            return redirect(url_for('gongji'))  # 로그인 성공 시 다른 페이지로 이동 가능

    return render_template("login.html", error=error)

@app.route("/gongji")
def gongji():
    return render_template("gongji.html")


# 로그인 성공 시 이동하는 대시보드
@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/neyock")
def neyock():
    return render_template("neyock.html")

@app.route("/yebi")
def yebi():
    return render_template("yebi.html")

@app.route("/user_info")
def user_info():
    return render_template("user_info.html")

@app.route("/menuTop")
def menuTop():
    return render_template("menuTop.html")



# 로그인 실패 시 이동하는 페이지
@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=1556)
