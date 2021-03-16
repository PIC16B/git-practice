# Practice with git and GitHub

This is a very simple repository for practicing with git and GitHub. git is a utility for *version control*. When a body of code is tracked with git, it is easy to see how the software has evolved over time, to roll back changes when needed, and to incorporate modifications by multiple collaborators. 

GitHub is a free online code hosting service that runs using git. We'll use git and GitHub to collaborate on code and to host the blogs on which you'll submit your homework. 

## Preparation

You should already have made an account on [GitHub](https://github.com/) and downloaded [GitHub Desktop](https://desktop.github.com/). 

## 1. Fork

*Forking* refers to the act of creating your personal copy of an existing body of code. You can then modify your *fork* as you wish. Forking is a great way to make use of templates and other resources upon which you can build. For example, you'll soon fork a template for your website, which you'll then populate and customize. 

Go ahead and fork this repo, using the "Fork" button at in the top-right corner. 

Check out your fork! At the moment, it's just a copy of the [original repository](https://github.com/PIC16B/git-practice). 

## 2. Clone

You now have a copy of this repository on GitHub. But how can you make changes? It's possible to manually edit files on GitHub, but this is not at all convenient. Instead, you should create a *local clone* of the repository. To do this, hit the big green button and choose Open in GitHub Desktop. Choose to create the repo in a location where you'll easily remember it. 

## 3. Edit a File

In your local clone of the repository, open this file (`README.md`). At the top of the file, underneath the title, type 

> I'm \[your name\] and I edited this file! 

## 4. Add and Commit

Now go over to GitHub Desktop. Observe that the file `README.md` is now listed as changed. If there isn't already a blue checkmark beside the file, click the box to make one. 

Then, add a *commit message* in the box below. The commit message should be a short description of what you achieved with your code modification. For example, a good commit message here might be "Add name to README.md." Once you've entered the commit message, click the big blue Commit button. 

## 5. Create a Folder and a File

But wait -- let's get crazy. Make a new folder called `practice-folder` within the cloned repository. Then, create a Jupyter Notebook in this folder. Run the following code, obtaining a simple plot of a sine wave. 

```python
from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 1001)
y = np.sin(x)
f = plt.plot(x,y)
``` 

Make sure to save the resulting notebook. 

## 6. Add and Commit

Now, add (click the checkbox) beside your new notebook. Add an informative commit message, and commit the file. 

## 7. Push

Great, we've made some local changes! Our primary remaining task is to *push* our code back to GitHub. This will allow us to share our code with others. Additionally, pushing code to GitHub is the recommended way to update your own website. 

To push your code, just click the black "Push" button at the top right of GitHub Desktop. Before you click, you can notice that the button indicates the number of commits that you have made since your last push. After you click the button, you will have no more commits to push. 

## 8. Inspect on GitHub

Now go to the URL of your fork on GitHub and inspect the new `README.md` file. You can also take a look at the Jupyter Notebook you created. Note a nifty feature: by default, GitHub renders the Jupyter Notebook, so that you can see the plot you created. Your code is also shown in an attractive and readable format. 

## 9. Pull

What if there's a change made on GitHub that's not present in your local repository? This is a common situation when collaborating. Your partner made some cool improvement to the code that you would like to access. To do this, you need to *pull*. 

To practice pulling, we need to make a change on GitHub. For now, just edit the `README.md` file again, which you can do by navigating to this file and clicking the pencil icon. Add another sentence to the top of the file. Here's a good one:

> I'm \[your name\] and I edited this file online! 

At the bottom of the editing screen, you'll be asked to commit the result. Make sure to add a useful commit message. 

Ok, let's incorporate this change into our local repository. In GitHub Desktop, the button that used to say "Push" should now say either "Fetch" or "Pull" with an indicator of how many commits there are to be pulled. If it says "Fetch," you should click it once and wait for it to say "Pull." Once it says "Pull," click it again and wait a few moments for the pull to complete. 

Finally, check the `README.md` file on your local machine. The change that you made online should now be reflected in your local file as well. 

## ...and beyond...

Great job! If you comfortably navigated these exercises, then you have the necessary basics for working with git and GitHub. These will get you most of the way through the course, and indeed, through your programming career. The most important topics that we haven't yet discussed are *merging* and *branching*, which are especially relevant when collaborating with others. We may come back to these in a future Discussion activity. 

Another topic that you might find useful to explore on your own is the `.gitignore` file. This file specifies files which should be *excluded* from tracking by git. This is handy if there are certain "junk" files that you would prefer not to see in GitHub Desktop. 





