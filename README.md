<h1>Mini Game Suite</h1> 

This project is a Python-based Mini Game Suite that includes three fun games:

<li>Hangman (CLI-based word guessing game)</li>
<li>Scribble (Scrabble-inspired word creation game with scoring)</li>
<li>Rock, Paper, Scissors (GUI-based with Tkinter and Pygame)</li>


<h2>Features</h2>
<h3>Hangman:</h3>
  
<ul>Random word selection</ul>
<ul>ASCII art for hangman stages</ul>
<ul>Guess-by-letter or whole word</ul>
<ul>Replay option</ul>

<h3>Scribble:</h3>

<ul>Simulates a Scrabble-style letter draw</ul>
<ul>Dictionary-based word validation (NLTK)</ul>
<ul>Letter scores and total score tracking</ul>
<ul>Background music (Pygame)</ul>

<h3>Rock, Paper, Scissors:</h3>

<ul>GUI interface using Tkinter</ul>
<ul>Player vs Computer logic</ul>
<ul>Score tracking to 5 points</ul>
<ul>Fullscreen win/lose/draw animations</ul>
<ul>Background music and sound effects (Pygame)</ul>

<h2>Requirements</h2>
<ul>Python 3.x</ul>

<h2>Packages</h2>
<li>pygame</li>
<li>tkinter (usually included with Python)</li>
<li>nltk</li>
<li>tkvideo (optional, if using video splash screens)</li>
<li>PIL (optional, if using ImageTk)</li>

<h2>To install dependencies</h2>

<li>pip install pygame nltk tkvideo pillow</li>
<li>Also, download the NLTK word corpus:</li>
<ul>
  
</ul>

    import nltk
    nltk.download('words')

<h2>Folder Structure</h2>
  
Ensure the following assets are available at the specified paths:
```
C:/jenitemp/
├── rock.png
├── paper.png
├── scissor.png
├── win.png
├── lose.png
├── draw.png
├── win_sound.mp3
├── lose_sound.mp3
├── draw_sound.mp3
├── where-the-light-is-15702.wav
You can change the paths in the code to point to your custom asset folder.
```

<h2>How to Run</h2>
bash
python main.py
  
You will be prompted to choose between:
<p>
  Hangman (1) <br>
  Scribble (2) <br>
  Rock Paper Scissors (3) <br>
  Exit (4) <br>
</p>

<h2>Notes</h2>
  
<li>The Hangman and Scribble games run in the terminal.</li>
<li>The Rock, Paper, Scissors game opens a GUI window.</li>
<li>You can modify the word list in words.py or customize your own set.</li>
<li>This project is a fun exercise in combining CLI games with GUI-based interaction using Tkinter and Pygame.</li>

<h2>License</h2>
This project is open-source and available under the MIT License.










