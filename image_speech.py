import cv2
import pytesseract
import os
from gtts import gTTS
from mutagen.mp3 import MP3
from playsound import playsound

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
current_dir = os.path.dirname(os.path.realpath(__file__))
audio_file = (current_dir+"/audio_text")
image_file = (current_dir+"/images_text")
language = 'en'
count = 0
while True:
    im_list = []
    for file_name in os.listdir(image_file):
        if file_name.split(".")[-1].lower() in {"png"}:
            im_list.append(file_name)
    string = ""
    for image in im_list:
        try:
            text=pytesseract.image_to_string(image_file+"/"+image)
            print(text)
            string = string+text
            os.remove(image_file+"/"+image)
        except:
            pass
    if string!="":
        text=string
        count = str(count)
        output = gTTS(text=text, lang=language, slow=False)
        output.save(audio_file+"/"+count+".mp3")
        playsound(audio_file+"/"+count+".mp3")
        os.remove(audio_file+"/"+count+".mp3")
        count = int(count)
        count+=1
        
        
            
