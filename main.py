from flask import Flask, jsonify
from venv import utilis

app = Flask(__name__)

@app.route("/new",methods = ["GET"])
def get_news():
    rows = utilis.get_all("SELECT * FROM news")
    data = []
    for r in rows:
        data.append({
            "id": r[0],
            "subject": r[1],
            "description": r[2],
            "image": r[3],
            "original_url": r[4],
            "category": r[5]
        })
    return jsonify({"news": data})


@app.route("/new/<int:news_id>", methods=["GET"])
def get_new_by_id(news_id):
    data = utilis.get_new_by_id(news_id)
    news ={
        "news_id": news_id,
        "subject": data[0],
        "description": data[1],
        "image": data[2],
        "original_url": data[3],
        "category_name": data[4]
    }
    return jsonify({"news":news})

if __name__  == "__main__":
    app.run()

