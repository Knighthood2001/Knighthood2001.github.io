import re
import requests
import os
from datetime import datetime

def wechat_image_get(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/124.0.0.0 Safari/537.36"
    }

    timestamp = int(datetime.now().timestamp())
    img_path = "wechat_image/" + str(timestamp)
    if not os.path.exists(img_path):
        os.makedirs(img_path)

    response = requests.get(url=url, headers=headers).text
    rule = re.compile('data-src="([^"]+)"').findall(response)
    i = 1
    for line in rule:
        # 过滤掉非链接的数据
        if line.startswith('https') or line.startswith('http'):
            images_data = requests.get(url=line, headers=headers).content
            with open(img_path + '/' + str(i) + '.jpg', 'wb') as f:
                f.write(images_data)
            print('正在下载第: ' + str(i) + '张图片')
            i += 1
    print('壁纸全部下载完成, 请注意查看！')

if __name__ == '__main__':
    url = 'https://mp.weixin.qq.com/s/wcWYXcCP1gEkJ0e6TvoOMg'
    wechat_image_get(url)