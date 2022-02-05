
from importlib import resources
from sre_constants import SUCCESS
from flask import Flask, request, jsonify
from mysql import connector
from flask_cors import CORS, cross_origin


#INSERT INTO `pesquisa` (`id`, `valor`, `coment`, `data`) VALUES ('a', '1', 'ola', '2022-02-01');

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
@cross_origin(origins="*")
def store():
    data = request.get_json()
    print(data)
    db = connector.connect(host="localhost", database="satisfa", user="root", password="")
    dbinfo = db.get_server_info()
    cursor = db.cursor()
    sql = """INSERT INTO pesquisa (id,valor,coment) VALUES (%s,%s,%s)"""
    #cursor.execute("INSERT INTO `pesquisa` (`id`, `valor`, `coment`, `data`) VALUES (`{}`,`{}`,`{}`,`{}`)".format(data["id"], data["valor"], data["coment"], "NOW()" ))
    cursor.execute(sql,(data["id"], data["valor"], data["coment"]))
    db.commit()
    #record = cursor.fetchone()
    
    return jsonify(success=True)

if __name__ == "__main__":
    app.run(debug=True)