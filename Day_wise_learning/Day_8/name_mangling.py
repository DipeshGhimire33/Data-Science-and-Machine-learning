class SmartDevice:
    """Represent a generic smart device."""

    def __init__(
        self,
        device_name: str,
        firmware_version: str,
        system_key: str,
    ):
        """Initialize a smart device."""
        self.device_name = device_name
        self._firmware_version = firmware_version
        self.__system_key = system_key

    def get_device_status(self) -> None:
        """Display the device name and firmware version."""
        print(
            f"Device name: {self.device_name}, "
            f"Firmware version: {self._firmware_version}"
        )


class SmartCamera(SmartDevice):
    """Represent a smart camera."""

    def __init__(
        self,
        device_name: str,
        firmware_version: str,
        system_key: str,
        video_resolution: str,
    ):
        """Initialize a smart camera."""
        super().__init__(device_name, firmware_version, system_key)
        self.video_resolution = video_resolution

    def exploit_test(self) -> None:
        """Demonstrate that the private attribute is not directly accessible."""
        print(self.__system_key)

    def display(self) -> None:
        """Display the camera details using name mangling."""
        print(
            self.device_name,
            self._firmware_version,
            self._SmartDevice__system_key,
            self.video_resolution,
        )


if __name__ == "__main__":
    camera = SmartCamera(
        "Living Room Cam",
        "014B",
        "044C#1f",
        "1080p",
    )

    camera.get_device_status()

    try:
        camera.exploit_test()
    except AttributeError as error:
        print(f"AttributeError caught: {error}")

    print(
        "Accessing __system_key via name mangling:",
        camera._SmartDevice__system_key,
    )