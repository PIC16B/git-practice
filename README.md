# Practice with git and GitHub

This is a very simple repository for practicing with git and GitHub. 

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








