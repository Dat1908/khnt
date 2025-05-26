# CORS: giup client tu domain khac co the su dung tai nguyen (API) cua Flask, Python
# SS: Flask: Bat SSL cho Backend de dam bao an toan du lieu
# Can co cac file chua khoa va chung chi so SSL
# import re
import os
from random import random
# Import flask
from flask import Flask
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
# Import cac ham chinh
from body_shape_calculator import get_body_shape
from face_shape_detector import load_face_model, get_face_shape
from skin_hair_color_detector import *  
# Face shape classes
classes = ['Heart', 'Oblong', 'Oval', 'Round', 'Square']
# Load Model 
model = load_face_model()

# Khởi tạo Flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = ""

# Giao diện trang chủ
@app.route("/")
def home_page():
    return render_template("home.html")

# Giao diện thông tin của personal color
@app.route("/face_shape/round", methods=['GET', 'POST']) # Personal color
def face_shape_func_round():
    # Nếu là POST (gửi file)
    if request.method == "POST":
         return render_template('round.html')

    else:
        # Nếu là GET thì hiển thị giao diện upload
        return render_template('round.html')
    
# Giao diện đoán face shape
@app.route("/face_shape", methods=['GET', 'POST']) # Face Shape
def face_shape_func():
    # Nếu là POST (gửi file)
    if request.method == "POST":
         try:
            # Lấy file gửi lên
            image = request.files['file']
            if image:
                # Lưu file3
                path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], 'static/' + image.filename)
                # app.config['UPLOAD_FOLDER'] = r"D:/Python/FusionAIVytec2023/static/"  # Dùng 'r' để tránh lỗi escape sequence

                # # Tạo thư mục nếu chưa có
                # os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

                # # Lọc bỏ ký tự đặc biệt trong tên file
                # safe_filename = re.sub(r'[/*?:"<>|]', '_', image.filename)
                # path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], safe_filename)
                print("Save = ", path_to_save)
                image.save(path_to_save)
                if detect_face(path_to_save) == False:
                    return render_template("face_shape.html", msg="Anh khong hop le")

                face_shape = get_face_shape(model, classes, image_path=path_to_save)
                # skin_color = get_skin_color(path_to_save)
                # hair_color = get_hair_color(path_to_save)
                
                label = f'Face: {face_shape}\n' 
                
                if face_shape in classes:
                    # Trả về kết quả
                    return render_template("face_shape.html", label=label,
                                            msg="Tải file lên thành công")
                else:
                    # Anh chat luong kem
                    return render_template("face_shape.html", 
                                            msg="Vui lòng chọn ảnh khác")
            else:
                # Nếu không có file thì yêu cầu tải file
                return render_template('face_shape.html', msg='Hãy chọn file để tải lên')

         except Exception as ex:
            # Nếu lỗi thì thông báo
            print(ex)
            return render_template('face_shape.html', msg='Không nhận diện được vật thể')

    else:
        # Nếu là GET thì hiển thị giao diện upload
        return render_template('face_shape.html')


# Giao diện thông tin của personal color
@app.route("/body_shape/hourglass", methods=['GET', 'POST']) # Personal color
def body_shape_func_hourglass():
    # Nếu là POST (gửi file)
    if request.method == "POST":
         return render_template('hourglass.html')

    else:
        # Nếu là GET thì hiển thị giao diện upload
        return render_template('hourglass.html')  

# Giao diện đoán face shape
@app.route("/body_shape", methods=['GET', 'POST'])
def body_shape_func():
    if request.method == "POST":
        # Lấy thông tin từ các trường input trong form
        bust = request.form.get('Bust')
        waist = request.form.get('Waist')
        hip = request.form.get('Hip')

        # Xử lý dữ liệu đầu vào, ví dụ: tính toán hình dáng cơ thể
        # body_shape = calculate_body_shape(bust, waist, hip)
        
        # Trả về kết quả, bạn có thể chuyển kết quả đó vào template hoặc trả về dạng JSON
        # return render_template('body_shape_result.html', body_shape=body_shape)
        body_shape = get_body_shape(int(bust), int(waist), int(hip))
        return render_template('body_shape.html', body_shape = body_shape, msg = "Thành công!")

    else:
        # Nếu là GET thì hiển thị giao diện form nhập liệu
        return render_template('body_shape.html')

# Giao diện thông tin của personal color
@app.route("/personal_color/light_summer", methods=['GET', 'POST']) # Personal color
def personal_color_func_light_summer():
    # Nếu là POST (gửi file)
    if request.method == "POST":
         return render_template('light_summer.html')

    else:
        # Nếu là GET thì hiển thị giao diện upload
        return render_template('light_summer.html')

# Giao diện đoán personal color
@app.route("/personal_color", methods=['GET', 'POST']) # Personal color
def personal_color_func():
    # Nếu là POST (gửi file)
    if request.method == "POST":
         try:
            # Lấy file gửi lên
            image = request.files['file']
            if image:
                # Lưu file
                path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], 'static/' + image.filename)
                # # Định nghĩa thư mục lưu file
                # app.config['UPLOAD_FOLDER'] = r"D:/Python/FusionAIVytec2023/static/"  # Dùng 'r' để tránh lỗi escape sequence

                # # Tạo thư mục nếu chưa có
                # os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

                # # Lọc bỏ ký tự đặc biệt trong tên file
                # # import re
                # safe_filename = re.sub(r'[/*?:"<>|]', '_', image.filename)
                # path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], safe_filename)
                print("Save = ", path_to_save)
                image.save(path_to_save)
                if detect_face(path_to_save) == False:
                    return render_template("personal_color.html", msg="Anh khong hop le")

                skin_color = get_skin_color(path_to_save)
                hair_color = get_hair_color(path_to_save)
                
                # Xu li de ra loai personal color
                # label = str(skin_color) + ' ' + str(hair_color)
                label = personal_color(skin_color, hair_color)
                
                    # Trả về kết quả
                return render_template("personal_color.html", label=label,
                                        msg="Tải file lên thành công")
            else:
                # Nếu không có file thì yêu cầu tải file
                return render_template('personal_color.html', msg='Hãy chọn file để tải lên')

         except Exception as ex:
            # Nếu lỗi thì thông báo
            print(ex)
            return render_template('personal_color.html', msg='Không nhận diện được vật thể')

    else:
        # Nếu là GET thì hiển thị giao diện upload
        return render_template('personal_color.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)