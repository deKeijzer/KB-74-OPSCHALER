__Introduction__

This portfolio describes the work I (Daan Boesten, 16021665) have done during the minor Applied Data Science. The minor was held in the period from September 2018 to January 2019 at The Hague University of Applied Sciences. With a group of 6 students we were assigned to the OPSCHALER project, a measurement campaign on the influence of housing characteristics on energy costs and comfort. Our goal was to predict the energy consumption of residential dwellings using several machine learning methods. Gaining insight into the energy consumption that will be used by residents in the near future can be helpful in balancing the grid. 

The OPSCHALER group consists of members from the TU Delft, The Hague University and several companies which can be found here http://www.opschaler.nl/partners/. Thus far the TU Delft has recorded energy consumption data from 52 residential dwellings. This data has been used as training data for the machine learning models. 

During this minor we tried to answer the following research question:

_Is it possible to accurately predict the house energy consumption with few physical building parameters and the climate data with use of multivariate regression models and neural network models?_

After consulation with the OPSCHALER group it was decided to aim to predict the energy consumption for a week ahead with hourly and daily resolutions. Three different methods were going to be compared based on the accuracy of the prediction:

1. Multivariate regression
2. Fourier series
3. Neural networks 

| Resolution | Multivariate regression | Fourier series | Neural networks |
|------|------|------|------|
| Hourly | ..% | ..% | ..% |  
| Daily  | ..% | ..% | ..% |
| Weekly  | ..% | ..% | ..% | 


In addition to the prediction accuracy, it was also important to compare the computing time needed for each prediction method. One of the end goals of OPSCHALER is to locally predict the energy consumption using smartmeter data, with a preference for low computing power methods to minimize costs and power consumption. 

During the minor we learned about several deep learning models, each with its own pros and cons. We encountered some of those models in other research papers on forecasting energy (mainly university buildings), during the guest lectures and weekly presentations. It was decided to focus our research on trying out and comparing those deep learning models instead of using just one neural network.
    
__Personal Work__
  
My interest in data science began when I first learned about the usage of artificial neural networks in pattern recognition. It was incredible to see neural networks being applied in many different applications such as autonomous driving, human speech recognition and even the recognition of brain tumors. I really wanted learn this in depth, so I thought the minor Applied Data Science would be a good introduction to this.

During the first 2 weeks our project group was split into two teams:  
__Team 1__: Data cleaning & preparation  
__Team 2__: Reading literature on other forecasting studies  
  
  I was part of the second team, which meant we had to search for related research papers on forecasting energy consumption. We noticed straight away that most of the research has been done on universtity buildings, probably due to privacy issues regarding the data collection of residential dwellings. By collaborating with OPSCHALER, we had access to 52 dwellings with up to 9 months of data. This was pretty cool. 
  
  Most of the research was based around either multivariate linear regression (MVLR) or deep neural networks (DNN). We weren't able find any papers that applied Fourier Transforms to recognize certain human patterns, which we thought could help with the forecasting accuracy. We saw this as an oppertunity to try something new, which will be shown later in the portfolio (spoiler alert: didn't work as well as expected). 
  
  Alongside the literature, all project members focused on machine learning in Python. This was mostly done using Datacamp and Coursera. The courses and weeks in which I participated can be found at the bottom of the portfolio. Due to my background in Physics, I had a pretty solid knowledge of Matlab, which is my opinion pretty similar to Python. 
  
  Due to the impressive  motivation and contribution in machine learning by our group member Brian, my focus during this minor was mainly around understanding and visualizing the data. Thus, this portfolio will mostly show the contributions I did in terms of getting to know the fundementals behind the data. 
  
  __Understanding and visualizing the data__
  
 
 To reach our goal of using as less building characteristics and climate data as possible, I decided to look at what could be done with just the outside temperature and gas consumption data from multiple dwellings. After team 2 had finished collecting the smart meter data from the OPSCHALER database and weather data from KNMI, I [wrote a code](https://datascience.hhs.nl:8888/user/16021665/notebooks/KB-74-OPSCHALER/Personal_folders/Daan/correlationships.ipynb) to visualize the temperature and gas consumption at different time frames. This was done by taking the mean gas consumption and average outside temperature. The following gif shows the result:
  
<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Daan/Images/gasvstemp2.gif"  width="700"> </p>
    
 The first plot is the (almost) raw data with a resolution of 1 hour. Mainly due to human patterns and day/night diffference, the data fluctuates a lot. However, when the data is resampled to different time frames, an inversely proportional correlation between gas consumption and temperature begins to show up. Although this is intuitive, showing this correlation with data is pretty convincing. 
   
   To show this in another way, [in the same notebook](https://datascience.hhs.nl:8888/user/16021665/notebooks/KB-74-OPSCHALER/Personal_folders/Daan/correlationships.ipynb) I used Seaborn heatmap to plot the correlation between all variables from the KNMI data and dwelling energy consumptions. The correlation between outside temperature (T) and gas consumption (gasMeter) was calculated at different times frames, which can be seen in the following plot: 
  <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Daan/Images/correlatie.png"  width="700"> </p>  
  
  It is impressive to see a correlation of (almost) -1 between the outside temperature and gas consumption at a time fame of a month. When this was shown to our project leader Baldiri, he asked me to sent those plots for his future lectures about building characteristics. This gave our group motivation to keep on getting great results, which in my opinion is one of the most important things when working together.  
  
  We also noticed that most dwellings seem to stop heating when the outside temperature is above around 16.5 °C. This property was used to create a simple linear regression using the gas consumption when the outside temperature was lower than 16.5 °C. The result can be seen in the following plot:
      <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Daan/Images/gasvstemp1d%20(1).png"  width="700"> </p>  
  When this is extrapolated, an estimation can be calculated for the gas consumption at temperatures below  16.5 °C
  __Presentations__  
[First presentation TU Delft](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/appendix/friday%20presentations/28-09-2018%20(TU%20delft%20meeting).pptx) 

The weekly presentations I did are listed below: <br>
[Week 1](https://prezi.com/p/28wycwuqqggc/#present)   
[Week 3](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/appendix/friday%20presentations/14-9-2018.pptx)  
[Week 6](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/appendix/friday%20presentations/05-10-2018.pptx)  
[Week 10](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/appendix/friday%20presentations/05-10-2018.pptx) 


__Datacamp__

<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Daan/Images/datacamp.png"> </p>

Followed courses:  
[Intro to Python for Data Science](https://www.datacamp.com/statement-of-accomplishment/course/f8e37c6eb334a741da23db6990d164c06bd249ff)  
[Intermediate Python for Data Science Course](https://www.datacamp.com/statement-of-accomplishment/course/4690bbe3cc8780040feb0ff962fd0df8b4aea56d)  
[Supervised Learning with scikit-learn Course](link) (Chapter 1,2) 
 
__Coursera__
<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Daan/Images/stanford.png"> </p>
