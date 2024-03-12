import pyautogui
import time

def send_text_as_typing(text):
    # Give some time to switch to the text box after running the script
    time.sleep(5)
    
    print("starts now")

    # Type the text with a small delay between each character
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(0.004)  # Adjust this delay if needed
    
    print("finished")

if __name__ == "__main__":
    # Replace 'Your Text Here' with the text 
    send_text_as_typing("this will be typed in the text box like a human typing it out.")
