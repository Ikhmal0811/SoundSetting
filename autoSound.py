import keyboard
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

# List of output devices to toggle between
DEVICES = ["Fantech Tamago WHG01", "Speakers"]  # Replace with your device names
current_device_index = 0

def switch_audio_output(device_name):
    session = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "Audiodg.exe":
            interface = session._ctl.QueryInterface(ISimpleAudioVolume)
            interface.SetMute(0, None)  # Unmute the device
            print(f"Switched audio output to {device_name}")

# Function to toggle between devices
def toggle_audio_output():
    global current_device_index
    current_device_index = (current_device_index + 1) % len(DEVICES)
    switch_audio_output(DEVICES[current_device_index])


# Set up keyboard shortcut
keyboard.add_hotkey("win+`", toggle_audio_output)

print("Press win+` to toggle audio output devices. Press Esc to exit.")
keyboard.wait("esc") 