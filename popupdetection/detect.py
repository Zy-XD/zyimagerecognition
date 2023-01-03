import pyautogui
import argparse
from time import sleep, time
import os

global image_to_detect
image_to_detect = None

global popup_action
popup_action = 0

global task_to_kill
task_to_kill = None

def main():

    print ("ZyImageRecognition - Pop-Up Detection")

    #CLI Features
    parser = argparse.ArgumentParser(
        prog='ZyImageRecognition - Pop-Up Detection',
        description='Detects given image on screen',
        epilog='')
    
    parser.add_argument('-p', '--path', help="Path to image being detected", required=False)
    parser.add_argument('-a', '--action', type=int, help="Determine action upon detection", required=False)
    parser.add_argument('-t', '--task', help="Task to kill - Action 0", required=False)

    args = parser.parse_args()

    try:
        if args.path is not None:
            image_to_detect = args.path
    except:
        None

    if image_to_detect is None:
        script_dir = os.path.abspath(os.path.dirname(__file__))
        image_to_detect = script_dir + "..\\image\\" + "image.png"
    
    print("Image to detect: {}".format(image_to_detect))
    
    try:
        if args.action is not None:
            popup_action = args.action
    except:
        None

    try:
        if args.task is not None:
            task_to_kill = args.task
    except:
        None
    
    print("Settings: Action - {}".format(popup_action))

    sleep(1)

    print("Initializing...")
    
    sleep(1)

    detector()

    sleep(1)

    print("Commencing Action {}...".format(popup_action))

    sleep(1)

    action(popup_action)

def detector():
    popup = None
    while popup is None:
        popup = pyautogui.locateOnScreen(image_to_detect, grayscale=False)
    print("Image Detected!")

def action(act=0):
    switcher = {
        0: killtask()
    }
    key = act
    switcher.get(key, "default")

def killtask():
    if task_to_kill == None or task_to_kill == "":
        raise Exception("Task to kill not specified")

if __name__ == "__main__":
    main()