from flask import Flask, request
import sqlite3
import os 
app = Flask(__name__)

@app.route('/')
def login_form():
    return '''
    <form action="/login" method="post">
        Username: <input name="username">
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}'"
        print("Running query:", query)
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            return "✅ Login Success"
        else:
            return "❌ Login Failed"
    except Exception as e:
        return f"❌ Internal Error: {e}"

app.run(debug=False, use_reloader=False)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)