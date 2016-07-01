# Zhihu_XiaChe_Audio
Use Baidu Speech API to play Zhihu daily "瞎扯"

# Installation
- This program only works on Linux and macOS. Compatible with Raspberry Pi.
- Install python2 packages in "requirements.txt".
- Install mplayer. Linux: `apt-get install mplayer`. macOS: `brew insall mplayer`
- You can use crontab on Raspberry Pi, to make this program as an alarm clock.

#Usage
- Register on [http://yuyin.baidu.com/](http://yuyin.baidu.com/) to get Baidu Speech API key.
- run zhihu_audio.py
- spider_zhihu.py: a small spider for Zhihu daily. API from [https://github.com/Artwalk/GO-ZhihuDaily](https://github.com/Artwalk/GO-ZhihuDaily)
- baidu_sound.py:Use Baidu Speech API to transfer text to speech.


# 知乎瞎扯广播
用百度语音API播放当天的知乎日报瞎扯。

# 安装
- 可用于linux 和 macOS. 兼容树莓派。
- 安装Python2的依赖包 "requirements.txt".
- 安装 mplayer. Linux: `apt-get install mplayer`. macOS: `brew insall mplayer`
- 可以使用树莓派的crontab定时任务，把此程序作为闹钟。

#使用说明
- 注册 [http://yuyin.baidu.com/](http://yuyin.baidu.com/) ,取得 百度 API key.
- 运行 zhihu_audio.py
- spider_zhihu.py:知乎日报小型爬虫，API来自 [https://github.com/Artwalk/GO-ZhihuDaily](https://github.com/Artwalk/GO-ZhihuDaily)
- baidu_sound.py:百度语音API，文字转语音。
