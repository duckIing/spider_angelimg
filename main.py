import requests
from lxml import etree
import os

# 目标网站
url = 'http://angelimg.spbeen.com/tag/1'

# 构造请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.3',
    'Referer': 'http://angelimg.spbeen.com/',
}

# 获取响应
response = requests.get(url, headers=headers)
response_text = response.text
# print(response_text)

# 网站响应字符串解析为HTML
html = etree.HTML(response_text)

# 使用xpath获取图标链接
images_links = html.xpath('.//img/@src')

# 创建保存图片的目录
save_dir = './images'
os.makedirs(save_dir, exist_ok=True)


for index, link in enumerate(images_links, start=1):
    # 图片名称
    img_name = f"{index}_{link.split('/')[-1]}"
    # 图片保存路径
    img_path = os.path.join(save_dir, img_name)

    try:
        # 获取图片响应
        img_response = requests.get(link, headers=headers)
        # print(img_response.request.headers)
        # print(img_response.content)
        with open(img_path, 'wb') as f:
            # 写入本地文件
            f.write(img_response.content)
    except Exception as e:
        print(e)
