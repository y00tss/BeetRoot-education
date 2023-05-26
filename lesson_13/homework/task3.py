CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController():
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self):
        self.current_channel_index = 0
        return self.current_channel()

    def last_channel(self):
        self.current_channel_index = len(self.channels) - 1
        return self.channels[self.current_channel_index]



    def turn_channel(self, N):
        if 1 <= N <= (len(self.channels) - 1):
            self.current_channel_index = N - 1
            return self.channels[self.current_channel_index]
        else:
            print(f'Channel {N} not works')

    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.current_channel()

    def previous_channel(self):
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def is_exist(self, channel):
        if isinstance(channel, int):
            return "Yes" if 1 <= channel <= len(self.channels) else "No"
        elif isinstance(channel, str):
            return "Yes" if channel in self.channels else "No"
        else:
            return "Invalid argument"


controller = TVController(CHANNELS)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(4))
print(controller.is_exist("BBC"))

# Можно убрать коммент, чтобы сделать проверку на правильность - True/False
# print(controller.first_channel() == "BBC")
# print(controller.last_channel() == "TV1000")
# print(controller.turn_channel(1) == "BBC")
# print(controller.next_channel() == "Discovery")
# print(controller.previous_channel() == "BBC")
# print(controller.current_channel() == "BBC")
# print(controller.is_exist(4) == "No")
# print(controller.is_exist("BBC") == "Yes")





