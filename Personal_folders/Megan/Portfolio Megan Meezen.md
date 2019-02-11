# Portfolio Megan Meezen KB-74-OPSCHALER


  <p align="center">
  <b>Welcome reader, feel free to have a look around</b><br> 
</p>

<p align="center">
  <img width="460" height="300" src="https://media.giphy.com/media/xUPGGDNsLvqsBOhuU0/giphy.gif">
</p>


<p align="center">
  <b>This is my portfolio for the minor Applied data science from the Hague University of applied sciences. I am a third year student industrial engineering and management. Befor I started this minor I had no background in programming Python, but I was keen on learning the skill. I was assigned with other fellow students to project OPSCHALER from the TU Delft. The project OPSCHALER started in September 2018 till January 2019. The goal for project OPSCHALER was to analyze smart meter data from 54 dwellings to see if it was possible to accurately predict residential energy consumption. One of the key points was to see if it was possible to predict energy consumption with as few paramaters as possible with the use of the residential housing and KNMI data. This portfolio will mainly focussed on what I learned during the minor. I hope you do enjoy my portfolio. NOTE TO READER: this portfolio has been improved to the repeat or re-trial portfolio delivery. It has been said to add more Neural Networks which I did.</b><br>
</p>

### Reader's Guide

This paper wil include information on the following subject:

- Completed courses: Datacamp, Coursera
- Data preperation&cleaning
- Data visualization&collection
- predictive models research&Evaluation
- Communication: Presentation, summaries, paper etc.
- Domain knowledge

  I.E. this is not a chronological order, just a summary of what this notebook includes. 

  Also my notebooks may be a mix of English and Dutch mixed together, but I don't see this as a problem since my readers are billingual.

###

  -Dwellings: Residential houses in the area of Rotterdam the Netherlands
  -Smartmeter data: data from smartmeters from dwellings
  -gasPower: Amount of gas used
  -Also a paper I used a lot was the one from a researcher from the TU Delft:  [link ](  https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/Master%20thesis%20report_%20Cristina%20Jurado%20Lopez-Data-driven%20Predictive%20Control%20for%20Heating%20Demand%20in%20Buildings%20(1).pdf)
  
  -Seaborn: Is een correlatiemap 
  -Fourier: Wiskundige manier om patronen te herkennen voor menselijke patronen binnen een huishouden, dit kan invloed hebben op het gasverbruik. 
   
   So first it is also important to know that out of all the features, six features were selected to use for predicting gas usage, which feature is used depends completely on the type of model and it's usage. 

### Completed Courses

### Datacamp
  I have completed the mandatory Datacamp courses. Which I found very helpfull for beginning programmers. Below you can see my score and completed chapters, I have also used Datacamp & Coursera & Machine learning mastery to create the neural networks:


<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/datacamp.png"> </p>
   Here is more insight in which courses/chapters I completed:
 <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/datacamp21.png"> </p>

### Coursera
  I have also completed the mandatory Coursera machine learning courses by Stanford university from Andrew Ng. 
 

<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/Coursera.png"> </p>

## Neural Networks Multivariate linear regression, Convolutional neural networks, Long-term short-term neural networks
  All these models shall be referred to from now on as: CNN, MVLR, LSTM
  
  So I created these models to show my skill and understanding of CNN, MVLR and LSTM. At first I had problems computing the easy neural network models as I wasn't allowed to show a DNN because it already had been done a lot of times by other people, which is completely understandable. I primarily used the Keras libraries as the anker point for the NN's because some funtions of tensorflow are not available because of the packages installed on the datascience server. First I shall talk about my first created MVLR, the MVLR is the best machine learning model to start with. 

<p align="center">
  <b>MVLR</b><br> 
</p>

 <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/MVLR.png"> </p>
   As you can see the actual gas prediction completely overlaps the prediction, which results in overfitting over a longer period of time, the amount of epochs(10) and test size(0.1) is standardized is all my NN notebooks to see if the different models perform the same or different in different set of conditions. Which actually does, every model does behave differently in the same set of conditions. Based on already known data from other scripts from the project the MVLR model should perform the best on the processed data set. 

