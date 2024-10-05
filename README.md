<div align=center><h1>Seitenverhältnis berechnen</h1></div>
 
````
pip install gradio
````
or
````
pip install --upgrade gradio
````
You need Python 3.10, 3.11 or 3.12!

Start with Python
````
python main.py
````

Update the Programm
````
git pull
````
To calculate an aspect ratio, a value is required and the aspect ratio, for example 16:9.
Assuming you have the dimension for the height of 1024px, you do not know the dimension for the width. The solution is actually simple:
1024px / 16 = 64px
64px * 9 = 576px
This is then 1024 high and 576 wide

Enter either height or width, select your aspect ratio 16:9 or 9:16, 3:2 or 2:3 and the program will calculate the value you are looking for