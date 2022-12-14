class tv_set():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channel_list = []

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on == True:
            print("TV set is on, the channel number is", self.channel_no)
        else:
            print("TV set is off")

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channel_list):
        self.channel_list = channel_list

    def show_channels(self):
        print(self.channel_list)



tv1 = tv_set()
tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.set_channel(5)
tv1.set_channels(["TVP1", "TVP2", "Polsat", "TVN",  "Filmbox", "Discovery"])
tv1.show_channels()
tv1.show_status()
tv1.turn_off()
tv1.show_status()