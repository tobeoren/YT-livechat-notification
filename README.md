---

# YouTube Live Chat Notification

## Introduction
This program is designed to monitor YouTube live chat and play a notification sound whenever a new message is received. It allows users to adjust the volume of the notification sound using keyboard shortcuts. The application utilizes the `pytchat` library to fetch live chat messages and the `pygame` library to handle audio playback.

## Features
- **Live Chat Monitoring**: Continuously listens for new messages in a specified YouTube live chat.
- **Audio Notification**: Plays a sound notification each time a new message arrives in the chat.
- **Volume Control**: Users can easily adjust the notification sound volume using keyboard shortcuts:
  - Press `[` to decrease the volume.
  - Press `]` to increase the volume.
- **User-Friendly Console Display**: Provides a clear console output of chat messages and volume changes.

## Getting Started
Follow these steps to run the program:

1. **Install Required Libraries**: Ensure you have Python installed on your system. Install the necessary libraries using pip:
   ```bash
   pip install pytchat pygame rich keyboard
   ```
   
2. **Prepare Audio File**: Download an audio file for notifications (e.g., `notifikasi.mp3`) and save it in the same directory as the script.

3. **Run the Program**:
   - Open your terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script using:
     ```bash
     python your_script_name.py
     ```
   - Enter the YouTube `video_id` when prompted. The `video_id` is part of the URL of the YouTube live stream. For example, in `https://www.youtube.com/watch?v=DZ0hf7sKP4g`, the `video_id` is `DZ0hf7sKP4g`.

4. **Enjoy Monitoring**: The program will now start monitoring the live chat. You will see messages printed in the console, and you can control the volume as needed.

## Requirements
To run this program, ensure you have the following:

- Python 3.x installed on your machine.
- The following Python libraries:
  - `pytchat`: For accessing YouTube live chat.
  - `pygame`: For audio playback.
  - `rich`: For better console output formatting.
  - `keyboard`: For detecting key presses.

Make sure to have a compatible audio file in the specified format for notifications.

---

Feel free to modify any part of the guide to suit your preferences!
