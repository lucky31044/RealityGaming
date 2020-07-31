## Description
With covid everyone is locked in their homes at this time I thought of learning new skills and making some fun projects .I worked on a concept I called  “Reality Gaming” . 
It is simply controlling games with our movements .I used object tracking using opencv for this Project and PyAutoGUI for the key press.
This can be used to control any game with a set of keys we want to use for control.
Game concept is first we mark the object we want to track then in code we have divided our screen area into left ,right, up,down and neutral for the specific key press we want .Now whenever our tracking object moves to left with help of PyAutoGUI  left key is pressed similarly for other keys .
In the later session I will explain everything with code.
Their are various trackers available in opencv to track the movement .
BOOSTING Tracker
KCF Tracker
MIL Tracker
TLD Tracker
MEDIANFLOW Tracker
GOTURN tracker
MOSSE tracker
CSRT tracker
 
The main tradeoff between all these trackers is speed and accuracy ,i.e. the frame rate it can provide and accuracy it can track objects with.
The one I used was MOSSE which provided a very high frame rate it can support upto 450fps and the second one is CSRT which has comparatively lower fps (25 fps) but gives higher accuracy for object tracking.
 
Libraries used
# opencv
# pyautogui

##  links:
Subway surfer https://www.kiloo.com/subway-surfers/
Temple run https://m.plonga.com/adventure/Temple-Run-2-Online-Tablet

