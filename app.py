from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    with open('subscribers.txt', 'a') as file:
        file.write(email + "\n")
    return 'Thank you for subscribing!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
