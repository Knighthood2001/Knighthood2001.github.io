import requests
import re
import os
#TODO 使用时间戳当作文件名称
def get_time():
    import time
    timestamp = int(time.time())
    return timestamp
#TODO 实现从网页图片保存到本地，输入为图片网址和保存路径
def image_save(image_url, path):
    if not os.path.exists(path):         # 如果文件夹不存在，则创建
        os.makedirs(path)

    # 发送 GET 请求获取图片数据
    response = requests.get(image_url)
    # 确保请求成功
    if response.status_code == 200:
        image_name = get_time()
        image_name = "{}.jpg".format(image_name)
        # 指定图片保存路径
        save_path = os.path.join(path, image_name)  # 这里将图片保存在名为 images 的文件夹中
        # 将图片数据写入文件
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f'图片已保存为: {save_path}')
        return save_path
    else:
        print(f'下载图片失败，状态码: {response.status_code}')

# TODO 微信公众号获取封面并保存，输入网址
def get_image(wechat_url):
    response = requests.get(wechat_url)

    # 检查响应状态码，200表示请求成功
    if response.status_code == 200:
        # 定义包含目标网址的字符串
        source_code = response.text
        # 使用正则表达式提取网址
        url_pattern = re.compile(r'cdn_url_1_1 = "(.*?)"')
        matches = url_pattern.findall(source_code)
        # 输出提取到的网址
        if matches:
            print(matches[0])
            file = image_save(matches[0], "cover_images")
            return matches[0], file

if __name__ == '__main__':
    # 定义目标网页的URL
    url = 'https://mp.weixin.qq.com/s/d7DUHB-hT8DExjpxsEncQw'
    print(get_image(url))