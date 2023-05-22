import cv2

# 打开默认的摄像头
cap = cv2.VideoCapture(0)

while True:
    # 检查摄像头是否成功打开
    if not cap.isOpened():
        print("无法打开摄像头")
        break

    # 逐帧捕获图像
    ret, frame = cap.read()

    # 将每一帧显示出来
    cv2.imshow('frame', frame)

    # 按 Q 键退出
    if cv2.waitKey(1) == ord('q'):
        break

# 释放摄像头资源
cap.release()
cv2.destroyAllWindows()
