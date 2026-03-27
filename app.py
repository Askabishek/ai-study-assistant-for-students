from flask import Flask, request, jsonify
from db import run_query
import os

app = Flask(__name__)

# 🔥 Auto-create DB if not exists (IMPORTANT for Render)
if not os.path.exists("study.db"):
    import init_db


# 🔥 Natural Language → SQL Logic
def convert_to_sql(user_input):
    user_input = user_input.lower()

    if "ai topics" in user_input:
        return "SELECT topic FROM study_materials WHERE subject='AI';"

    elif "dsa" in user_input:
        return "SELECT topic FROM study_materials WHERE subject='DSA';"

    elif "faculty" in user_input:
        return "SELECT subject, faculty FROM study_materials;"

    elif "deep learning" in user_input:
        return "SELECT notes FROM study_materials WHERE topic='Deep Learning';"

    else:
        return "SELECT * FROM study_materials;"


@app.route("/")
def home():
    return "✅ AI Study Assistant is running!"


@app.route("/query", methods=["POST"])
def query():
    user_input = request.json["query"]

    sql_query = convert_to_sql(user_input)
    result = run_query(sql_query)

    return jsonify({
        "user_query": user_input,
        "sql_generated": sql_query,
        "result": result
    })


# 🔥 IMPORTANT FOR RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
