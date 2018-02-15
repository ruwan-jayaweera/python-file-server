from threading import Thread

import cv2
import sys

class FaceDetector:
    cascPath = "haarcascade_frontalface_default.xml"

    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier(FaceDetector.cascPath)

    def detect_face(self, image_frame):
        gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

        return self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )


class Camera:
    def __init__(self, id):
        self.id = id

    def allocate(self):
        self.video_capture = cv2.VideoCapture(self.id)

    def release(self):
        self.video_capture.release()

    def capture_vedio(self):
        return self.video_capture.read()

    def draw_rectangle(self, frame, x, y, w, h):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


class FaceDetectionAgent:
    def __init__(self, cameras):
        self.cameras = cameras
        self.cameraThreads = []

    def execute(self):
        for camera in self.cameras:
            camera.allocate()
            cameraThread = FaceDetectionTread(camera)
            self.cameraThreads.append(cameraThread)
            print("starting thread ", cameraThread.id)
            cameraThread.start()

        for thread in self.cameraThreads:
            thread.join()
            print("joining thread", thread.id)
            thread.camera.release()

        cv2.destroyAllWindows()


class FaceDetectionTread(Thread):
    face_detector = FaceDetector()

    def __init__(self, camera: Camera):
        Thread.__init__(self)
        self.camera = camera
        self.id = camera.id


    def run(self):
        while True:
            frame = self.camera.capture_vedio()
            faces = FaceDetectionTread.face_detector.detect_face(frame)
            for (x, y, w, h) in faces:
                self.camera.draw_rectangle(frame, x, y, w, h)
                print("face found")

            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


if __name__ == '__main__':
    camera_ids = []
    if sys.argv.__len__() > 1:
        camera_id_args = sys.argv[1]
        camera_id_args = camera_id_args.split(",")
        for camera_id_arg in camera_id_args:
            camera_ids.append(int(camera_id_arg))
    else:
        camera_ids.append(20)

    cameras = []
    for camera_id in camera_ids:
        cameras.append(Camera(camera_id))

    agent = FaceDetectionAgent(cameras)
    agent.execute()
