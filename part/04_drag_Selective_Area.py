import cv2

Lbtn_Down = False
x_start = None
y_start = None

def draw_selective_area(event, x, y, flags, param):
    global Lbtn_Down, x_start, y_start
    if event == cv2.EVENT_LBUTTONDOWN:
        Lbtn_Down = True
        x_start = x
        y_start = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if Lbtn_Down:
            drawing_page = img.copy()
            cv2.rectangle(drawing_page, (x_start, y_start), (x, y), (0, 255, 0),2)
            cv2.imshow('img',drawing_page)
    elif event == cv2.EVENT_LBUTTONUP:
        if Lbtn_Down:
            Lbtn_Down = False
            width = x - x_start
            height = y - y_start
            if width < 0:
                width = x_start
                x_start = x
            if height < 0:
                height = y_start
                y_start = y
            if width != 0 and height != 0:
                roi = img[y_start:y_start+height, x_start:x_start+width]
                cv2.imshow('select_area', roi)
                cv2.moveWindow('select_area', 0, 0)
                cv2.imwrite('./select_area.png', roi)

img = cv2.imread('./capture.png')
cv2.imshow('img', img)
cv2.setMouseCallback('img', draw_selective_area)
cv2.waitKey()
cv2.destroyAllWindows()