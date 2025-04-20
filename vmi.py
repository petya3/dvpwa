from flask import Flask, request, render_template_string
import pickle
import html

app = Flask(__name__)

# Fake user session storage
user_sessions = {}

@app.route('/')
def index():
    return '''
        <h2>Welcome</h2>
        <form method="POST" action="/save">
            <input name="username" placeholder="Enter your username">
            <button type="submit">Save Session</button>
        </form>
    '''

@app.route('/save', methods=['POST'])
def save():
    username = request.form.get('username', 'guest')
    # Simulate storing user data as pickled object (bad idea)
    session_data = pickle.dumps({"user": username})
    user_sessions[username] = session_data
    safe_username = html.escape(username)
    return f"Session saved for {safe_username}. <a href='/load/{safe_username}'>Load session</a>"

@app.route('/load/<username>')
def load(username):
    session_data = user_sessions.get(username)
    if session_data:
        # 🔥 VULNERABILITY: unsafe deserialization of user-controlled data
        session = pickle.loads(session_data)
        return render_template_string("<h3>Hello {{user}}</h3>", user=session["user"])
    else:
        return "No session found."

if __name__ == '__main__':
    app.run(debug=True)
