from inference.models.utils import get_roboflow_model
import cv2



# Roboflow model
model_name = "rock-paper-scissors-sxsw"
model_version = "14"

# Open the default camera (usually the built-in webcam)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Get Roboflow face model (this will fetch the model from Roboflow)
model = get_roboflow_model(
    model_id="{}/{}".format(model_name, model_version),
    # Replace ROBOFLOW_API_KEY with your Roboflow API Key
    api_key="T9dyaU5pnxSWychmChZi"
)

test_dict = {}
test_dict["Rock"] = 1
test_dict["Paper"] = 2
test_dict["Scissors"] = 3
buffer = ""
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If the frame was read successfully, display it
    if ret:
        # Run inference on the frame
        results = model.infer(image=frame,
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
            hold = str(prediction.class_name)


            if buffer != hold:
                print(hold)
            buffer = hold
        else:
            buffer = ""


        # Display the resulting frame
        cv2.imshow('Webcam Feed', frame)

        # Press 'q' to quit the video window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error: Could not read frame.")
        break

# When everything is done, release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()