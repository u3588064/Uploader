import math
from PIL import Image, ImageFont, ImageDraw
import datetime
import random
import textwrap
import re

#fonType参数需要修改为完整的字体文件名，字体文件一般在C:\Users\【用户名】\AppData\Local\Microsoft\Windows\Fonts这个文件夹下
def CreatePic(text,imgPath,size=[1242,1660],margin=2,backgroundRGB=[204,204,255],fontType=r'.ttf',fontRGB=[0,0,0],min_width=5, max_width=7):
#204,204,255
    sentences = re.split(r'[，。！？]+', text)
    for sentence in sentences:
        # 去除句子开头和结尾的空白字符
        sentence = sentence.strip()
        # 如果句子不为空，则打印输出
        if len(sentence) > 11:
            width = random.randint(min_width, max_width)
            # 使用 textwrap.fill() 函数将文本换行
            sentence = textwrap.fill(sentence, width=width)
        text='！\n'.join(sentences)
    print(text)
    
    size=tuple(size)
    backgroundRGB=tuple(backgroundRGB)
    fontRGB=tuple(fontRGB)

    image=Image.open("test_image.png")
    #image = Image.new('RGB', size, backgroundRGB) # 设置画布大小及背景色
    iwidth, iheight = image.size # 获取画布高宽

    # 计算字节数，GBK编码下汉字双字，英文单字。都转为双字计算
    size=len(text)/2
    # 计算字体大小，每两个字号按字节长度翻倍。
    fontSize=math.ceil((iwidth-(margin*2))/size)+5

    font = ImageFont.truetype(fontType, fontSize) # 设置字体及字号
    draw = ImageDraw.Draw(image)

    fwidth, fheight = draw.textsize(text, font) # 获取文字高宽
    owidth, oheight = font.getoffset(text)

    fontx = (iwidth - fwidth - owidth) / 2
    fonty = (iheight - fheight - oheight) / 2

    draw.text((fontx, fonty), text, fontRGB, font)
    image.save(imgPath+str(datetime.date.today())+'.jpg')# 保存图片
