# marchenko_OT
Project for "Objectove technologie"

## **1. Welcome**

The game is designed to pass the exam on the subject of game creation. In which there are various functions, methods used to better implement the game. Which will show my knowledge gained from this subject.
### **1.1 Player experience**

Try to survive. You need to avoid collisions of falling objects in space, and any opportunity to find a way out, for this there is an opportunity to kill opponents. There is an opportunity to move around the map, and have reinforcements that gives the opportunity to survive much longer.

### **1.2 What has been used**

**Pygame** - programming language

**Pycharm** - game writing (IDE)

**Pages** - sounds, objects  

---
## **2. Conception**
### **2.1 Gameplay**

The player chooses an airplane that he or she likes. His task is to survive or dodge a falling meteorite or ship. The player can move the airplane as he wants and can feel how he controls it. In addition to meteorites will fall Boosts, which will give privileges to survive longer. The game has no end, you just play for the best score, which gives you the opportunity to compete with friends and make the evening more interesting.

### **2.2 Interpretation**

_Meteor Shower_ - your airplane flies and meets with difficulties, it falls objects that can take its life. Your task in every possible way to facilitate the path of the plane up, because there is a laser that you shoot. On your way will meet objects that can help you in strengthening your airplane. But just try to distract yourself, your airplane will crash!

### **2.3 Mechanic**

**_Opponents:_**

From above appear different kinds of objects, like meteorites, and hit ships that fall.

**_Bonus:_**

From above will fall as well as three types of boosts that can increase your strength, speed, or vulnerability. To understand what and how to play !

**_Bugs:_**

Opponents spawn behind the screen area, this prevents you from shooting at them beforehand, as the laser disappears as soon as you reach the top edge of the game.

**_Elimination:_**

Eliminating players with a laser that on impact takes one enemy life

### **2.4 Classes** 
_Main:_
```
class, in which the game startup and menu operation is located.
```
_Game:_
```
class, which contains the main game logic, relations between objects and object creation.
```
_Character:_
```
class in which the character's logic and actions reside.
```
_Enemy:_
```
class in which the enemie's logic and actions reside
```
_EnemyLaser:_
```
class in which settings laser for enemy
```
_Boost:_
```
class in which the boost's logic is located, and the boost is drawn out
```
_Score:_
```
class in which the score's logic is located, and the score is drawn out
```
_Explosions:_
```
class in which the explosion's logic is located, and the explosion is drawn out
```
_Background:_
```
class in which the background's logic is located, backdrop star work.
```
_Hud:_
```
working with menu buttons and display.
```
_Button:_
```
working with buttons for menu and choose character
```
_Stars:_
```
elements for background animation
```
---

## **3. View**

### **3.1 Attractiveness** 

The game was created as a 2D game where free Sprite objects were used. There were taken a choice of 3 airplanes for which the player will have to play. 3 kinds of meteorites and 3 kinds of falling ships that will try to shoot down our airplane.

<p align="center">
  <img src="https://github.com/mrudnit/marchenko_OT/blob/main/assets/enemy1.png" alt="Opponents">
  <br>
</p>

### **3.2 Design** 

The goal was to create a 2D game with the look of an RPG and pixels
Created only one level that changes and runs randomly

_There is a picture attached at the bottom:_

<p align="center">
  <img src="https://github.com/mrudnit/marchenko_OT/blob/main/project.png" alt="View">
  <br>
</p>

___
## **4. Media Files**

Media files were taken from all available sites with both short and long audio files: <sup>https://zvukipro.com</sup>. 

_The sounds have been picked up in the style of a rpg pixel game, giving the game a chance to turn into a deeper meaning and interest._

---

## **5. Game experience**

### **5.1 Game interface**

The user has a menu in which he can choose an airplane to his taste, and start the game. Also learn about what to do and what each superpower means, that is a brief description of the game.

### **5.2 Contorls**

_Keyboard_
```
~ WASD: player movement
~ Arrows: alternative for player movement
```
_Mouse_
```
~ Left mouse button airplane shooting
```

---

## **6. Author**

This repository was made for the purpose of handing in a project on <ins>Objectove technologie</ins>. This project contains Meteor Shower game files, which I worked with to develop the game. It is safe to say that there is no plagiarism in these files.

_Author : Maksym Marchenko_

_Topic : One level that changes every time (RPG)_
