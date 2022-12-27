# Pomodoro Timer

##### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)

---

<p float="center">
    <img src="https://github.com/SDBranka/Pomodoro_Timer/blob/main/Resources/Screenshots/Start_screenshot.png" width=22% alt="start image"/>
    <img src="https://github.com/SDBranka/Pomodoro_Timer/blob/main/Resources/Screenshots/Work_screenshot.png" width=22% alt="work image"/>
    <img src="https://github.com/SDBranka/Pomodoro_Timer/blob/main/Resources/Screenshots/Break_screenshot.png" width=22% alt="break image"/>
    <img src="https://github.com/SDBranka/Pomodoro_Timer/blob/main/Resources/Screenshots/LongBreak_screenshot.png" width=22% height=163 alt="long break image"/>
</p>

## Description

This app aids in a user's studying or working process by providing a timer based on Francesco Cirillo's Pomodoro Technique for improved performance and/or retention.

##### Controls
<ul>
    <li>The user should decide on a task to be performed and then click the Start button to begin the timer
        <ul>
            <li>The timer label will change to "Work" and begin to run for 25 minutes during which the user should be performing their designated task</li>
        </ul>
    </li>
    <li>After the 25 minute timer has run out
        <ul>
            <li>The app will pop out to the forefront of the screen
                <ul>
                    <li>Click anywhere on the window (except the close or reset button) to acknowledge and then resume working</li>
                    <li>Note: minimizing the window will prevent this from happening</li>
                </ul>
            </li>
            <li>The label will change from "Work" to "Break"</li>
            <li>A checkmark will be added to denote how many work cycles have been completed</li>
            <li>The app will present a 5 minute timer during which the user should take a break</li>
        </ul>
    </li>
    <li>The timer will run this cycle four times and then present the user with a 20 minute long break
        <ul>
            <li>At the conclusion of each long break the green work session check marks will be cleared and a red cycle check mark will be added</li>
        </ul>
    </li>
    <li>The timer and checkmarks may be reset at any time by clicking the reset button</li>
</ul>

##### Technologies

- Python
- Tkinter
- Visual Studio

---

## How To Use

Download or clone this repository to your desktop. Run main.py in an appropriate Python environment.

---

## References

##### Continuing Work on
- added cycle check mark function to the original program
- https://github.com/SDBranka/_100DOP_Exercises

\
[Back To The Top](#pomodoro-timer)