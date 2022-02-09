# python-wordle-solver
Welcome to my Wordle Solver! Quickly guess the wordle of the day between three to five attemtps!


## About Wordle
Wordle is a word game reminiscent of mastermind. The player tries to guess a five letter word within six attempts. After each attempt, hints are given. Green tiles show that the letter is in the right position. Yellow tiles indicate that the letter is in the word but in the wrong spot. Grey tiles show that the letter is not in the world. Words a 5 lettered and only a maximum of six attempts are allowed. 
![Wordle Interface](https://user-images.githubusercontent.com/44172551/153125873-dfa25c5d-b8b4-4fce-83a0-b98345c47299.png)

## Installing Dependencies 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required dependicies found in ```requirements.txt```.

```pip install -r requirements.txt```
## Launching Instructions 
1. Open a console
2. Create a vitual enviroment 
3. Install the dependiences 
4. Run the following command ```python3 solver.py``` in the console 
5. Follow the instructions 
6. Enjoy!

## Operating the Solver
1. Open Wordle and Run ```solver.py``` side by side.
2. A sequence of 15 words should appear in the console. These are the words that have the highest commonality value ranging from 0 to 1. The higher the value, the higher the chance it is to have a letter in the daily wordle.
3. Choose a word from the list and enter it into the Wordle Puzzle.
4. Enter the cooresponding output. ```G``` or ```1``` for green tiles, ```Y``` or ```2```  for yellow tiles, and ```?``` or ```3``` for grey tiles. Hit Enter. 
5. Another sequence of words sorted by their commonality values will appear. Choose one and repeat steps 3 and 4 until the Wordle is correctly guessed. 



## Variables 

There are options available to customize the solver

- The word list can be changed by altering the ```words.txt``` file in the data folder. However, its name and path must be ```data/words.txt```
- The length of word can be changed depending on the the size of the board. The default is set to ```5```. This can be changed by altering the ```word_len``` variable in the ```wordle.py``` file. Note that the words in the ```words.txt``` only inlcude five letter words, which are standard to wordle
- The number of attempts can also be altered by changing the ```max_attempt``` variable in ```wordle.py```
- The set of legal characters can also be altered by changing the ```legal_char``` variable in ```wordle.py```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Development References 
- [Unicode](https://unicode-table.com/en/1F389/)
- [Unicode Emoji Guide](https://www.geeksforgeeks.org/python-program-to-print-emojis/)
- [Parsing and Solving Algorithms](https://www.inspiredpython.com/article/solving-wordle-puzzles-with-basic-python)
- [Colored Console Output](https://stackoverflow.com/questions/37340049/how-do-i-print-colored-output-to-the-terminal-in-python/37340245)
