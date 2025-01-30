# import keyboard
# import subprocess

# # Device IDs (Replace with your actual IDs)
# DEVICES = {
#     "headphones": "{0.0.0.00000000}.{03bbbc17-f182-4035-a9dd-d537b61ac203}",
#     "speakers": "{0.0.0.00000000}.{57b8d666-2a88-4743-8cb9-679802db3f6e}"
# }
# current_device = "headphones"  # Start with headphones

# def switch_audio_output():
#     global current_device
#     new_device = "speakers" if current_device == "headphones" else "headphones"
#     device_id = DEVICES[new_device]

#     try:
#         print(f"Switching to {new_device}...")
#         subprocess.run(
#             ["powershell", "-Command", f"Set-AudioDevice -ID {device_id}"],
#             capture_output=True,
#             text=True
#         )
#         print(f"Switched to {new_device}!")
#         current_device = new_device
#     except Exception as e:
#         print(f"Error switching audio: {e}")

# # Set up keyboard shortcut
# keyboard.add_hotkey("Ctrl+`", switch_audio_output)

# print("Press Ctrl+` to toggle audio output devices. Press Esc to exit.")
# keyboard.wait("esc")

# import keyboard
# import subprocess

# # List of output devices to toggle between
# DEVICES = ["Headphones", "Speakers"]  # Replace with your device names
# current_device_index = 0

# def switch_audio_output(device_index):
#     """Switches the default audio output device using PowerShell."""
#     try:
#         command = f"Set-AudioDevice -Index {device_index}"
#         subprocess.run(["powershell", "-Command", command], check=True)
#         print(f"Switched to device {device_index}!")
#     except subprocess.CalledProcessError as e:
#         print(f"Error switching audio device: {e}")

# # Function to toggle between devices
# def toggle_audio_output():
#     global current_device_index
#     current_device_index = (current_device_index + 1) % len(DEVICES)
#     switch_audio_output(current_device_index + 1)  # PowerShell index starts from 1

# # Set up keyboard shortcut
# keyboard.add_hotkey("Ctrl+`", toggle_audio_output)

# print("Press Ctrl+` to toggle audio output devices. Press Esc to exit.")
# keyboard.wait("esc")

import keyboard
import subprocess
import json

# List of output devices to toggle between (use exact names from `Get-AudioDevice -Playback`)
DEVICES = ["Headphones (Fantech Tamago WHG01)", "Speakers (Realtek(R) Audio)"]  
current_device_index = 0

def get_audio_device_index(device_name):
    """Finds the index of the given audio device by name."""
    try:
        command = "(Get-AudioDevice -List | ConvertTo-Json -Compress)"
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
        
        if result.returncode != 0:
            print("Error getting audio devices:", result.stderr)
            return None
        
        devices = json.loads(result.stdout)
        
        if isinstance(devices, dict):  # If there's only one device, PowerShell returns a dict instead of a list
            devices = [devices]
        
        for device in devices:
            if device_name.lower() in device["Name"].lower():
                return device["Index"]
        
        print(f"Device '{device_name}' not found!")
        return None
    except Exception as e:
        print(f"Error getting device index: {e}")
        return None

def switch_audio_output(device_name):
    """Switches the default audio output device using PowerShell by name."""
    device_index = get_audio_device_index(device_name)
    if device_index is not None:
        try:
            command = f"Set-AudioDevice -Index {device_index}"
            subprocess.run(["powershell", "-Command", command], check=True)
            print(f"Switched to {device_name}!")
        except subprocess.CalledProcessError as e:
            print(f"Error switching audio device: {e}")

def toggle_audio_output():
    """Toggles between the predefined audio devices."""
    global current_device_index
    current_device_index = (current_device_index + 1) % len(DEVICES)
    switch_audio_output(DEVICES[current_device_index])

# Set up keyboard shortcut
keyboard.add_hotkey("Ctrl+`", toggle_audio_output)

print("Press Ctrl+` to toggle audio output devices. Press Esc to exit.")
keyboard.wait("esc")
