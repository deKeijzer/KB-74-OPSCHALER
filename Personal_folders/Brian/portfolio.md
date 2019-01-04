`TODO: check spelling`  
Last updated: 04-01-2019 (DD-MM-YYYY)

# Personal portfolio  
Personal portfolio for the minor Applied Data Science at the Hague University of Applied Sciences.  

Student name: Brian de Keijzer  
Student number: 16011015  
Email: b.dekeijzer@student.hhs.nl  

## Introduction
This is a general introduction to the KB74-OPSCHALER project and it is also intended for people who do not know anything about the Applied Data Science minor.  
  
In the OPSCHALER project multiple universities and (energy) companies collaborate in developing methods and tools to extract useful information out of the energy usage data of residential houses on different aggregation levels. For more information on OPSCHALER itself, see their website: [www.opschaler.nl]( http://www.opschaler.nl/).  

The Hague University is one of the collaborators and offers the OPSCHALER data to students in their Applied Data Science minor, which takes one semester (30 ECT). This leads us to the KB74-OPSCHALER project.  
  
<details><summary> <b>Click here for information regarding the KB74-OPSCHALER team.</b>  </summary>  
  
<p> 
Our team consists of 6 students, 2 of which are doing this for their European Project Semester. Every one of us has different backgrounds. One person has a BSc in telecommunication engineering and is currently doing a masters. The others are studying industrial engineering and management, computer science engineering and engineering physics. Another important note is that most of us have never programmer before, or only in MATLAB. So along with learning the subjects from the minor, most of us had to learn Python from scratch aswell.  
  
</p>
</details>  
  
  
Our research started out by trying to predict the electricity and gas consumption of individual residential houses on a 10 second and one-hour resolution, respectively. The time we wanted to predict ahead was one hour to a week, by using as less data as possible. 
Due to model complexity, time, and scarce messy data, the research got narrowed down to predicting the gas consumption of houses on the aggregated level, predicting one hour, a day and a week ahead with an hourly resolution. This is done by only using historical and future weather information. Whereas the aggregated level in our case consists of the mean gas usage of 54 houses and could represent a block of houses. These predictions are done by using the different models listed below and are eventually compared to each other.  

- MVLR: Multivariate Linear Regression
- DNN: Deep Neural Network
- CNN: Convolutional Neural Network
- RNN: Recurrent Neural Network
- LSTM: Long Short-Term Memory
- GRU: Gated Recurrent Unit
- TimeDistributed(CNN)+RNN+DNN

Despite these models being based on data on the aggregated level, they should also work for individual houses when trained specifically for that house. Creating an accurate general model, using only weather data is just hard due to each house having a specific gas consumption pattern.  


## Jargon
`TODO: Add more jargon.  `  
Used jargon for Opschaler is listed below.
* Dwelling: an unique house.  
* Smartmeter data: electricity and gas meter data.   
* gasPower: amount of gas being used at a given time.
* ePower: amount of electricity being used at a given time.
* smart: electricity DataFrame of a dwelling.
* seq2seq: sequence to sequence

## Online courses
Onlince courses from both DataCamp, Coursera and fast.ai have been followed for this minor.

### DataCamp
<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/datacamp/General.png"> </p>

One of my personal goals was to finish the [Data Scientist with Python](https://www.datacamp.com/tracks/data-scientist-with-python) track on DataCamp ([statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/track/a5c7f47662f67b9a19bf1a214c3316ecb7573b62)). Apart from this I also did some other courses which seemed usefull for KB74-OPSCHALER. All mandatory courses for the minor have been finished. Screenshots of the completed courses are shown below. Links to the course description including the statement of accomplishment can be seen below the screenshots. 

<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/datacamp/data_scientist_track.png"> </p>

**Completed courses (not in order)**  
![courses part 1](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/datacamp/p1.png)  
![courses part 2](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/datacamp/p2.png)  
![courses part 3](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/datacamp/p3.png)  
![courses part 4](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/datacamp/p4.png) 

Press `course description` to see the contents of the course, press `statement of accomplishment` to see the certificate given out by DataCamp upon completing the course. To see everything in one view, you can also look at my DataCamp profile [here](https://www.datacamp.com/profile/BrianDeKeijzer).

**Basic Python**
* Intro to Python for Data Science: [course description](https://www.datacamp.com/courses/intro-to-python-for-data-science), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/01e115bd07164cd840cc41c7fe831ba08d7dca1a)   
* Intermediate Python for Data Science Course: [course description](https://www.datacamp.com/courses/intermediate-python-for-data-science), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/246fecb0b112d881f24131944063f3345cbb70d8)  

**Python for Data Science**  
* Python Data Science Toolbox (Part 1) Course: [course description](https://www.datacamp.com/courses/python-data-science-toolbox-part-1), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/d07e9a26136fd801656e94bd39049247602fbce1)  
* Python Data Science Toolbox (Part 2) Course: [course description](https://www.datacamp.com/courses/python-data-science-toolbox-part-2), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/f88ff03b0c3bd4f71781cff692a3cbaed61a4be7)  

**Importing data**
* Importing Data in Python (Part 1) Course: [course description](https://www.datacamp.com/courses/importing-data-in-python-part-1), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/2e6d0dde86e189b3b79328a823104b3937c57b56)  
* Importing Data in Python (Part 2) Course: [course description](https://www.datacamp.com/courses/importing-data-in-python-part-2), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/824adfac50d7835387dc9509863ec42aef63ee16)  

**Cleaning and transforming data**
* Cleaning Data in Python Course: [course description](https://www.datacamp.com/courses/cleaning-data-in-python), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/7a1c78cc670415289136447878822899ac968543)  
* pandas Foundations Course: [course description](https://www.datacamp.com/courses/pandas-foundations), [](https://www.datacamp.com/statement-of-accomplishment/course/95341cab0c49de075afc345533b945176bb92f41)  
* Manipulating DataFrames with pandas: [course description](https://www.datacamp.com/courses/manipulating-dataframes-with-pandas), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/24164e462d63070611fc45ff9349836c3f196551)  
* Merging DataFrames with pandas Course: [course description](https://www.datacamp.com/courses/merging-dataframes-with-pandas), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/673dba72c544df4b977cf6b555d2d6799f81f33e)  

**Databases**
* Introduction to Databases in Python Course: [course description](https://www.datacamp.com/courses/introduction-to-relational-databases-in-python), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/bc8bc8a89124619d48d6338aab461c6177825c1d)  
* Intro to SQL for Data Science Course: [course description](https://www.datacamp.com/courses/intro-to-sql-for-data-science), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/e7264e6e4e916f6f0730027bf2dff39be676454b) 
* Joining Data in PostgreSQL Course: [course description](https://www.datacamp.com/courses/joining-data-in-postgresql), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/ae1c6e0d5368e0fad21003b42abcb4be88aa5e10)  

**Data visualisation**
* Introduction to Data Visualization with Python Course: [course description](https://www.datacamp.com/courses/introduction-to-data-visualization-with-python), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/75b9fd93c583c0c0131106ef05b1a52515ccf0e2)  
* Interactive Data Visualization with Bokeh Course: [course description](https://www.datacamp.com/courses/interactive-data-visualization-with-bokeh), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/0b559a1d25a6f3b1260f248838d6f968b22ed727)  

**Statistics with Python**
* Statistical Thinking in Python (Part 1) Course: [course description](https://www.datacamp.com/courses/statistical-thinking-in-python-part-1), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/9f6cd5082511ecb5d6b7c6bf9fd053350d3c13af)  
* Statistical Thinking in Python (Part 2) Course: [course description](https://www.datacamp.com/courses/statistical-thinking-in-python-part-2), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/14f7db481ac78649805ff20d36355693157f2fce)  

**Machine learning & Deep learning**
* Supervised Learning with scikit-learn Course: [course description](https://www.datacamp.com/courses/supervised-learning-with-scikit-learn), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/8cf4bedbf7fc5cb2d81cf69a97e634fc818cd7a7)  
* Deep Learning in Python Course: [course description](https://www.datacamp.com/courses/deep-learning-in-python), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/c90ac629566673ede129fa1e18fd4e42764cc702)   
* Preprocessing for Machine Learning in Python Course: [course description](https://www.datacamp.com/courses/preprocessing-for-machine-learning-in-python), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/f43c37bfe1b7b90f0d9997ea180470e43c8d0b08)  
* Unsupervised Learning in Python Course: [course description](), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/4b29bc8932dd18603ed8d945d14e478a3cdb2957)  
* Network Analysis in Python (Part 1) Course: [course description](https://www.datacamp.com/courses/network-analysis-in-python-part-1), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/3414d0b46826e1582680c0257757fe4ee3c886e4)  
* Machine Learning with the Experts: School Budgets Course: [course description](https://www.datacamp.com/courses/machine-learning-with-the-experts-school-budgets), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/2076db5ee5120136404a0311a29164aa8141ab8e)  


**Big data & parallel computing**
* Parallel Computing with Dask Course: [course description](https://www.datacamp.com/courses/parallel-computing-with-dask), [statement of accomplishment](https://www.datacamp.com/statement-of-accomplishment/course/2c005dbb8743cd4210165c2326863f2dddc5ded7)  


### Coursera: Machine Learning by Stanford University
The mandatory courses as set by the guidelines of the minor have been completed and are listed below. Programming assignments have not been done. 
<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/coursera/general.png"> </p>

<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/coursera/week%201.png"> </p>

<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/coursera/week%202.png"> </p>

<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/coursera/week%203.1.png"> </p>

<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/coursera/week%203.2.png"> </p>

<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/coursera/week%206.png"> </p>

### Fast.ai
The courses from [fast.ai](https://www.fast.ai/) got recommended by a teacher as extra and more advanced material. They offer a Python package that allows the usage of more state of the art deep learnings methods, in a more simple and less code intensive way than is currently (21-11-2018) possible with Keras and TensorFlow. Their course material consists of lectures and example notebooks of the covered material during those lectures. The following courses have been followed.  

* Deep learning part 1
  * Recognizing cats and dogs (image recognition): [link to course](https://course.fast.ai/lessons/lesson1.html)
  * Convolutional neural networks: [link to course](https://course.fast.ai/lessons/lesson2.html)
  * Improving your image classifier: [link to course](https://course.fast.ai/lessons/lesson3.html)
  * Structured, time series & language models: [link to course](https://course.fast.ai/lessons/lesson4.html)
  * Collaborative filtering; inside the training loop: [link to course](https://course.fast.ai/lessons/lesson5.html)
  * Interpreting embeddings; RNNs from scratch: [link to course](https://course.fast.ai/lessons/lesson6.html)

These courses have been very usefull to learn more about DNNs and specifically CNNs and RNNs. Certain methods like the learning rate scheduler and transfer learning have been applied in Keras during the project.  


## Friday presentations  
`TODO: dump as PDF`  
The weekly KB74-OPSCHALER presentations that I contributed to.
* [Week 1: made by all group members](https://prezi.com/p/28wycwuqqggc/#present), presented by Megan & Brian. 
* [Week 4](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/appendix/friday%20presentations/21-09-2018.pptx), presented by Victor G. and Brian.
* [Week 7](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/appendix/friday%20presentations/12-10-2018.pptx), presented by Pol and Brian.
* [Week 10](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/appendix/friday%20presentations/9-11-2018.pptx), presented by Pol. Slide 2 up to and including 25 are made by me.
* [Week 11](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/appendix/friday%20presentations/Opschaler%20partners%20presentation%20%20at%20TU%20Delft%20(13-11-2018).pptx), presented by Victor G. and me. The complete presentation design and the figures from slide 5, 14, 16 are made by Victor G. Figures from slide 42 are from Daan. The other content is made by me.
* [Week ?, contains usefull animations](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/appendix/friday%20presentations/07-12-2018.pptx), made & presented by me.


## Python notebooks
`TODO: Only list relevant notebooks that show what has been learned. For example: do not list 5 notebooks for reading in data.`  
`TODO: Add screenshots of important code & plots to show the learning progress`  
`TODO: Clean up and run all notebooks show the correct output is shown.`  
`TODO: Dump final versions of notebooks to pdf and link to those.`  
`TODO: Update github history timeline once everything is done.`  
All notebooks have been commented, apart from lines where the programming is basic Python (for data science). Besides commenting code, i try to document all changes by committing small changes to GitHub. Doing this helped to document the work being done. However, the amount of commits obviously is no estimate of the quality of the work.

<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/github_timeline.png"> </p>

Certain events have been marked with an arrow, to see their description click the dropdown box below. 

<details><summary> <b>Click here to see the GitHub commit history description.</b>  </summary>  

1. Initial commit of KB74-OPSCHALER and the start of data reading & cleaning.  
2. Finished the largest part of data cleaning and started working on MVLR and neural networks.   
3. Started creating the personal portfolio.  
4. Finished the main models, started working on the multivariate time series in Keras repository.  
5. Polishing all the models and adding explanations to all the models.  
6. Mainly finished step 5, found out there is a data leakage. The test set was used as validation set.  
7. Fixed the data leakage and started using Hyperas to find model architectures again. This is because the previous architectures are biased due to the previous dataleakage.  

</details>  
  
Quite a lot of notebooks which are relevant for KB74-OPSCHALER have been created by me. Most started out as smaller notebooks, to learn the programming techniques required for the job. Later on a lot of the smaller notebooks have been combined in larger important notebooks. Important notebooks have been marked with (!), really important ones are marked with (!!). These (!!) are notebooks that contain main code for KB74-OPSCHALER. I basically have done everything from extracting the raw data from multiple sources, to cleaning and combining it to two usable Pandas DataFrame (10s and 1H resolution). Besides this i also did all the preprocessing and created all the models that are used for the gas consumption prediction.
  
The notebooks that have been made for KB74-OPSCHALER are:
  
* Data preperation  
This is the process of preparing the raw data for analysis, getting the data in easy useable DataFrames. The raw data consists of sensor data per dwelling, smartmeter data per dwelling and KNMI weather data of a station in Rotterdam. The smartmeter dataframes consists of merged electricity and gasmeter frames. Certain datafiles are in nested folders, with each file having a uniqiue name. The file types are both `.csv` and `.xlsx`. 
  * Reading in data 
    * Reading in raw sensor + excel data: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/Reading%20_in_data/reading_in_raw_sensor%2Bexcel_data.ipynb)
    * Reading in raw smartmeter data: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/Reading%20_in_data/reading_in_raw_smartmeter_data.ipynb)
    * Reading in raw weather data: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/Reading%20_in_data/reading_in_raw_weather_data.ipynb)

  * Cleaning & combining data  
    * Combining weather, electricity and gas data: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/Cleaning_combining_data/Combining%20weather%2C%20electricity%20and%20gas%20data.ipynb)
    * Cleaning house data: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/Cleaning_combining_data/cleaning_excel_data.ipynb)

  * NaN checker  
    * DataFrame NaN checker: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/NaN_checker/df_NaN_checker.ipynb)
    * Drop NaN streaks above set threshold: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/NaN_checker/drop_nan_streaks_above_threshold.ipynb)

  * Main data preperation notebooks: Reading, cleaning & combining all dwellings
    * (!) Data preperation main notebook: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/data_preperation_main.ipynb)
    * Loading combined smart, gas and weather generalized notebook: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/loading_combining_smart_gas_weather_generalized.ipynb)
    * (!) Creating one DataFrame for all dwellings: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/Create%20one%20df%20for%20all%20dwellings.ipynb)

* KNMI  
In these notebooks the 10 minute resolution weather data is processed. This data has been received by mail from the KNMI. The raw data consists of a folder with multiple `.csv` files. There are different file types depending on the measured variables and the year in which the values were measured.  
  * (!) Combining DataFrames: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/KNMI/1.KNMI_high_resolution_combining_dfs.ipynb)
  * (!) Cleaning DataFrames: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/KNMI/2.KNMI_high_resolution_cleaning_df.ipynb)
  * Exploratory Data Analysis (EDA): [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/KNMI/KNMI%20visualization.ipynb)

* (!) EDA  
Notebooks that contain general EDA on the created DataFrames which contain all the combined raw data per dwelling. Plus a table containing usefull information per dwelling has been created. 
  * EDA on dwelling P01S01W8655: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/EDA/EDA%20on%20dwelling%20P01S01W8655.ipynb)
  * Raw dwelling information table: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/EDA/Raw%20dwelling%20information%20table.ipynb)
  * Reading in all dwellings, plus making correlation matrices: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/EDA/reading%20in%20%26%20correlation%20matrices%20on%20processed%20data.ipynb)
  
* PyCharm  
The 'data_preperation_main.py' file used to be the main script to create the prepared dwelling data. Later on Dask has been implemented due to having improved performance because of being able to parallelize tasks on multiple CPU cores.  
  * (!) Data preperation main script: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/EDA/reading%20in%20%26%20correlation%20matrices%20on%20processed%20data.ipynb)
  * Data preperation main test notebook: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/pycharm/data_preperation_main_test_notebook.ipynb)
  * EDA on processed data: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/pycharm/EDA%20on%20processed%20data.ipynb)
 
* Dask  
Currently (29-10-2018) this is the main notebook for all the data processing done for KB74-OPSCHALER. This notebook has implemented most relevant functions from previously listed notebooks in a way so they can be run in parallel with Dask. It basically takes all raw data and saves unprocessed and processed (NaNs taken care off) `.csv` files per dwelling, which can be used for analysis.
  * (!!) Dask data processing: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Dask/Dask%20data%20processing.ipynb)

* Keras  
This folder contains all the notebooks related to deep learning. Note that there are multiple notebooks being very similar to each other. Sometimes the only difference inbetween similar notebooks are changes in settings (nodes, layers and selected dwellings). Most notebooks start off with EDA to check if the correct data is being used, then the model is being created and evaluated.
  * Feedforward
    * All dwellings EDA + machine learning: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/feedforward/all%20dwellings%20EDA%20%2B%20machine%20learning.ipynb)  
  Notebooks containing feedforward models.  
    * 8655 gasPower, sample rate 1 day: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/feedforward/8655%20gasPower%201D.ipynb)
    * 8655 gasPower, higher sample rate: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/feedforward/8655%20gasPower%20higher%20resolution.ipynb)
  * Hyper parameter optimization  
  Notebook that tries out different network architectures and shows all the results. This can be used to evaluate and choose between different architectures and hyperparameters. 
    * Hyperparameter optimization (Only feedforward for now 29-10-2018): [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/Hyperparameter%20optimization.ipynb)
  * LSTM  
  Notebook used to learn how LSTM time series prediction works.
    * (!) 8655 RNN LSTM: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/LSTM/8655%20RNN%20LSTM.ipynb)
  * sequence to sequence  
  Notebook used to learn how sequence to sequence time series prediction works.
    * 8655 seq2seq: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/seq2seq/8655%20seq2seq.ipynb)
    * General seq2seq: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/seq2seq.ipynb)
   * Opschaler LSTM & seq2seq main  
   These notebooks contain the currently (29-10-2018) being used deep learning models. There also is a notebook where the input data shape of LSTM has been analyzed. This has made because it was quite unclear how this actually was done, dispite reading a lot of literature about it.  
     * (!) LSTM data preperation: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/LSTM%20data%20preperation.ipynb)
     * (!!) LSTM & seq2seq for gasPower prediction: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/LSTM.ipynb)
       * Results  
       Pictures of current results. For 'single layer LSTM' a single LSTM input layer of size 35 has been used. The input data is of an hourly sample rate. The previous 5*24 samples have been used as timesteps (also known as look back). The mean of gasPower from all dwelling from `all_dwellings_combined_hour.csv` per datetime value has been taken. Avarage error is the average percentage difference between the predicted and true value. The original images can be downloaded to get view them in high resolution.  
          * Single layer LSTM result with a hourly sample rate: <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/LSTM%20result%20hourly%2029-10-2018.png"> </p>
          * Single layer LSTM result with a daily sample rate: <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/LSTM%20result%20hourly%20resampled%20to%20daily%20by%20sum%2029-10-2018.png"> </p>
          * Sequence 2 sequence with a hourly sample rate: <p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/seq2seq%20result%20hourly%2029-10-2018.png"> </p>
          * Sequence 2 sequence with a daile sample rate: still need to create this
          
**Note about shared work:** `PyCharm: Data preperation main script` and `Dask: Dask data processing` contain functions which were made by other group members. Some of these functions (NaN figure for example) have been adapted and changed by me. Besides that, all listed notebooks are made by me.

### GitHub repositoy: Multivariate Time Series Models in Keras
Once the model complexity in Keras kept increasing, i had to think of a way to keep my peers up to date with how all the models work. Along with this, i experienced that it is a great struggle to learn about time series models when starting with no knowledge about them at all. Needing to use Google for weeks and combining the information from tons of resources is a huge hassle for anyone.  

Therefor i created the repository [Multivariate Time Series Models in Keras](https://github.com/deKeijzer/Multivariate-time-series-models-in-Keras), which contains all the models from this project along with an explanation per model. This repository is ment for anyone that has no knowledge about OPSCHALER, it should give a throughout explanation on how each model has been established and why certain choices have been made. The repository contains the following notebooks, they are certainly worth a look (alongside with the repository in general, [link](https://github.com/deKeijzer/Multivariate-time-series-models-in-Keras)). It is adviced however to look at the notebooks using Jupyter (click: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/deKeijzer/Multivariate-time-series-models-in-Keras/master)) and browse to the `notebooks` folder.  

- [1. EDA & Feature engineering](https://github.com/deKeijzer/Multivariate-time-series-models-in-Keras/blob/master/notebooks/1.%20EDA%20%26%20Feature%20engineering.ipynb)  
- [2. MVLR](https://github.com/deKeijzer/Multivariate-time-series-models-in-Keras/blob/master/notebooks/2.%20MVLR%20.ipynb)  
- [3. DNN](https://github.com/deKeijzer/Multivariate-time-series-models-in-Keras/blob/master/notebooks/3.%20DNN.ipynb)  
- [4.1 CNN & RNN Data Preperation](https://github.com/deKeijzer/Multivariate-time-series-models-in-Keras/blob/master/notebooks/4.1%20CNN%20%26%20RNN%20Data%20Preperation.ipynb)  
- [4.2 LSTM](https://github.com/deKeijzer/Multivariate-time-series-models-in-Keras/blob/master/notebooks/4.2%20LSTM.ipynb)  
- [4.3 GRU](https://github.com/deKeijzer/Multivariate-time-series-models-in-Keras/blob/master/notebooks/4.3%20GRU.ipynb)  
- [5.1 Multivariate time-series to images](https://github.com/deKeijzer/Multivariate-time-series-models-in-Keras/blob/master/notebooks/5.1%20Multivariate%20time-series%20to%20images.ipynb)  
- [5.2 CNN](https://github.com/deKeijzer/Multivariate-time-series-models-in-Keras/blob/master/notebooks/5.2%20CNN.ipynb)   
- [6. TimeDistributed(CNN)+RNN+DNN](https://github.com/deKeijzer/Multivariate-time-series-models-in-Keras/blob/master/notebooks/6.%20TimeDistributed(CNN)%2BRNN%2BDNN.ipynb)  

Note that the repository also contain `Hyperas MODEL_NAME.py` files. These are Python scripts that use [Hyperas](https://github.com/maxpumperla/hyperas) (which is a wrapper around Hyperopt), for hyperparameter optimization and architecture space evaluations. One example on the usage of Hyperas can be found [here](https://github.com/deKeijzer/Multivariate-time-series-models-in-Keras/blob/master/notebooks/Hyperas%20CNN.py). The total amount of space evaluations is set so it takes about 24 hours per model, running on a system that has an Intel i7-6700HQ CPU and NVIDIA GeForce 960M GPU.

## Scrum
`TODO: Don't link individual tickets, possibly show a screenshot of each task board.`  
`TODO: Combine these tickets with the notebooks. `  
`TODO: Say that after week 10 we stopped using Scrum due to it not being particulary usefull (in the way it should be used) for our research.`  
The guidelines set up by the minor make it mandatory to use Scrum. We are doing small sprints with a length of 2 weeks. Personally I like to do the most throughout documentation in GitHub with for example commits. However, I did use Scrum to document my time spend on tasks related to the minor.  
* [Sprint 1](https://www.scrumwise.com/scrum/#/taskboard/sprint/sprint-1/id-84641-11359-18)  
It seems that a lot of Scrum tickets are missing.
  * (3h) Datacamp course 1+2
  * (2h) Visualizing practise data: create practise data for the group, to create visualizations from.
* [Sprint 2](https://www.scrumwise.com/scrum/#/taskboard/sprint/sprint-2/id-84641-11359-120)  
It seems that a lot of Scrum tickets are missing.
  * (14h) Cleaning data
* [Sprint 3](https://www.scrumwise.com/scrum/#/taskboard/sprint/sprint-3/id-84641-11359-158)
  * (7.5h) NaN information per dwelling, one large table
  * (33h) Datacamp KB-74 assignments
  * (4h) NaN streak checker function
  * (5h) NaN checker plot function
  * (4h) EDA on dwelling P01S01W8655
  * (3h) Correlation heatmaps of all dwellings
  * (2h) EDA + multi variate regression on all dwellings
  * (8h) Prepare dwelling dataframes (unprocessed)
  * (1h) Combine dataframes (smartmeter, weather)
  * (20h) Prepare dwelling dataframes (processed)
  * (5h) Prepare high resolution weather df
  * (2h) GitHub README: document important notebooks & datalocations
  * (1.5h) Create two files which contain all the 'combined_gas_smart_weather_dfs'
  * (2h) Correctly document my own Scrumwise tasks
  * (8h) Preprocessing data for deep learning
* [Sprint 4](https://www.scrumwise.com/scrum/#/taskboard/sprint/sprint-4/id-84641-11393-72)  
A lot of time has gone into certain tasks due to searching for literature, reading literature and learning how certain things should be done.
  * (7.5h) NaN information per dwelling, in one large table
  * (8h) Preprocessing data for deep learning
  * (35h) Basic LSTM & seq2seq
  * (35h) Feedforward NNs
  * (8h) Hyperparameter optimazation
  * (18h) Preprocessing for LSTM

## Other
Other contributions to the project and/or learning progress, worth mentioning.

### GitHub
Introduced the group to GitHub and made some resources that help with the setup and usage of GitHub at the datascience server. It can be clearly seen when KB74-OPSCHALER has been started, as pointed out by the red arrow below. 

<p align="center"> <img src="https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/github_start_of_opschaler.png"> </p>

* Setup a GitHub environment for the project, plus keep maintaining it: [link](https://github.com/deKeijzer/KB-74-OPSCHALER)  
* Made a README for the project members containing information on how to setup GitHub on the datascience server, plus general important information about the project: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/README.md)  
* Made a GitHub push & pull tutorial: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/GitHub%20push%20%26%20pull%20tutorial.ipynb)  
* Created .bat files to run [jupyter lab](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/jupyterlab.bat), [run notebooks](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/run_notebook.bat) and do [ssh portforwarding](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/ssh%20portforward.bat) for usage at your local computer.

### New datascience server
...
