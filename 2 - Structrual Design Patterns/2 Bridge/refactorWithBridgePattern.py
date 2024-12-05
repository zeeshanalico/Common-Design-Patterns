from abc import ABC, abstractmethod

# Implementation Interface
class Device(ABC):
    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass

    @abstractmethod
    def set_volume(self, volume: int):
        pass

# Concrete Implementations of the Device
class TV(Device):
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

class Radio(Device):
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

# Abstraction
class RemoteControl:
    def __init__(self, device: Device):# instead of writing TV | Radio,write Device it is polymorphic
        self.device = device

    def power(self):
        if self.device.is_on:
            self.device.power_off()
        else:
            self.device.power_on()

    def volume_up(self):
        self.device.set_volume(self.device.volume + 1)

    def volume_down(self):
        self.device.set_volume(self.device.volume - 1)

# Refined Abstraction
class AdvancedRemote(RemoteControl):
    def mute(self):
        self.device.set_volume(0)
        print("Device is now muted.")

# Client Code
if __name__ == "__main__":
    # Using TV with BasicRemote
    tv = TV()
    basic_remote_for_tv = RemoteControl(tv)
    basic_remote_for_tv.power()
    basic_remote_for_tv.volume_up()
    basic_remote_for_tv.volume_down()
    basic_remote_for_tv.power()

    print("\n")

    # Using Radio with AdvancedRemote
    radio = Radio()
    advanced_remote_for_radio = AdvancedRemote(radio)
    advanced_remote_for_radio.power()
    advanced_remote_for_radio.volume_up()
    advanced_remote_for_radio.volume_down()
    advanced_remote_for_radio.mute()
    advanced_remote_for_radio.power()
