class TV:
    def __init__(self):
        self.volume = 0
        self.is_on = False

    def power_on(self):
        self.is_on = True
        print("TV is now ON.")

    def power_off(self):
        self.is_on = False
        print("TV is now OFF.")

    def set_volume(self, volume: int):
        self.volume = volume
        print(f"TV volume set to {self.volume}")

class Radio:
    def __init__(self):
        self.volume = 0
        self.is_on = False

    def power_on(self):
        self.is_on = True
        print("Radio is now ON.")

    def power_off(self):
        self.is_on = False
        print("Radio is now OFF.")

    def set_volume(self, volume: int):
        self.volume = volume
        print(f"Radio volume set to {self.volume}")

# Tight coupling between RemoteControl and specific device classes
class RemoteControl:
    def __init__(self, device_type):
        self.device = device_type
        self.device_is_on = False

    def power(self):
        if self.device_is_on:
            self.device.power_off()
            self.device_is_on = False
        else:
            self.device.power_on()
            self.device_is_on = True

    def volume_up(self):
        self.device.set_volume(self.device.volume + 1)

    def volume_down(self):
        self.device.set_volume(self.device.volume - 1)

# Client code using specific devices with RemoteControl
if __name__ == "__main__":
    tv = TV()
    radio = Radio()
    
    # Create remote control for TV
    remote_control_for_tv = RemoteControl(tv)
    remote_control_for_tv.power()
    remote_control_for_tv.volume_up()
    remote_control_for_tv.volume_down()
    remote_control_for_tv.power()

    print("\n")

    # Create remote control for Radio
    remote_control_for_radio = RemoteControl(radio)
    remote_control_for_radio.power()
    remote_control_for_radio.volume_up()
    remote_control_for_radio.volume_down()
    remote_control_for_radio.power()
