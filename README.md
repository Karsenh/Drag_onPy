# Drag_onPy

---
## Undetected Mobile Botting Software
(requies Bluestacks 5 Emulator)


### Requirements
1. Must have Permanent XP drops enabled in OSRS Client settings
2. DO NOT adjust Mini-map zoom (turn minimap zoom off)
3. Must start scripts on specified start-tiles



### [ 50+ ] Total Scripts



### Anti-Ban:
1. Human Mouse Movement
    
    Organic, randomized, mouse trajectories and x, y click deviations
2. Automatic interface normalization (camera pitch, yaw, and zoom adjusting, active tab detection, location detection, etc.)


![Alt Text](https://gyazo.com/90eeace3cc27c53979ed06a67a7954b5.gif)


## Generating .exe:
1. Delete build, dist, main.spec and output directories
2. Start instance of Anaconda (terminal) with Python 3.10+
3. `pip install -r requirements.txt` if any new packages have been added
4. `pip install auto-py-to-exe` if not already installed
5. `pyinstaller --onefile main.py` to create Build directory within project folder
6. `auto-py-to-exe` to start Auto-Py-To-Exe application
7. Import JSON config settings and convert to exe
8. (or) Manually configure based on following:
9. ** NOTE (not shown in image) Must include in "Hidden imports" - "pyautogui" & "pywintypes"
10. After .exe is built - move from output (click open output dir in py-to-exe) into output dir within this project
11. Once .exe from auto-py-to-exe is in the output dir of this project, start Inno
12. Use the Inno script in the 'Misc' dir within this project to create Inno setup Exe (which automatically grabs the .exe from the output dir in this proejct)

---


## Uploading Installation Media to AWS Bucket

1. Navigate to AWS dragonpy bucket containing the installation media: https://s3.console.aws.amazon.com/s3/buckets/dragonpy?region=us-west-2&tab=objects
2. Update the installation media
3. Match the name on the Front-End (Client) in the .env variables

---

## Updating Web App

1. Copy everything from client directory of working (dev) dir except for node_modules into Heroku client dir
2. Copy everything from root dir (server) except for node_modules
3. open bash terminal in root heroku dir
4. run command `git add .` followed by `git commit -m "<message>"` and finally `git push heroku master` to push web app updates to heroku
