# Instructions for getting started with Streamlit, NOT for using this repo

## Things you will need:
1. Python
* The Anaconda distribution is a nice way to download Python and lots of other common libraries for working with data. We'll need a few other libraries off the bat (like `venv` and `pip`) but those will come with the Anaconda distribution.
2. Some understanding of using the command line / terminal
* This demo is made for UNIX-like (basically Linux/OSX) systems. There are some differences in using the Windows command line. Production systems are built on Linux, so it's good to get used to UNIX-like environments.
3. A decent text editor for writing code. I like Sublime Text(more lightweight) and Atom (more all-in-one).

## Set up a project directory
1. Open up a terminal. You should be now in your home directory, where directories like "Documents" and "Downloads" are. 
* Double check this by typing `ls`. You will see the contents of this directory printed out. 
2. We're going to make our example directory here, under the home directory. 
* Enter the command `mkdir streamlit-example`. This will make a directory (hence the name `mkdir`) called `streamlit-example`
* If you're like me, you will develop a habit of running `ls` constantly. Try running `ls` now and you will see that your new directory has been created. 
3. Enter the directory by running the command `cd streamlit-example`. In case you're curious, `cd` means 'change directory'!

Now we're in our project folder. Let's get to work. 

## Set up your virtual environment

0. Open a terminal and navigate to the project directory, if you aren't already in it. 
1. Run the command `python -m venv env` . This will create a *virtual environment* in which we will install the necessary packages for our project. There are many benefits of using virtual environments! Here are a few:
	* Ensuring that collaborators can run your code. For our current setup, we can create a recipe for our environment with a file called `requirements.txt`. Then, someone else can create an environment from that file and make sure they have all the same libraries that you used!
	* Using multiple versions of libraries. For example, you might find yourself working on one project written in Python 2 and another one in Python 3. There are fundamental incompatibilities between these major versions of Python. With virtual environments, you can easily maintain different versions of Python (or other libraries) and keep them contained within the appropriate project.
2. If you type `ls` now, you'll see that we now have a directory called `env`. That contains everything for our virtual environment. We're going to *activate* that environment by entering the command `source env/bin/activate`. Now, you will notice that `(env)` shows up in the beginning of each line in your terminal prompt. 
3. It's time to install the necessary packages. We only need a few basic packages for this example. Run the command `pip install streamlit pandas openpyxl watchdog`. This will run for a little while as it downloads and installs those liraries and all of their dependencies. **Note: `pip` versions?**
4. Let's take a look at all the libraries we just installed. Run the command `pip freeze` and you'll see everything printed out in the form `{library}=={version}`. Let's put all this information into a `requirements.txt` file. Run the command `pip freeze > requirements.txt` to *pipe* the output of `pip freeze` into a new file. If you open `requirements.txt`, you will see the same output we saw in the terminal. 

## Set up your Streamlit app!
Let's check that streamlit is working. Run the command `stramlit hello`. This start a demo Streamlit app on your local machine, and it may open a browser window to that app. If it doesn't, then open a browser and enter the URL `localhost:8501`. This is the port Streamlit defaults to, but you can change the port if you ever want/need to. Look around this app a bit, if you'd like. 
