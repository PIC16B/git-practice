# Practice with git and GitHub

\[Your Step 3 Edit Here\]

This is a very simple repository for practicing with git and GitHub. git is a utility for *version control*. When a body of code is tracked with git, it is easy to see how the software has evolved over time, to roll back changes when needed, and to incorporate modifications by multiple collaborators. In this activity, we're going to focus on core git workflows for single-person projects. We may do a follow-up activity later in the quarter on workflows for collaborative projects. 

GitHub is a free online code hosting service that runs using git. We'll use git and GitHub to collaborate on code and to host the blogs on which you'll submit your homework. 

***Note***: if you are already comfortable using git from the command line, you can follow along with these instructions, replacing GitHub Desktop operations with the appropriate terminal commands. Both approaches are valid!! Phil personally prefers GitHub Desktop, but many prefer the command line instead. 

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

But wait -- let's do more. Make a new folder called `practice-folder` within the cloned repository. Then, create a Jupyter Notebook in this folder. Run the following code, obtaining a simple plot of a sine wave. 

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

## 10. Discard and Revert

One huge advantage of working with a version control system like git is that you can easily undo mistakes by going back to the last "good" version of your project. There are multiple ways of doing this. We'll focus on two. 

### 10.1 If You Haven't Committed Yet: Discard

So, you were making a small tweak to your file and accidentally broke the amazing function that you were working on. It happens! If you catch this before you commit your changes, then fixing it is easy -- all you need to do is *discard* your changes. 

In that Jupyter notebook you created in Step 5, delete the line `import numpy as np`. Now your notebook won't correctly generate the plot (after resetting the kernel). Whoops! Pretend that you didn't notice, and save the notebook. 

Over in GitHub Desktop, notice that there is a change recorded to that file. Right-click on the change and choose "Discard Changes." Check your notebook again. You should observe that the line `import numpy as np` is back where it belongs. Great!

### 10.2 If You Committed Your Mistake: Revert

Sometimes, we don't catch a mistake until after we've already committed it. If we're unlucky, we may even have created other commits since our mistake. In these cases, the first step is to identify on which commit the error was introduced. This requires careful debugging and attention to detail. One approach is to *go back* to a previous commit on which you know your code was working, and then step through the changes you made. To do this, we use the *revert* command. 

Go back to your Jupyter Notebook, and delete `import numpy as np` again. This time, commit the change, with commit message "remove numpy import." Oops! Now our committed code is broken. 

To *revert* the commit, navigate over to the History tab of GitHub Desktop. Right-click the commit with the message "remove numpy import," and choose "Revert Changes in Commit." This will have the effect of creating a *new* commit that undoes the changes in your erroneous commit. This will work even if you've made other commits since the bad one; only the changes from the bad commit will be reverted. 

***Note***: GitHub Desktop doesn't gave an option corresponding to `git reset`, but if you are comfortable in the terminal and familiar with this command, you can also use `git reset` to accomplish a similar task, albeit with different consequences for your commit history.

### 11. No Duplicate Files! 

An important principle of version control is that you **never** duplicate files. Rather than having `first_draft.ipynb`, `final_version.ipynb`, `final_version_REAL.ipynb`, you should instead commit your code at each stage (or even more frequently). You'll always be able to go back and find the earlier versions in the commit history. 

## More to Learn

Great job! If you comfortably navigated these exercises, then you have the necessary basics for working with git and GitHub. These will get you most of the way through the course, and indeed, through your programming career. The most important topics that we haven't yet discussed are *merging* and *branching*, which are especially relevant when collaborating with others. We may come back to these in a future Discussion activity. 

Another topic that you might find useful to explore on your own is the `.gitignore` file. This file specifies files which should be *excluded* from tracking by git. This is handy if there are certain "junk" files that you would prefer not to see in GitHub Desktop. 
