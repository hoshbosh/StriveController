# Strive Controller
This is a library written in Python that uses Vgamepad to allow users to control the training dummy in the training room using code, in Guilty Gear Strive

## Goal
The eventual goal is to make an reinforcement learning model to allow a bot to improve at GGST. This is just an attempt to allow the output(or action) aspect of that goal. An input project will begin shortly

## Installation and setup
1. Clone the repository
2. Run
```
cd StriveController
pip install ./requirements.txt
```
3. Open GGST and navigate to the training room
4. Set the dummy to control by controller
5. Run
```
python ControllerTest.py
```
6. Then tab back into the training room
In the Utils/Inputs.py file, you can modify the controls of the bot, this changes by user

## To Do
- [ ] Finish all characters command lists
- [ ] Make a more user friendly interface to change controls
- [ ] Use computer vision to make the input part of the RL model
