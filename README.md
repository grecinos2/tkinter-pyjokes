# tkinter-pyjokes
This repository contains an exercise for a course I am taking on Udemy, The Complete Python Developer.  Specifically an exercise on Tkinter and Pyjokes

My original plan was to make a Python app that displays a rotating wheel that stops at a random location.  Subsequently, displaying a PyJoke based on the
location it stopped on.  As I was coding the GUI interface, animation was limited.  So, I went with a simpler design.  I ended up creating a set of 3x3
"tiles".  Upon clicking on the "Go!" button, the game randomly cycles through the tiles and displays a PyJoke based on the tile that the game lands on.
I implemented sound effects, thus the need for the pygame library.

Feel free to download it, modify, learn, and of course have fun with it!

It requires the following libraries:
* tkinter
* pygame
* random
* pyjokes

Usage:  python .\tkinter_pyjokes.py

Note:  If it doesn't work, you may need to use Python 3.12 to get it to work. Specifically while installing the pygame library.
