from flask import Flask, render_template
import glob
from datetime import datetime
import os

app = Flask("Bella")

@app.route("/category/<c>")#文章標題和修改時間
def category(c):
  fs = glob.glob("articles/" + c + "/*.txt")
  fill = []
  for i, f in enumerate(fs):
    a = open(f)
    article = a.read()
    a.close()
    fp = f.split("/")[-1].replace(".txt", "")
    utc = datetime.utcfromtimestamp(os.path.getmtime(f))#電腦時間轉英國格林威治時間
    t = (i, fp, str(utc), article)#HTML MODEL會用到的ID, 文章標題,修改時間,文章內容
    fill.append(t)
  return render_template("category.html", cat=fill, title=c)

@app.route("/")#針對/做動作
def home():
    temp = glob.glob("articles/*")#找到符合格式的檔案
    fill = []#開始填空
    for t in temp:
      length = len(glob.glob(t + "/*.txt"))
      category = t.replace("articles/", "")
      f = (category, length)
      fill.append(f)
      print("來到首頁")#只有程式裡看得到
    return render_template("index.html", cat=fill)

app.run(debug=True, host="0.0.0.0", port="3000")#hpst 是IP位置 port是repl的固定號碼