# PERSONAL PORTFOLIO

This document gathers the most important steps taken during the Data Analisys course performed by the student Víctor García Romillo. With this document I pretend to reflect the knowledge acquired during the minor and the contributions I made to the Opschaler project.

## Datacamp courses

![Summary](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Vector/Resources_portfolio/Captura%20de%20pantalla%202019-01-10%20a%20las%2013.29.57.png)

I finished the mandatory courses that the minor assigns and I also took part in a Bokeh visualization course that helped me to develop one of my finished python notebooks.

![courses part 1](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Vector/Resources_portfolio/Captura%20de%20pantalla%202019-01-10%20a%20las%2012.32.56.png)
![courses part 2](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Vector/Resources_portfolio/Captura%20de%20pantalla%202019-01-10%20a%20las%2012.40.43.png)
![courses part 3](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Vector/Resources_portfolio/Captura%20de%20pantalla%202019-01-10%20a%20las%2012.40.53.png)
![courses part 4](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Vector/Resources_portfolio/Captura%20de%20pantalla%202019-01-10%20a%20las%2012.41.05.png)


## Coursera: Machine Learning by Stanford University
I have completed all mandatory Coursera courses. Green ticks are quizes taken. Programming assingments are not done. Sorry for language missmatch (Semana = Week, Cuestionario = Quiz, Preguntas = Questions).

![Coursera](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Vector/Resources_portfolio/coursera.png)

![1](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Vector/Resources_portfolio/Intro.png)<br/> 
![2](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Vector/Resources_portfolio/Linear%20reg%20with%20one.png)<br/> 
![3](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Vector/Resources_portfolio/Linear%20Alg.png)<br/>
![4](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Vector/Resources_portfolio/Linear%20reg%20with%20mult.png)<br/>
![5](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Vector/Resources_portfolio/octave.png)<br/>
![6](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Vector/Resources_portfolio/Logistic%20reg.png)<br/>
![7](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Vector/Resources_portfolio/Regularization.png)<br/>
![8](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Vector/Resources_portfolio/advice%20for%20ML.png)<br/>
![9](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Vector/Resources_portfolio/ML%20syst%20design.png)<br/> 


## Friday Presentations

This is the list of the presentations we created until the moment (4-11-2018):

[Week 1](https://prezi.com/p/28wycwuqqggc/#present): All the group edited this presentation.<br/>
[Week 2](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/appendix/friday%20presentations/7-9-2018.pptx): presented by Víctor Gómez and me.<br/>
[Week 4](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/appendix/friday%20presentations/21-09-2018.pptx): presented by Brian de Keijzer and me.<br/>
[Week 5](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/appendix/friday%20presentations/28-09-2018%20(TU%20delft%20meeting).pptx): presented by Daan Boesten and me.<br/>
[Week 6](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/appendix/friday%20presentations/05-10-2018.pptx): presented by Daan Boesten and me.<br/>
[Week 10](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/appendix/friday%20presentations/02-11-2018%20(1).pptx): presented by Daan Boesten and me.<br/>
[Week 13](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/appendix/friday%20presentations/Opschaler%20partners%20presentation%20%20at%20TU%20Delft%20(13-11-2018).pptx): presented by Brian de Keijzer and me at TU Delft.<br/>
[Week 14](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/appendix/friday%20presentations/30-11-2018.pptx): presented by me.<br/>
[Week 17](https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/appendix/friday%20presentations/21-11-2018.pptx): presented by me.<br/>


## Python Notebooks 

These are the Python Notebooks I finished containing the code I wrote for the Opschaler project:

-Bokeh visualization (https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Vector/Bokeh_graphs.ipynb)
As we are working with a large dataset we needed a way to visualize and interact with a huge amount of data. This notebook is meant to represent information from the whole dataset, before and after processing it. It was helpful to identify NaN gaps so that the processing of data could fix this problem

-Gas biggest gap (https://github.com/deKeijzer/KB-74-OPSCHALER/blob/master/Personal_folders/Vector/gas_biggest_gap.ipynb)
After doing a visual inspection of data we identified a big number of gaps we had to deal with. Some of the gaps could be interpolated but some others were to big to do so. This notebook removes gap sizes bigger than a certain amount and also returns some important information abount the size of the file until the first big gap is found. This information is relevant to extract some periodicity patterns used later

-Hour of the day as feature  
In order to implement hours of the day as new features to feed the models new columns have to be created in dataframes. This notebook isn't finished yet, I'm currently working on it.

-Feed forward NN
Next step I'd like to work on is the creation of a feed forward NN. This has already been done by Brian de Keijzer but I'd like to replicate it to put in practice the knowledge I acquired in this area.
