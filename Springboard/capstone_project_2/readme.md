This project explores Donald Trump Tweets with NLTK sentiment analysis and Gensim topic extraction. 

For replication, start with “data_wrangling.pdf," then "sentiment.ipynb", and "finally topic_extraction.ipynb". A presentation for general audiences is provided under "Final_Presentation.pptx". A more technical discussion is available in the paper "capstone_2_final_paper".  

"Final_Presentation.pptx" : Powerpoint for general audiences discussing the project process and results.

"capstone_2_final_paper" : Paper discussing the technical results of the project.

The data for the project was obtained using code by Jeremy Cunningham here:
https://github.com/j2cunningham/GetOldTweets-python

"sentiment.ipynb" :  Is a Jupyter notebook that imports the scrapped csv files. Cleans the data and applies NLTK's sentiment      analysis to Donald Trump tweets and tweets from 4 major news broadcasters. The data is then visualized for interactive exploration with Bokeh. 

"topic_extraction.ipynb" : Is a Jupyter notebook that picks up after "sentiment.ipynb". This notebook contains the topic extraction. Topic extraction was done with Gensim's LDA transformation. The hyper-parameters were tuned using SKLearn's clustering algorithms. The data was then visualized using Bokeh for interactive exploration. 

papers : Is a folder holding idea selection and mid-project papers.

"data_wrangling.pdf" Is a paper explaining the data collection steps, how to download the data yourself, and contact instructions if you just want the csv files. 
