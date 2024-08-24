import cv2
import tkinter as tk
from tkinter import messagebox, Frame, Button, Label
from PIL import Image, ImageTk


class FaceDetector:
    def __init__(self, root):
        self.root = root
        self.root.title("实时人脸检测")

        # UI设置
        self.setup_ui()

        # OpenCV初始化
        self.cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        self.face_cascade = cv2.CascadeClassifier(self.cascade_path)
        self.cap = None

    def setup_ui(self):
        self.root.configure(bg='white')

        title_label = Label(self.root, text="实时人脸检测", font=('Arial', 24), bg='white', pady=10)
        title_label.pack()

        self.frame = Frame(self.root, bg='white')
        self.frame.pack(padx=20, pady=20)

        self.start_button = Button(self.frame, text="开始检测", command=self.start_detection, width=15, height=2)
        self.start_button.grid(row=0, column=0, padx=10, pady=10)

        self.stop_button = Button(self.frame, text="停止检测", command=self.stop_detection, width=15, height=2,
                                  state=tk.DISABLED)
        self.stop_button.grid(row=0, column=1, padx=10, pady=10)

        self.camera_label = Label(self.root, text="摄像头状态: 未开启", font=('Arial', 12), bg='white')
        self.camera_label.pack(pady=10)

        self.camera_view = Label(self.root, bg='white')
        self.camera_view.pack()

        exit_button = Button(self.root, text="退出程序", command=self.root.quit, width=15, height=2)
        exit_button.pack(pady=20)

    def start_detection(self):
        if self.cap is None or not self.cap.isOpened():
            self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            messagebox.showerror("错误", "无法打开摄像头")
            return

        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.update_camera_label("开启")
        self.detect_faces()

    def detect_faces(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=img)

            self.camera_view.configure(image=img)
            self.camera_view.image = img

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            self.stop_detection()
            return

        self.root.after(10, self.detect_faces)

    def stop_detection(self):
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.update_camera_label("未开启")
        self.camera_view.configure(image='')

    def update_camera_label(self, status):
        self.camera_label.config(text=f"摄像头状态: {status}")

    def quit_program(self):
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = FaceDetector(root)
    root.mainloop()
