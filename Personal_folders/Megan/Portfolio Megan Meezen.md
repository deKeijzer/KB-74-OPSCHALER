# Portfolio Megan Meezen KB-74-OPSCHALER


  <p align="center">
  <b>Welcome reader, feel free to have a look around</b><br> 
</p>

<p align="center">
  <img width="460" height="300" src="https://media.giphy.com/media/xUPGGDNsLvqsBOhuU0/giphy.gif">
</p>


<p align="center">
  <b>This is my portfolio for the minor Applied data science from the Hague University of applied sciences. I am a third year student industrial engineering and management. Befor I started this minor I had no background in programming Python, but I was keen on learning the skill. I was assigned with other fellow students to project OPSCHALER from the TU Delft. The project OPSCHALER started in September 2018 till January 2019. The goal for project OPSCHALER was to analyze smart meter data from 54 dwellings to see if it was possible to accurately predict residential energy consumption. One of the key points was to see if it was possible to predict energy consumption with as few paramaters as possible with the use of the residential housing and KNMI data. This portfolio will mainly focussed on what I learned during the minor. I hope you do enjoy my portfolio.</b><br>
</p>

### Reader's Guide

This paper wil include information on the following subject:

- Completed courses: Datacamp, Coursera
- Data preperation/cleaning
- Data visualization/collection
- Predictive models
- Evaluation
- Communication: Presentation, summaries, paper etc.
- Domain knowledge

### Completed Courses

#### Datacamp
  I have completed the mandatory Datacamp courses. Which I found very helpfull for beginning programmers. Below you can see my score and completed chapters:


<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/datacamp.png"> </p>
   Here is more insight in which courses/chapters I completed:
 <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/datacamp21.png"> </p>

#### Coursera
  I have also completed the mandatory Coursera machine learning courses by Stanford university from Andrew Ng. Even though 
 

<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/Coursera.png"> </p>

### Data preperation and cleaning
  Data preperation and cleaning are known in data science as very time consuming tasks. Since I didn't have any experience with Python I searched the internet for usefull guides on how to prep and clean the data we had. At first we only had smart meter data from 60 dwellings which now have been reduced to 52 dwellings. There were quite a lot of problems with the data sets from smart meter data and KNMI data. Before I even attempted in cleaning & prepping the "real" smartmeter data I searched for a random dataset and started prepping and cleaning to practice and develop my skills. See the link to my basic data prep&clean code on a IMDB movie rating.
Starter Basic data cleaning dummy set: 

[Click the link for the notebook :)](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Basic_data_cleaning_dummy%20set.ipynb)  

### Data visualization
  In last couple of weeks of the first semester of the project. The best available dwelling was dwelling ID: 378, currently this dwelling has changed and the best dwelling is now dwelling ID: 8655. The primairy focus was to try to visualize the gasPower. The graph should've been more accurate since the dataset still consisted of NaN's and no mean values were taken. [Click the link for the notebook :)](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/First_visuals.ipynb) 
  
  Below is a piece of the code which created the plot/graph(with NaN's and no mean)
```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  import seaborn as sns 
  #To check the dataset select the first few columns
  
  df.head()

  df = pd.read_csv('/datc/opschaler/output/P01S01W0378_gas_electricity_weather.csv',header = 0, delimiter="\t")

```
<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/visuals2.png"> </p>

<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/firstplot378withnans.png"> </p>

To see if there were any correlations between the KNMI data and the smart meter data for dwelling 378 I created a Seaborn heatmap. Due to the NaN's in 378 there are empty spaces. There are high negative correlations between certain variables and positieve correlations on certain variables. 
<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/seaborncor.png"> </p>

## Fourier series

The goal for the project at first was to predict the overal energy and electrical consumption to eventually figure out when certain appliences were used in a dwelling/residential house to save energy. This eventually changed to predicting only the gas consumption which was already difficult. In order to eventually have predictions on which appliences households used regurlarly an Fourier model had to be applied to distinguish different appliences in the household from eachother. An ARIMA/ARMA model would have worked, but I got advised to do a Fourier series, but this proved to be very difficult. I found two different ways to program a Fourier signal(FFT). I would've also liked to create a ARIMA model, but this was not a priority at the moment. 



#### Communication

As In have mentioned in the beginnen of my portfolio. Before I started this minor I didn't have any programming background. I have done a lot of research in the first couple of weeks on different topics regarding data science. I made a couple of documents containing helpfull information about: Fourier, Linear Regression, Regressional types, Neural networks/machine learning (DNN/GRU/MVLR), Seaborn. I created these documents for me to better understand Python and machine learnng and so my groupmates could also benefit from the documents. I have also created a Flow-chart based on the main code from OPSCHALER which has been changed over time. It was quite important for the progress of the group to have an overview of what we we're exactly doing at the time. 
