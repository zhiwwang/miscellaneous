
# Weibo_Topic_WordsCount

*抓取微博话题下所有博文内容及统计词语出现频率*

**【简介】**

使用 Selenium 模拟用户点击操作抓取，获取对应话题下所有的博文内容。加入文本清洗，统计微博话题下对应的博文中各个词语的出现频次，导出为CSV文件，可用于市场分析等领域。

PS: 由于是使用Selenium模拟真实用户操作，抓取速度较慢，建议用于少于1000条博文的需求中。

**【运行环境要求】**

1. Firefox 浏览器
2. 安装驱动 GeckoDriver
   https://blog.csdn.net/hy_696/article/details/80114065



> **参考**
>
> https://zhuanlan.zhihu.com/p/370036445
>
> https://blog.csdn.net/m0_37693335/article/details/85775697


# heif
*图片批量自动编码heif格式*

**【简介】**

图片压缩：识别文件夹中的所有图片，批量自动压缩成heif格式，并负责源图片的metadata数据到新图片。比较压缩前后图片的体积，保留体积小的那个。(统计压缩率大概80%)

视频压制：自动识别文件夹中的所有非h265视频，保持码率和清晰度不变，批量压制成h265视频。


**【运行环境要求】**

1. 图片压缩：ImageMagick https://www.imagemagick.org/
2. 视频压缩：ffmpeg https://ffmpeg.org/


