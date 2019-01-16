from PIL import Image
import numpy as np
from io import BytesIO

def image_gray(img):
    w = img.size[0]
    h = img.size[1]
    img_video = img.convert("YCbCr")  # 转化为视频格式

    c = Image.new("1", (w, h))
    for x in range(w):
        for y in range(h):
            light, cb, cr = img_video.getpixel((x, y))
            if light < 120:
                c.putpixel((x,y),(0,))
            else:
                c.putpixel((x,y),(1,))
    return c

def image_denoiser(img_matrix):

    # 先把周围一圈的去噪
    h, w = img_matrix.shape
    img_matrix[:, (0, 1, w-1)] = 1
    img_matrix[(0, 1, h-1), :] = 1


def image_process(img_bin):
    img = Image.open(BytesIO(img_bin))
    gray_img = image_gray(img)
    img_matrix = np.array(gray_img, dtype=np.ubyte)
    image_denoiser(img_matrix)
    return image_split(img_matrix)

def image_split(img_matrix):
    h, w = img_matrix.shape
    index = 7
    char_weight = 10
    interval = 3
    splits = []
    while index + char_weight < w:
        splits.append(img_matrix[:, index: index+char_weight]) # (index, 0, index+char_weight, h))
        index += char_weight + interval
    return splits

def imsave(img_bin, path):
    img = Image.open(BytesIO(img_bin))
    img.save(path)
