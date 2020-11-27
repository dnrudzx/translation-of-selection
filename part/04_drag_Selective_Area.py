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

            rect = [-1, -1, -1, -1]
            if height > 0:
                rect[0] = y_start
                rect[1] = y_start + height
            else:
                rect[0] = y
                rect[1] = y_start
            if width > 0:
                rect[2] = x_start
                rect[3] = x_start + width
            else:
                rect[2] = x
                rect[3] = x_start
            if width != 0 and height != 0:
                roi = img[rect[0]:rect[1], rect[2]:rect[3]]
                cv2.imshow('select_area', roi)
                #cv2.moveWindow('select_area', 0, 0)
                cv2.imwrite('./select_area.png', roi)

img = cv2.imread('./capture.png')
cv2.imshow('img', img)
cv2.setMouseCallback('img', draw_selective_area)
cv2.waitKey()
cv2.destroyAllWindows()