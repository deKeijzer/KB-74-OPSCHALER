Last update: 29-10-2018

# Personal portfolio
Student name: Brian de Keijzer  
Student number: 16011015


## Online courses
Onlince courses from both DataCamp and Coursera have been followed for this minor.

### DataCamp
![DataCamp progress](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/datacamp_profile.png)
One of my personal goals is to finish the [Data Scientist with Python](https://www.datacamp.com/tracks/data-scientist-with-python) track on DataCamp. Apart from this I also did some other courses which seemed usefull for project Opschaler. All mandatory courses for the minor have been finished.

Completed courses (not in order):  
[Intro to Python for Data Science](https://www.datacamp.com/statement-of-accomplishment/course/01e115bd07164cd840cc41c7fe831ba08d7dca1a)  
[Intermediate Python for Data Science Course](https://www.datacamp.com/statement-of-accomplishment/course/246fecb0b112d881f24131944063f3345cbb70d8)  
[Python Data Science Toolbox (Part 1) Course](https://www.datacamp.com/statement-of-accomplishment/course/d07e9a26136fd801656e94bd39049247602fbce1)  
[pandas Foundations Course](https://www.datacamp.com/statement-of-accomplishment/course/95341cab0c49de075afc345533b945176bb92f41)  
[Supervised Learning with scikit-learn Course](https://www.datacamp.com/statement-of-accomplishment/course/8cf4bedbf7fc5cb2d81cf69a97e634fc818cd7a7)  
[Importing Data in Python (Part 1) Course](https://www.datacamp.com/statement-of-accomplishment/course/2e6d0dde86e189b3b79328a823104b3937c57b56)  
[Deep Learning in Python Course](https://www.datacamp.com/statement-of-accomplishment/course/c90ac629566673ede129fa1e18fd4e42764cc702)  
[Python Data Science Toolbox (Part 2) Course](https://www.datacamp.com/statement-of-accomplishment/course/f88ff03b0c3bd4f71781cff692a3cbaed61a4be7)  
[Cleaning Data in Python Course](https://www.datacamp.com/statement-of-accomplishment/course/7a1c78cc670415289136447878822899ac968543)  
[Introduction to Data Visualization with Python Course](https://www.datacamp.com/statement-of-accomplishment/course/75b9fd93c583c0c0131106ef05b1a52515ccf0e2)  
[Manipulating DataFrames with pandas Course](https://www.datacamp.com/statement-of-accomplishment/course/24164e462d63070611fc45ff9349836c3f196551)  
[Importing Data in Python (Part 2) Course](https://www.datacamp.com/statement-of-accomplishment/course/824adfac50d7835387dc9509863ec42aef63ee16)  
[Statistical Thinking in Python (Part 1) Course](https://www.datacamp.com/statement-of-accomplishment/course/9f6cd5082511ecb5d6b7c6bf9fd053350d3c13af)  
[Introduction to Databases in Python Course](https://www.datacamp.com/statement-of-accomplishment/course/bc8bc8a89124619d48d6338aab461c6177825c1d)  
[Merging DataFrames with pandas Course](https://www.datacamp.com/statement-of-accomplishment/course/673dba72c544df4b977cf6b555d2d6799f81f33e)  
[Interactive Data Visualization with Bokeh Course](https://www.datacamp.com/statement-of-accomplishment/course/0b559a1d25a6f3b1260f248838d6f968b22ed727)  
[Statistical Thinking in Python (Part 2) Course](https://www.datacamp.com/statement-of-accomplishment/course/14f7db481ac78649805ff20d36355693157f2fce)  
[Preprocessing for Machine Learning in Python Course](https://www.datacamp.com/statement-of-accomplishment/course/f43c37bfe1b7b90f0d9997ea180470e43c8d0b08)  
[Parallel Computing with Dask Course](https://www.datacamp.com/statement-of-accomplishment/course/2c005dbb8743cd4210165c2326863f2dddc5ded7)  


### Coursera: Machine Learning by Stanford University
![Coursera progress](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/coursera_progress.png)  
Did not do a lot of Coursera yet, am planning on finishing it within 7 days from now (29-10-2018).

## Jargon
Used jargon for Opschaler is used below.
* Dwelling: a unique house.  
* Smartmeter data: electricity and gas meter data.   
* gasPower: amount of gas being used at a given time.
* ePower: amount of electricity being used at a given time.
* smart: electricity DataFrame of a dwelling.
* seq2seq: sequence to sequence
* LSTM: long short-term memory


## Friday presentations  
-


## Python notebooks
All notebooks have been well commented, apart from lines where the programming is basic Python (for data science).
Besides commenting code, i try to document all changes by committing small changes to GitHub.  
![github_commits](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/appendix/github_commits.png)  

Quite a lot of notebooks which are relevant for Opschaler have been created. Most started out as smaller notebooks, to learn the programming techniques required for the job. Later on a lot of the smaller notebooks have been combined in larger notebooks.  
In general several notebooks have been created for Opschaler (listed mainly in order or creation):  

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
    * Data preperation main notebook: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/data_preperation_main.ipynb)
    * Loading combined smart, gas and weather generalized notebook: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/loading_combining_smart_gas_weather_generalized.ipynb)
    * Creating one DataFrame for all dwellings: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Data_preperation/Create%20one%20df%20for%20all%20dwellings.ipynb)

* KNMI  
In these notebooks the 10 minute resolution weather data is processed. This data has been received by mail from the KNMI. The raw data consists of a folder with multiple `.csv` files. There are different file types depending on the measured variables and the year in which the values were measured.  
  * Combining DataFrames: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/KNMI/1.KNMI_high_resolution_combining_dfs.ipynb)
  * Cleaning DataFrames: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/KNMI/2.KNMI_high_resolution_cleaning_df.ipynb)
  * Exploratory Data Analysis (EDA): [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/KNMI/KNMI%20visualization.ipynb)

* EDA  
Notebooks that contain general EDA on the created DataFrames which contain all the combined raw data per dwelling. Plus a table containing usefull information per dwelling has been created. 
  * EDA on dwelling P01S01W8655: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/EDA/EDA%20on%20dwelling%20P01S01W8655.ipynb)
  * Raw dwelling information table: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/EDA/Raw%20dwelling%20information%20table.ipynb)
  * Reading in all dwellings, plus making correlation matrices: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/EDA/reading%20in%20%26%20correlation%20matrices%20on%20processed%20data.ipynb)
  
* PyCharm  
The 'data_preperation_main.py' file used to be the main script to create the prepared dwelling data. Later on Dask has been implemented due to having improved performance because of being able to parallelize tasks on multiple CPU cores.  
  * Data preperation main script: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/EDA/reading%20in%20%26%20correlation%20matrices%20on%20processed%20data.ipynb)
  * Data preperation main test notebook: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/pycharm/data_preperation_main_test_notebook.ipynb)
  * EDA on processed data: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/pycharm/EDA%20on%20processed%20data.ipynb)
 
* Dask  
Currently (29-10-2018) this is the main notebook for all the data processing done for the Opschaler project. This notebook has implemented most relevant functions from previously listed notebooks in a way so they can be run in parallel with Dask. It basically takes all raw data and saves unprocessed and processed (NaNs taken care off) `.csv` files per dwelling, which can be used for analysis.
  * Dask data processing: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Dask/Dask%20data%20processing.ipynb)

* Keras  
This folder contains all the notebooks related to deep learning. Note that there are multiple notebooks being very similar to each other. Sometimes the only difference inbetween similar notebooks are changes in settings (nodes, layers and selected dwellings). Most notebooks start off with EDA to check if the correct data is being used, then the model is being created and evaluated.
  * Feedforward
    * All dwellings EDA + machine learning: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/feedforward/all%20dwellings%20EDA%20%2B%20machine%20learning.ipynb)
  Notebooks containing feedforward models.
    * 8655 gasPower, sample rate 1 day: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/feedforward/8655%20gasPower%201D.ipynb)
    * 8655 gasPower, higher sample rate: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/feedforward/8655%20gasPower%20higher%20resolution.ipynb)
  * LSTM  
  Notebook used to learn how LSTM time series prediction works.
    * 8655 RNN LSTM: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/LSTM/8655%20RNN%20LSTM.ipynb)
  * sequence to sequence  
  Notebook used to learn how sequence to sequence time series prediction works.
    * 8655 seq2seq: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/seq2seq/8655%20seq2seq.ipynb)
  * Hyper parameter optimization  
  Notebook that tries out different network architectures and shows all the results. This can be used to evaluate and choose between different architectures and hyperparameters. 
    * Hyperparameter optimization (Only feedforward for now 29-10-2018): [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Brian/Keras/Hyperparameter%20optimization.ipynb)


**Note about shared work:** `PyCharm: Data preperation main script` and `Dask: Dask data processing` contain functions which were made by other group members. Some of these functions (NaN figure for example) have been adapted and changed by me. Besides that, all listed notebooks are made by me.

## Scrum
-

## Other
Other contributions to the project / learning progress, worth mentioning.

### GitHub
Introduced the group to GitHub and made some resources that help with the setup and usage of GitHub at the datascience server. 

* Setup a GitHub environment for the project, plus keep maintaining it: [link](https://github.com/deKeijzer/KB-74-OPSCHALER)  
* Made a README for the project members containing information on how to setup GitHub on the datascience server, plus general important information about the project: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/README.md)  
* Made a GitHub push & pull tutorial: [link](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/GitHub%20push%20%26%20pull%20tutorial.ipynb)  
* Created .bat files to run [jupyter lab](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/jupyterlab.bat), [run notebooks](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/run_notebook.bat) and do [ssh portforwarding](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/ssh%20portforward.bat) for usage at your local computer.
