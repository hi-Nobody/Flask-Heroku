from flask import Flask
app_test=Flask(__name__)#__name__表示目前執行的模組

@app_test.route("/")#函式的裝飾(Decorator):以函式為基礎，提供附加的功能
def home():
    return "Hello flkk"

@app_test.route("/test")#/test是代表我們要處理的網站路徑
def test():
    return "Hello test123"

if __name__ == "__main__":#如果以主程式執行
    app_test.run(debug=True)#立刻啟動伺服器
