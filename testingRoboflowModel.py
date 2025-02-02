from inference.models.utils import get_roboflow_model


from pywin32_testutil import testmain

import testingKeyboard
import cv2
import time



# Roboflow model
class GestureRecognizer:
    __slots__ = ['model_name', 'model_version', 'model', 'last_time',
                 'last_input', 'time_buffer','cap','last_x','last_y','last_dx','last_dy','last_width','last_height']





#WILL NEED TO TAKE IN DICTIONARY OF MAPPINGS

    def __init__(self, buffer_input) -> None:
        """
        Initializes the recognizer to be used within main.
        :param: mappings_input Dictionary of mappings from gestures to
        output objects
        """
        # Open the default camera (usually the built-in webcam)
        self.model_name = "rock-paper-scissors-sxsw"
        self.model_version = "14"
        self.model = get_roboflow_model(
            model_id="{}/{}".format(self.model_name, self.model_version),
            # Replace ROBOFLOW_API_KEY with your Roboflow API Key
            api_key="T9dyaU5pnxSWychmChZi"
        )
        self.last_time = 0
        self.last_input = ""
        self.last_x = 0
        self.last_y = 0
        self.last_dx = 0
        self.last_dy = 0
        self.last_width = 0
        self.last_height = 0
        self.time_buffer = buffer_input
        self.cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
        if not self.cap.isOpened():
            print("Error: Could not open camera.")
            exit()



        return

    def recognizer_ui_update(self,new_buffer):

        self.time_buffer = new_buffer
        return
    def recognizer_run(self) -> None:

        ret, frame = self.cap.read()

        if ret:
            # Run inference on the frame
            results = self.model.infer(image=frame,
                              confidence=0.50,
                              iou_threshold=0.5)

            # Plot image with face bounding box (using opencv)
            if results[0].predictions:
                prediction = results[0].predictions[0]

                x_center = int(prediction.x)
                y_center = int(prediction.y)
                width = int(prediction.width)
                height = int(prediction.height)

                current_input = str(prediction.class_name)
                x0 = x_center - width // 2
                y0 = y_center - height // 2
                x1 = x_center + width // 2
                y1 = y_center + height // 2
                cv2.rectangle(frame, (x0, y0), (x1, y1), (255, 255, 0), 10)
                #cv2.putText(frame,'Gesture', (x0, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
                cv2.putText(frame, str(x0), (x0, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
                cv2.putText(frame, str(y0), (x0+ 120, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
                # program will not recognize a similar input for a certain amount of real time
                # or until another input is recognized (FOR CLICK TYPE ONLY)
                if self.last_input != current_input or time.perf_counter() - self.last_time > self.time_buffer:
                    testingKeyboard.handle_action(current_input,x_center,y_center,width,height)

                    self.last_time = time.perf_counter()
                    self.last_input = current_input
                    self.last_dx = self.last_x-x_center
                    self.last_dy = -(self.last_y-y_center)
                    self.last_width = width
                    self.last_height = height
                else:
                    testingKeyboard.handle_action(self.last_input,self.last_x,self.last_y,width,height)

                self.last_x = x_center
                self.last_y = y_center





            # Display the resulting frame
            frame = cv2.flip(frame, 1)


            cv2.imshow('Webcam Feed', frame)



        else:
            print("Error: Could not read frame.")
            self.recognizer_terminate()


    def recognizer_terminate(self):
        self.cap.release()
        cv2.destroyAllWindows()
        return