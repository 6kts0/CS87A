from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    usr_input = data.get('message')

    result = f"You sent: {usr_input} Length: {len(usr_input)}"
    return jsonify({'response': result})

if __name__ == '__main__':
    app.run(debug=False)