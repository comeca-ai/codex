from flask import Flask, send_file, request

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/contact')
def contact():
    return send_file('contact.html')

@app.route('/book', methods=['POST'])
def book():
    # Handle booking form submission
    data = request.form
    print(f"Booking received: {data}")
    return "Booking received!", 200

@app.route('/support', methods=['POST'])
def support():
    # Handle support form submission
    data = request.form
    print(f"Support request received: {data}")
    return "Support request received!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
