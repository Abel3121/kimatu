#ライブラリのインストール
# from cgitb import text
import streamlit as st
import pyocr
# import os
from PIL import Image

file = st.file_uploader("ここにファイルを入れてね")

def main():
	
	if file is not None:
		pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

		#利用可能なOCRエンジンをリストで取得する
		tools = pyocr.get_available_tools()

		#利用するOCRエンジンのオブジェクトを作成する
		tool = tools[0]

		#ocr対象の画像ファイルを読み込む
		img = Image.open(file)
		st.image(img)

		#Tesseract のオプションを設定する
		#デフォルト値は、「3」で「0～6」まで設定することができます。
		#今回は、「6」の精度が良さそうなので「tesseract_layout=6」を利用しています。
		builder = pyocr.builders.TextBuilder(tesseract_layout=6)

		#ocr実行
		text = tool.image_to_string(img,lang="jpn",builder=builder)

		st.write('加工前')
		st.write(text)

		a=prepare_picture()
		st.write('加工後')
		text_after = tool.image_to_string(a,lang="jpn",builder=builder)
		st.write(text_after)

	else:
		st.write('ファイルを入れてください')

#画像処理
def prepare_picture():
	img = Image.open(file)
	img = img.convert('RGB')
	size = img.size
	img2 = Image.new('RGB',size)

	border = 110

	for i in range(size[0]):
		for j in range(size[1]):
			r,g,b = img.getpixel((i,j))
			if r > border or g > border or b > border:
				r = 255
				g = 255
				b = 255
			img2.putpixel((i,j),(r,g,b))
	return img2

if __name__ == "__main__":
	main()
