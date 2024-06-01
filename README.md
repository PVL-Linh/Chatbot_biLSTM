# Giới thiệu về Chatbot sử dụng mô hình LSTM

Chào mừng bạn đến với dự án Chatbot, một ứng dụng chatbot thông minh được xây dựng bằng Python và sử dụng mô hình mạng nơ-ron hồi quy dài ngắn hạn (LSTM) để cung cấp các phản hồi tự nhiên và chính xác cho người dùng. Dự án này sử dụng thư viện Keras để xây dựng và huấn luyện mô hình LSTM.

![4](https://github.com/PVL-Linh/Chatbot_biLSTM/assets/136146829/3249c608-9fc5-4103-a730-ab95c1c04361)
![3](https://github.com/PVL-Linh/Chatbot_biLSTM/assets/136146829/c77877c4-a6b7-4009-b2e0-250004a69680)

## Cấu trúc dự án

1. **Dữ liệu (Data):** Phần này chứa các tập dữ liệu câu hỏi và câu trả lời, được lấy từ một tập dữ liệu trên Kaggle.

    ![image](https://github.com/PVL-Linh/Chatbot_biLSTM/assets/136146829/c0cd61a6-b90d-451e-9570-08221a33c679)

2. **Mô hình LSTM:** Sau khi huấn luyện, mô hình LSTM được lưu dưới dạng file `chatbot_model.h5`.

3. **Ứng dụng Chat (Chat App):** Phần này chứa các file để load model đã huấn luyện và đưa câu hỏi từ người dùng vào model để nhận được các phản hồi.

## Cách sử dụng

1. **Huấn luyện mô hình LSTM:**
   - Sử dụng tập dữ liệu câu hỏi và câu trả lời để huấn luyện mô hình LSTM.

2. **Chạy ứng dụng Chatbot:**
   - Load model đã huấn luyện và sử dụng để nhận các câu hỏi từ người dùng và trả lời một cách tự động và chính xác.

## Hướng dẫn cài đặt

1. **Cài đặt Python:** Đảm bảo rằng bạn đã cài đặt Python trên máy của mình. Nếu chưa, bạn có thể tải Python từ [python.org](https://www.python.org/downloads/).

2. **Sao chép kho lưu trữ:**
   ```bash
   git clone https://github.com/PVL-Linh/Chatbot_biLSTM.git
   ```

3. **Cài đặt các thư viện cần thiết:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Huấn luyện mô hình:**
   - Sử dụng tệp `train.py` để huấn luyện mô hình LSTM.

5. **Chạy ứng dụng Chatbot:**
   - Sử dụng tệp `app.py` để khởi động ứng dụng chatbot và bắt đầu tương tác với người dùng.

## Đóng góp

Mọi đóng góp đều được hoan nghênh! Hãy thoải mái mở các vấn đề hoặc gửi yêu cầu kéo với các cải tiến, sửa lỗi hoặc tính năng mới.
