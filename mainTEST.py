from testingRoboflowModel import GestureRecognizer

dict ={}
buffer = .5
test = GestureRecognizer(dict,buffer)
while True:
    test.recognizer_run()