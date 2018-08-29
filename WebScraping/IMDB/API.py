from flask import Flask, jsonify
from pymongo import MongoClient
import re

app = Flask(__name__)


@app.route('/movie/<string:title>')
def getTitle(title=""):
    try:
        mongo = MongoClient()
        db = mongo.movie
        titles = db.titles
        regex = re.compile(f"{title}", re.IGNORECASE)
        res = list(titles.find({"title": regex}, {'_id': 0}))
        data = getJson(res)
        # for doc in res:
        #     print("{")
        #     for key, value in doc.items():
        #         print(f"\t{key}: {value}\n")
        #     print("}")
        if res:
            return jsonify(data)
            # return render_template('hello.html', name=data)
        else:
            return "Not Found"
    except AttributeError:
        return 'Server Error'


def getJson(movies):
    result = {}
    for movie in movies:
        result[movie['title']] = movie
    # result = json.dumps(result)
    return result


if __name__ == '__main__':
    app.run()
