from flask import Flask, jsonify, render_template
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

def get_connection():
    return psycopg2.connect(
        host='db',
        database='sampledb',
        user='admin',
        password='admin123'
    )

@app.route('/posts/json')
def get_posts_json():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT title, content FROM posts;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{'title': row[0], 'content': row[1]} for row in rows])

@app.route('/')
def home():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT title, content FROM posts;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('posts.html', posts=[{'title': r[0], 'content': r[1]} for r in rows])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
