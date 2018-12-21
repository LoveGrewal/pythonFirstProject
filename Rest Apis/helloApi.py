from flask import Flask,request
import apiFunction as apf
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"



@app.route("/preview")
def preview():
    #return apf.top5().to_json(orient='records')
    start = request.args.get("start", type=int, default=0)
    end = request.args.get("end", type=int, default=5)
    column_str = request.args.get("columns", type=str, default="0")
    return apf.filteredColumn(start, end, column_str).to_html()

@app.route("/filteredColumn")
def filteredColumn():
    #return apf.top5().to_json(orient='records')
    column_name = request.args.get("name", type=str, default='CroMax_RX')
    operator = request.args.get("operator", type=str, default='equals')
    value = request.args.get("value", type=int, default=0)
    return apf.specificFilteredColumn(column_name, operator, value).to_html()

@app.route("/columns/<column>")
def col_preview(column):
    #return apf.top5().to_json(orient='records')
    return apf.top5Column(column).to_html()



if __name__ == "__main__":
    app.run()