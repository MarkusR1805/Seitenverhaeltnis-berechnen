<div align=center><h1>Seitenverhältnis berechnen</h1></div>
<p align="center">
  <img src="https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/a10229e3-12ae-46d7-a22a-b53bf81b76e9/original=true,quality=90/37638528.jpeg" />
</p>
 
```sh
pip install gradio
```

or

```sh
pip install --upgrade gradio
```

## You need Python 3.10, 3.11 or 3.12!

Start with Python

```sh
python main.py
```

Update the Programm

```sh
git pull
```

To calculate an aspect ratio a value is needed and the aspect ratio, for example 16:9. Suppose you have the measure for the height of 1024px, then you don't know the measure for the width.<br>
The solution is actually simple: 1024px / 16 = 64px<br>
64px * 9 = 576px<br>
This is then 1024 high and 576 wide<br>
Enter either height or width, choose your aspect ratio 16:9 or 9:16, 3:2 or 2:3 and the program calculates the value you are looking for