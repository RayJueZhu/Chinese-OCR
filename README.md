# Chinese-OCR   基于tensorflow、keras+vgg16方向识别+ctpn+crnn实现对自然场景的文字检测及端到端的OCR中文文字识别
python3.6,GPU版的chinese-ocr的修改与支持
之前作3.6版本的chinese-ocr,只有对cpu的支持，使用gpu后发现很多不好解决的小问题，经过一周的修改，已经全部跑通，特此分享
实际测试。一张复杂土图片完成OCR需要8s左右，vgg16的方向识别也没有太大的问题，但是本项目对已检测方向的文本OCR效果依然很一般，希望可以一起交流！
模型等资料github均可获得，也可以联系我。
e-mail：1448266751@qq.com
PS:以解决源代码中对于翻转角度的图片的识别问题，准确率如下：



