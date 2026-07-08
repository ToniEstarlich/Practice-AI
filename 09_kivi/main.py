import cv2
import mediapipe as mp
import numpy as np

from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture


class HandTrackingApp(App):

    def build(self):
        # Webcam
        self.cap = cv2.VideoCapture(0)

        # MediaPipe hand detector
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.mp_draw = mp.solutions.drawing_utils

        # Kivy image
        self.img = Image()

        Clock.schedule_interval(self.update, 1.0 / 30.0)

        return self.img

    def update(self, dt):
        ret, frame = self.cap.read()

        if ret:
            # Mirror camera (selfie style)
            frame = cv2.flip(frame, 1)

            # Convert BGR → RGB
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process hand detection
            results = self.hands.process(rgb)

            # Draw hand landmarks if detected
            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    self.mp_draw.draw_landmarks(
                        frame,
                        handLms,
                        self.mp_hands.HAND_CONNECTIONS
                    )

            # Convert to Kivy texture
            buf = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, _ = buf.shape

            texture = Texture.create(size=(w, h))
            texture.blit_buffer(buf.tobytes(), colorfmt='rgb', bufferfmt='ubyte')

            self.img.texture = texture

    def on_stop(self):
        self.cap.release()


if __name__ == "__main__":
    HandTrackingApp().run()