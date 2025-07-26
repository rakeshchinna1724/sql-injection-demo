from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# HTML template
form_html = '''
<h2>Login</h2>
<form method="POST">
  Username: <input name="username"><br>
  Password: <input name="password" type="password"><br>
  <button type="submit">Login</button>
</form>
<p>{{ message }}</p>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # ✅ SECURE: Parameterized query
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            message = '✅ Logged in successfully!'
        else:
            message = '❌ Invalid username or password.'
    return render_template_string(form_html, message=message)

if __name__ == '__main__':
    app.run(debug=True)
