from flask import Flask, request, render_template
from flask import send_file
from flask import redirect
from wechat_cover_image_get import get_image
from wechat_image_get import wechat_image_get
app = Flask(__name__)


@app.route('/')
def index():
    # 在这里加载模板文件
    return render_template('认知up吧的导航网站.html')

# ---------
@app.route('/get_cover')
def get_cover():
    return render_template('get_cover.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    input_url = request.form['input_text']
    img = get_image(input_url)
    # return send_file(readme_img, mimetype='image/jpeg') #图片格式不太可用
    # return redirect(readme_img)#出现此图片来自微信公众平台，未经允许不可引用
    # return readme_img  # 该方法导致只是链接，但是点击不能跳转。
    return send_file(img[1])
# ---------

@app.route('/get_all_images')
def get_all_images():
    return render_template('get_wechat_article_all_images.html')

@app.route('/process_input2', methods=['POST'])
def process_input2():
    input_url = request.form['input_text']
    wechat_image_get(input_url)
    return "成功"

if __name__ == '__main__':
    app.run(debug=True)
