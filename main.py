# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import os

# 去掉 https warnings
requests.packages.urllib3.disable_warnings()

headers = {
	'user-agent': 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; MI 4S Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3'
}

folder = './download_douyin/'
if not os.path.exists(folder):
	os.mkdir(folder)


def parse_douyin_share(url):
	res = requests.get(url, headers=headers, verify=False)
	res.encoding = 'utf-8'
	data = res.text
	html = BeautifulSoup(data, 'lxml')
	addr = html.find('video', class_='video-player').get('src').replace('playwm', 'play')
	video_id = data.split("itemId: \"")[1].split("\",")[0]
	return video_id, addr


def download(url, id):
	video = requests.get(url, headers=headers, verify=False)
	filename = os.path.abspath(folder + id + '.mp4')
	with open(filename, 'wb') as f:
		f.write(video.content)
	return filename


while True:
	url = input('链接:')
	url = 'https://v.douyin.com/Gce3Sx/'
	videoid, addr = parse_douyin_share(url)
	download(addr, videoid)
