# Learn Calculus with Python

Hello! This repository contains supporting materials for the book *Learn Calculus with Python* by Nick McIntyre. The book is in production and will be published in early 2027 by the good folks at [No Starch Press](https://nostarch.com).

You can work through the entire book without downloading anything. All examples and exercises will run entirely in your web browser using the website [https://calculus.dev](https://calculus.dev). Many thanks to the alchemists behind the [JupyterLite](https://jupyterlite.readthedocs.io/en/stable/) project for making this possible!

If you prefer to work offline, the book uses a few Python packages that you can install on most computers running Linux, macOS, or Windows. Follow along with the steps below to get your local environment up and running.

## Download Data and Solutions

The book has over 200 exercises and you're encouraged to check your work against the solution set. The solutions are stored as text files (*.ipynb* and *.py* files). In Chapters 8 and 9, you'll apply calculus to analyze data stored in NumPy arrays (*.npy* files).

If you already know how to clone a git repository, then feel free to do so. Alternatively, you can download a copy of all the files stored here by clicking the green **Code** button above and then clicking the **Download ZIP** button. Then, unzip the folder somewhere on your filesystem and rename it from `learn-calculus-main` to `learn-calculus`. The *data* and *solutions* subfolders are laid out like so:

```sh
learn-calculus
├── data
    ├── audio
    ├── cpi
    ├── wdi
        ├── air_mortality.npy
        ├── child_mortality.npy
        ├── country.npy
        ├── food_insecurity.npy
        ├── maternal_mortality.npy
        └── wash_mortality.npy
    └── wrdb
└── solutions
    ├── ch1
    ├── ch2
    ├── ch3
        ├── calcplotlib.py
        └── solutions_ch3.ipynb
    ├── ch4
    ├── ch5
    ├── ch6
    ├── ch7
    ├── ch8
    └── ch9
```

## Installing Python

Install Python on your computer by following the instructions for your operating system at [https://www.python.org/downloads/](https://www.python.org/downloads/). Then, create a *virtual environment*, which is a folder containing a dedicated copy of Python along with the packages we'll use throughout the book: [JupyterLab](https://jupyter.org), [NumPy](https://numpy.org), and [ipycc](https://ipy.cc). 

On Linux/macOS, run the following commands in the Terminal application to set up your virtual environment:

```sh
cd /path/to/learn-calculus
python3 -m venv venv
source venv/bin/activate
pip install jupyterlab numpy ipycc
```

On Windows, run the following commands in the Terminal application instead:

```powershell
cd \path\to\learn-calculus
py -m venv venv
venv\Scripts\activate
pip install jupyterlab numpy ipycc
```

You can find the current version of these instructions on the Python Packaging User Guide at [https://packaging.python.org/en/latest/tutorials/installing-packages/](https://packaging.python.org/en/latest/tutorials/installing-packages/).

## Running JupyterLab

At this point, you're ready to launch JupyterLab by running the `jupyter lab` command. By default, JupyterLab will only send 1,000 messages (drawing instructions) per second to your web browser. Complex animations require lots of drawing instructions, so you'll probably need to raise this limit. Each time you open your terminal, run the following commands:

On Linux/macOS:
```sh
source venv/bin/activate
jupyter lab --ZMQChannelsWebsocketConnection.iopub_msg_rate_limit=1.0e10
```

On Windows:
```powershell
venv\Scripts\activate
jupyter lab --ZMQChannelsWebsocketConnection.iopub_msg_rate_limit=1.0e10
```

## A tale of two turtles

The Python language doesn't include drawing commands by default, so the book uses a version of the beloved [Turtle Graphics module](https://ipy.cc/turtle) that runs within a Jupyter notebook. Here's how we'll draw throughout the book:

```python
from ipycc.turtle import Turtle, showscreen

# Show the screen
showscreen()

# Create a Turtle
t = Turtle()
```

If you're working through the book offline, then you also have the option of using Python standard library's version of Turtle Graphics. Here's the modification you'll need to make:

```python
from turtle import Turtle, setup

# Connect the Jupyter and Turtle event loops
%gui tk

# Show the screen and resize the window to
# 400 x 400 with padding for scrollbars
setup(405, 405)

# Create a Turtle
t = Turtle()
```

When you see an import statement such as `from ipycc.turtle import Turtle, showscreen` in the book, that's your cue to use `from turtle import Turtle, setup` instead. The *magic command* `%gui tk` makes Jupyter play nicely with Turtle Graphics. It also opens a separate window on your computer to display drawings.

## Reporting Bugs

Find an error, bug, or opportunity to explain something more clearly? Please feel free to [open an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/quickstart)!

## License

The content in this repository is free to use under the terms of the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a>.
