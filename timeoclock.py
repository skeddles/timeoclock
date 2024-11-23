import os
import sys
import time
from playsound import playsound 

# Determine the base path for the executable
if getattr(sys, 'frozen', False):  # If the script is running as an executable
    base_path = sys._MEIPASS  # PyInstaller sets this to a temporary folder
else:
    base_path = os.path.abspath(".")  # Otherwise, use the current working directory

# Path to the audio file, now at the root level of the bundled files
sound_file = os.path.join(base_path, "bitty.mp3")
chime_interval_minutes = 30  # Set your chime interval here

def chime():
    print(f"Chime program started. Will chime every {chime_interval_minutes} minutes starting from the next hour.")
    playsound(sound_file)

    # Wait until the top of the next hour
    current_time = time.localtime()
    seconds_until_next_hour = (60 - current_time.tm_min) * 60 - current_time.tm_sec
    time.sleep(seconds_until_next_hour)

    # Start the regular chime intervals
    while True:
        # Play the chime sound
        playsound(sound_file)

        # Sleep for the interval specified
        time.sleep(chime_interval_minutes * 60)

if __name__ == "__main__":
    chime()