[Click the link for the notebook :)](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/LSTM.ipynb) 

  Note: I also created a 3 dimensional map of a multivariate regression, which required an X,Y,Z space or two parameters moving around in the same area, but due to predictimg gas consumption this type of model wasn't suitable for a prediction with the use of 3MVLR to gain more insight. 
  
  [Click the link for the notebook :)](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/3dmvlr.ipynb) 
  
  <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/3DMVLR.png"> </p>



 <p align="center">
  <b>CNN</b><br> 
</p>
 
 <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/CNN.png"> </p>
 
  <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/CNN_sep.png"> </p>
  As seen the predicted values vary quite differently from the test/train data, but based on the amount of epochs the CNN actually performs better, which is rather suprising taking into account that the MVLR theoretically should perform better, increasing the amount of epochs and training and test size could influence the accuracy of the model. If we take computational power into account this CNN model does take more time and computational power with more 'accurate' predictions on GasPower.
  
  [Click the link for the notebook :)](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/CNN.ipynb) 
  
   <p align="center">
  <b>LSTM</b><br> 
</p>

 <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/LSTM_BLACK.png"> </p>

  
  The LSTM notebook actually didn't work right for some reason on the jupyter server which was quite a hinderance for me, the LSTM model was optional for me as this was the model which I found quite difficult to compute, I found a way to visualize it, but the accuracy is way off, but yet it was still an accomplishment for me, for those who would still like to see this LSTM notebook, it's on my personal drive of mycharm, for computational purposed I would have rather used pycharm. As it can be see the LSTM model does not perform well with prediction gas consumption this is due to the fact that there is a limited amount of data available, it is known that an LSTM needs tons of data to perform well, but would perform more accurate in case there was more data available. 
  
   [Click the link for the notebook :)](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/LSTM.ipynb) 
  
  
 
  
  

  

### Data preperation and cleaning
  Data preperation and cleaning are known in data science as very time consuming tasks. Since I didn't have any experience with Python I searched the internet for usefull guides on how to prep and clean the data we had. At first we only had smart meter data from 60 dwellings which now have been reduced to 52 dwellings. There were quite a lot of problems with the data sets from smart meter data and KNMI data. Before I even attempted in cleaning & prepping the "real" smartmeter data I searched for a random dataset and started prepping and cleaning to practice and develop my skills. See the link to my basic data prep&clean code on a IMDB movie rating.
Starter Basic data cleaning dummy set and yes this dummy set has been taken from another github user, I used this for practice in the beginning of the minor, so don't pay much attention to it, I just let this sit in my github so I can see where I improved my github page and for my own learning curve: 

[Click the link for the notebook :)](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Basic_data_cleaning_dummy%20set.ipynb)  

  I have also created a flowchart to have an insight in what the main code does. A flowchart has contributed to make the code clear for all groupmembers. See flowchart below. I used draw.io to create it.
  
  
 <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/Flowchart%20cleaning.png"> </p>
 
 [Click the link for the notebook on which the flowchart is based:)]( 
 https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/data_preperation_main.ipynb)  


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

## More data cleaning

  So for the remake of this portfolio I created some more data prep based on the processed and clean data files for the average dwelling, in the first part of the datacleaning you saw a seaborn heatmap with a lot of NaN's still included and not clear which parameters and features were suitable. I also added a histogram to gain more insight in the varity and division of the data and its features. You can see the images for the finally neat seaborn map. 
  
  <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/correlations_matrix.png"> </p>
  
   <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/correlations_matrix_2.png"> </p>
   
 <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/correlations_matrix_2.png"> </p>
 
 [Click the link for the notebook :)](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Prep.ipynb) 
 
 This gave an insight in the different correlations which eventually led to this list which was also presented at the final presentation at the symposium:
 
 In grey were the chosen features for the predictions 
 
  <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/parameters.png"> </p>
 
 
