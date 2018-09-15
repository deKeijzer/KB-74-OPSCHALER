# KB-74-OPSCHALER
This repository contains code for the KB-74-OPSCHALER project. KB-74 stands for the minor Applied Data Science at the Hague University of Applied Sciences, with Opschaler being the project name. The goal of this project is to predict the energy usage of houses, 1 week a head with a 10 second resolution. More information about Opschaler can be found at their [website](http://www.opschaler.nl/). 

## Setting up GitHub on JupyterHub
1. Login to JupyterHub on the datascience server. 
2. In the top right press 'New -> Terminal'. A SSH terminal should pop up in a new window. 
3. Next follow this tutorial: [link](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent). 
4. When you have done this you will need to add the SSH key to your GitHub account: [link](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account). Notice that step 1 will not work because 'clip' is not recognized! Work around this by using FileZilla to browse to your `~/.ssh/id_rsa.pub` and download the file. Where `~` is your home folder. Then open the file with a texteditor, copy the contents and go on with the tutorial.
5. Test your connection: [link](https://help.github.com/articles/testing-your-ssh-connection/)
6. You are ready to clone repositories.

### Basic SSH commands
* `ls` Lists directory contents
* `cd` directory_name' Moves up to directory_name
* `cd` Moves down a directory
* `cp` Copies a file or directory to directory
Note that `~` represents your home folder. 
More info on Linux commands: [link](https://1.bp.blogspot.com/-Y9rBRKuT0wA/VrJ7xwjdVjI/AAAAAAAAh2k/sdrCyf7nLbo/s1600/linux-reference-bg-invert-1.png)


### Cloning the KB-74-OPSCHALER repository
1. Once GitHub has been setup correctly you can clone this reposotiry by pressing the green `Clone or download` button, copy the (link](https://github.com/deKeijzer/KB-74-OPSCHALER.git). 
2. In the jupyter terminal window you should see the line `studentnumber@datascience:~$`. Move to the 'notebooks' folder by typing `cd notebooks`. The directory you are in now should be `~/notebooks`. 
3. While in here type `git clone <the link you copied, from this repository>`. 
4. Once this is done, move to the 'KB-74-OPSCHALER' folder by typing `cd KB-74-OPSCHALER`. 5. Once in here type `git status`. This will give you additional information and show you that you have cloned successfully. 

### Git push & pull
Before you start working on code in jupyter, be sure that you have the latest version of this repository. Do this by typing `git pull`. Once you have written certain parts of code and want to upload it to this repository do this as follows.
* `git add .` (this will select all files)
* `git commit -m 'commit message. For examples changes that you made to the code.'`
* `git push`
More push & pull information can be found in [this notebook](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/GitHub%20push%20%26%20pull%20tutorial.ipynb).

# Important data locations

## KNMI dataframe
`weather = pd.read_csv('//datc//opschaler//weather_data//weather.csv', delimiter='\t', comment='#', parse_dates=['datetime'])  
weather = weather.set_index(['datetime'])  
weather.head()`
