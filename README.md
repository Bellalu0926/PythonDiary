# PythonDiary

## 專案介紹

我的第一個網站

## 成品展示

[網站](https://belladiary.herokuapp.com/)

![](https://raw.githubusercontent.com/Bellalu0926/PythonDiary/master/bella.png)

## 使用技術

工具名稱 | 用途
---------|----------
Python 3 | 程式語言
Flask(python)    | 幫我建立伺服器
HTML/CSS  | 網頁表示&排版
Heroku   | 託管網頁
Github   | 存放原始碼

##程是碼片段
```python
@app.route("/")
def home():
    temp = glob.glob("articles/*")
    fill = []
    for t in temp:
      length = len(glob.glob(t + "/*.txt"))
      category = t.replace("articles/", "")
      f = (category, length)
      fill.append(f)
      print("來到首頁")
    return render_template("index.html", cat=fill)
    ```



