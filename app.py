from flask import Flask, render_template, request
import csv
from test import predict_class , getResponse , intents
from keras.models import load_model


app = Flask(__name__, template_folder='templates')
model = load_model('./chatbot_model.h5')

history_file = 'history.csv'


"""data_file = open("intents_1.json").read()
intents = json.loads(data_file)"""
def load_chatbot_model():
    global model
    if model is None:
        model = load_model('chatbot_model.h5')

def chatbot_response(msg):
    load_chatbot_model()  # Tải mô hình trước khi sử dụng
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res
def write_to_csv(data):
    with open(history_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)

"""def read_from_csv():
    try:
        with open(history_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return []"""
def read_from_csv():
    data = []
    try:
        with open(history_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Bỏ qua hàng tiêu đề (nếu có)
            for row in reader:
                data.append([row[0], row[1]])
    except FileNotFoundError:
        pass  # Tránh lỗi nếu không tìm thấy file
    return data


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    output = chatbot_response(user_input)  # For simplicity, echo the input as output

    if user_input:
        write_to_csv([user_input, output])  # Save question-answer pair to CSV

    return render_template('index.html', output=output)

@app.route('/history', methods=['POST'])
def history():
    data = read_from_csv()  # Đọc dữ liệu từ file CSV
    return render_template('history.html', data=data)



if __name__ == '__main__':
    app.run(debug=True)