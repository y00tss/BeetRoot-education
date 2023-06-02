class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        self.logerror()

    def logerror(self):
        with open('logs.txt', 'a') as file:
            file.write(self.msg + "\n")


try:
    raise CustomException("My error")
except CustomException as e:
    print("CustomException - ", e)
