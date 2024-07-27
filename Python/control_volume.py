pip install pycaw comtypes


from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_volume(volume):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
    volume_interface.SetMasterVolumeLevelScalar(volume, None)

if __name__ == "__main__":
    try:
        volume = float(input("Enter volume level (0.0 to 1.0): "))
        if 0.0 <= volume <= 1.0:
            set_volume(volume)
            print(f"Volume set to {volume * 100}%")
        else:
            print("Please enter a value between 0.0 and 1.0.")
    except ValueError:
        print("Invalid input. Please enter a numeric value between 0.0 and 1.0.")






