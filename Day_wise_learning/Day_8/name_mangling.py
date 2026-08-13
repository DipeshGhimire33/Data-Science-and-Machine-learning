class SmartDevice():
    def __init__(self, device_name, attribute_firmware_version, system_key):
        self.device_name = device_name
        self._attribute_firmware_version = attribute_firmware_version
        self.__system_key = system_key

    def get_device_status(self):
        print(f"Device name is {self.device_name} and version is {self._attribute_firmware_version}")
    
    

class SmartCamera(SmartDevice):
    def __init__(self, device_name, attribute_firmware_version, system_key, vid_resoln):
        super().__init__(device_name, attribute_firmware_version, system_key)
        self.video_resolution = vid_resoln
        
    def exploit_test(self):
            # Attempt to access the private attribute directly
            print(self.__system_key)  # This will cause AttributeError outside the class

    def display(self):
        # Accessing the "private" attribute __system_key
        print(self.device_name, self._attribute_firmware_version, self._SmartDevice__system_key, self.video_resolution)

# External testing block
if __name__ == "__main__":
    # Instantiate the camera
    cam = SmartCamera("Living Room Cam", "014B", "044C#1f", "1080p")
    
    # Call inherited method
    cam.get_device_status()
    
    # Call the exploit_test method (which will raise AttributeError)
    try:
        cam.exploit_test()
    except AttributeError as e:
        print(f"AttributeError caught: {e}")

    # Access the private attribute using name mangling
    print("Accessing __system_key via name mangling:", cam._SmartDevice__system_key)