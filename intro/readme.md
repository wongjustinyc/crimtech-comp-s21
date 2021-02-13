# Project 1: Intro

## Welcome to GitHub!
GitHub's pretty cool, and without it thecrimson.org might not even exist as we know it. The first thing you should do is [make an account](https://github.com/join) (if you haven't already); having an account will allow you to a) work on the projects and b) contribute to the Crimson's codebase later on when you graduate from this comp.

### Adding an SSH key
The first step to using GitHub is to add an ssh key to your account. If you don't know what an ssh key is, follow these instructions.

We need to link the account you just made to your local machine. The ssh key is like the identity of a computer, and it is how GitHub knows whether to trust your machine.

In your terminal, run the command `ssh-keygen` and hit Enter a few times, leaving the files blank. Then, run `cat ~/.ssh/id_rsa.pub`. You should get a string that goes `ssh-rsa [a bunch of characters]`. Copy it.

Go to github.com, click on your user and go to Settings. Click on `SSH and GPG keys` and click on `New SSH key` and paste the key you got into there.

### Fork this repo
Come back to [https://github.com/crimtech/crimtech-comp-s21](https://github.com/crimtech/crimtech-comp-s21). You should see a button on the upper right called "Fork". Click it! Now, you should have your personal copy of this repository.

Next, you need to **clone** this repository onto your machine. Go back to the home directory of the repo and click on the green `code` option to the upper-right and copy the URL given there. Then, in your terminal, navigate to your desired destination using `cd` and type in `git clone [the url you just received]`. Don't close your terminal yet, we'll need it later!

If you get an error, chances are the SSH key step didn't work. **Ask us for help if this happens.**

## Installation Time

We will now install 3 tools: Git, Python and pip.
1. Git (not to be confused with GitHub) is how you'll submit your assignments. It's a version control system that allows multiple people to work on a single piece of software, and it does that by keeping a record of all the changes that have been made to the source code along with who made them and when. GitHub, on the other hand, is an online service where people typically host their repositories.
2. Python is a popular programming language. Its syntax is very similar to pseudo-code, which enhances its readability and makes it a good choice for beginners. In the next project, you'll use Python to create a simple game of snake.
3. `pip` is the Python package manager; installing packages allows you to do tons of cool things with Python that you wouldn't otherwise be able to do.

### Install Git
Open up your terminal and type in `git --version`. If you get an error, you need to install Git. Follow the instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to install it.

### Install Python
In your terminal, type in `python3 --version`. If you get an error, you need to install Python 3: follow the instructions below.

- If you're using MacOS, you should check out `homebrew`, which is a really useful package manager. The instructions for getting Python with homebrew are [here](https://docs.python-guide.org/starting/install3/osx/). Alternatively, you can download Python from the [website](https://www.python.org/downloads/).
- If you're using Linux, you can download Python 3 from the [website](https://www.python.org/downloads/), or use `sudo apt-get install python3.7`.

### Install `pip`
In your terminal, type `pip --version`. If you get an error, you need to install `pip`. Follow the instructions [here](https://pip.pypa.io/en/stable/installing/).

## Choose a ~~Pokémon~~ Text Editor!
In order to edit files, you'll need some kind of text editor. Popular options include **[VSCode](https://code.visualstudio.com/)**, [Sublime Text](https://www.sublimetext.com/), and [Atom](https://atom.io/), though you can (technically) also use the built-in text editing software like TextEdit for Mac or Notepad for Windows. We don't recommend that though, since you'll miss a lot of features that come with more modern text editors).

### Fill out intro.txt
Using whichever editor you want, fill out the questions in `intro.txt`!

## Making a Commit
Time to make a commit! First, run `git status` in your terminal. This will show you all the files you have changed in the directory.

Run the command `git add -A`, then `git commit -m "Submit intro"` You should get something that goes `[master ******] Submit intro...`.

At this step, Git may ask you to set your username/email. If so, follow those instructions or call us over.

## Push the commit
The change you just made is still living on your local machine. How do you upload them to GitHub?
Run the command `git push`. Then, go onto your github repository. You should see some changes there!

## Submit
There should be a button now called "pull request" or "make pull request". Click on it!

Put in a title and a description, which can be anything you want. Then, hit "open pull request" or something like that.

Once that's done, you are done! Congratulations on finishing your first lab :D