# Fourier series

(edit: this was also a github examplary notebook used for fourier which ended up as an example, majority part of notebook isn't my property, just to give an insight in the progress of the project, the data files had been loaded in though. )

The goal for the project at first was to predict the overal energy and electrical consumption to eventually figure out when certain appliences were used in a dwelling/residential house to save energy. This eventually changed to predicting only the gas consumption which was already difficult. In order to eventually have predictions on which appliences households used regurlarly an Fourier model had to be applied to distinguish different appliences in the household from eachother. An ARIMA/ARMA model would have worked, but I got advised to do a Fourier series, but this proved to be very difficult. I found two different ways to program a Fourier signal(FFT). I would've also liked to create a ARIMA model, but this was not a priority at the moment. 

Fourier method 1
[Click the link for the notebook :)](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/Fourier_1.ipynb) 

Fourier methhod 2
[Click the link for the notebook :)](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/Fourier2.ipynbb)

<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/fourier1_2.png"> </p>

### Conducted research on predictive models/NN

  During the project different predictive models were used. The project team was divided into two teams those who researched and those who created the models. I researched LSTM and GRU which are both neural networks which belonged to RNN. I also researched DNN and MVLR. There are multiple ways of interpreting these models and different was to compute them. Below I will link to the research I conducted. I would've linked my all my bookmarks/refrences in this git hub portfolio which I read, but there are hundreds of them. So to keep this my github portfolio ordened I inserted the documents I made regarding the machine learning topics. Github currently has a problem with opening PDF's , I also enlisted the PDF in the e-mail attachments just in case the links fail to work

#### Communication

  As In have mentioned in the beginnen of my portfolio. Before I started this minor I didn't have any programming background. I have    done a lot of research in the first couple of weeks on different topics regarding data science. I made a couple of documents containing helpfull information about: Fourier, Linear Regression, Regressional types, Neural networks/machine learning (DNN/GRU/MVLR), Seaborn. I created these documents for me to better understand Python and machine learnng and so my groupmates could also benefit from the documents. I have also created a Flow-chart based on the main code from OPSCHALER which has been changed over time. It was quite important for the progress of the group to have an overview of what we we're exactly doing at the time. I was really focused on datacamp the first couple of weeks and struggles with programming. I know some basics, but I am stil not as skilled as some of my other teammates. I have also read the most papers on understanding machine learning and it's uses and advantages. 
  
  (edit: I actually have computed more models on NN now compared to other teammates in the past so that's a plus) :) 


# Presentations

  I have also done a couple of presentations alone and together with teammates. I will post a link to my teammates portfolio for the rest of the presentations in which I participated.  [Link teammate](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/portfolio.md)
  
  
  The presentations down below are the ones I created and performed. 

[1](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/16-11-2018.pdf)
[2](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/17-10-2018%20good.pdf)
[3)](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/17-12-2018.pdf)
[4)](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/Final_pres.pdf)

  I presented the final presentation with brain, but you probably noticed. 

# Papers and research

  Here are the papers and conducted research links as discussed above. I added the links to the rough paper drafts I made and findings which I mainly created and the final paper were the whole team worked on. The table we created which shows the machine learning models performance is also in the final paper.

  1 = This paper draft contains my first findings based on reseaches conducted on machine learning methods[1](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/Findings_methodology.pdf)
  
  2 = A paper which explains the Gated Recurrent Unit
  [2](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/GRU.pdf)
  
  3 = A paper I made based on the differnt types of regressional methods
  [3](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/methods%20for%20regression.pdf)
  
  4 = A rough draft in which I added unfinished parts of the final paper and applied some feedback to it. 
  [4](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/Paper_rough_draft.pdf)
 
   Final team opschaler paper [5](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Megan/portfoliolinks/Imagesportfolio/Opschaler%20paper%20final%20version.pdf)
  
  #### Thank you :)
    
   As mentioned above I have added al these files listed, which I wrote all myself except for the final paper draft which was written together. 
    
  
