from PIL import ImageGrab       #install pillow

imgg = ImageGrab.grab().resize((900,600))
imgg.save('capture.png')