import cv2


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)


def video_demo():
    capture = cv2.VideoCapture(0)
    while(True):
            ret, frame = capture.read()
            c = cv2.imread("video", frame)
            if c == 27:
                break


src = cv2.imread("图片1.jpg")
cv2.namedWindow("dog")
cv2.imshow("Image", src)
# get_image_info(src)
# video_demo()
cv2.waitKey(0)
cv2.destoryAllWindows()