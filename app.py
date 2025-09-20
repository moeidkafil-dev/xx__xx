from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ذخیره داده‌ها
keys_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_keys', methods=['POST'])
def receive_keys():
    data = request.json.get('keys')
    if data:
        keys_data.append(data)
    return jsonify({"status": "ok"})

@app.route('/get_keys', methods=['GET'])
def get_keys():
    return jsonify(keys_data)

if __name__ == '__main__':
    app.run(debug=True)
