# KB-74-OPSCHALER
Code for the KB-74-OPSCHALER project.

## Setting up GitHub on JupyterHub
Login to JupyterHub on the datascience server. 
In the top right press 'New -> Terminal'. A SSH terminal should pop up in a new window. 
Next follow this tutorial: [link](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent). 
When you have done this you will need to add the SSH key to your GitHub account: [link](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account). Notice that step 1 will not work because 'clip' is not recognized! Work around this by using FileZilla to browse to your `~/.ssh/id_rsa.pub` and download the file. Where `~` is your home folder. Then open the file with a texteditor, copy the contents and go on with the tutorial.
Test your connection: [link](https://help.github.com/articles/testing-your-ssh-connection/)

### Basic SSH commands
`ls` Lists directory contents
`cd` directory_name' Moves up to directory_name
`cd` Moves down a directory
`cp` Copies a file or directory to directory
Note that `~` represents your home folder. 
Linux commands: [link](https://1.bp.blogspot.com/-Y9rBRKuT0wA/VrJ7xwjdVjI/AAAAAAAAh2k/sdrCyf7nLbo/s1600/linux-reference-bg-invert-1.png)


### Cloning the KB-74-OPSCHALER repository
Once GitHub has been setup correctly you can clone this reposotiry by pressing the green `Clone or download` button, copy the (link](https://github.com/deKeijzer/KB-74-OPSCHALER.git). In the jupyter terminal window you should see the line `studentnumber@datascience:~$`. Move to the 'notebooks' folder by typing `cd notebooks`. The directory you are in now should be `~/notebooks`. While in here type `git clone <the link you copied, from this repository>`. Once this is done, move to the 'KB-74-OPSCHALER' folder by typing `cd KB-74-OPSCHALER`. Once in here type `git status`. This will give you additional information and show you that you have cloned successfully. 

### Git push & pull
Before you start working on code in jupyter, be sure that you have the latest version of this repository. Do this by typing `git pull`. Once you have written certain parts of code and want to upload it to this repository do this as follows.
* `git add .` (this will select all files)
* `git commit -m 'commit message. For examples changes that you made to the code.'`
* `git push`
