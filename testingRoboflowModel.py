from inference.models.utils import get_roboflow_model
import cv2
import time



# Roboflow model
class GestureRecognizer:
    __slots__ = ['model_name', 'model_version', 'mappings', 'model', 'last_time',
                 'last_input', 'time_buffer','cap']





#WILL NEED TO TAKE IN DICTIONARY OF MAPPINGS

    def __init__(self,mappings_input, buffer_input) -> None:
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

        self.cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
        if not self.cap.isOpened():
            print("Error: Could not open camera.")
            exit()
        #self.mappings = mappings_input
        #self.time_buffer = buffer_input
        #REMOVE THIS SHIT LATER FUCKING IDIOT
        self.mappings = {}
        self.mappings["Rock"] = 1
        self.mappings["Paper"] = 2
        self.mappings["Scissors"] = 3
        self.time_buffer = .5
        #THIS SHIT
        return

    def recognizer_ui_update(self,new_mappings,new_buffer):
        #THIS ALSO NEEDS TO BE CHANGED EVENTUALLY
        #self.mappings = self.new_mappings
        self.mappings = new_mappings
        self.time_buffer = new_buffer
        return
    def recognizer_run(self) -> None:
        # Capture frame-by-frame
        ret, frame = self.cap.read()

        # If the frame was read successfully, display it
        if ret:
            # Run inference on the frame
            results = self.model.infer(image=frame,
                              confidence=0.66,
                              iou_threshold=0.5)

            # Plot image with face bounding box (using opencv)
            if results[0].predictions:
                prediction = results[0].predictions[0]
                print(prediction)

                x_center = int(prediction.x)
                y_center = int(prediction.y)
                width = int(prediction.width)
                height = int(prediction.height)
                current_input = str(prediction.class_name)

                # program will not recognize a similar input for a certain amount of real time
                # or until another input is recognized (FOR CLICK TYPE ONLY)
                if self.last_input != current_input or time.perf_counter() - self.last_time > self.time_buffer:
                    print(current_input)

                    self.last_time = time.perf_counter()
                    self.last_input = current_input




            # Display the resulting frame
            cv2.imshow('Webcam Feed', frame)

            # Press 'q' to quit the video window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.recognizer_terminate()
        else:
            print("Error: Could not read frame.")
            self.recognizer_terminate()

# When everything is done, release the capture and destroy all windows
    def recognizer_terminate(self):
        self.cap.release()
        cv2.destroyAllWindows()
        return