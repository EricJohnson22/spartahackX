from testingRoboflowModel import GestureRecognizer


buffer = .1
test = GestureRecognizer(buffer)
while True:
    test.recognizer_run()