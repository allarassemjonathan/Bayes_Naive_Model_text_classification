# Bayes_Naive_Model_text_classification


Following is the statement of the problem: “Given a document, can we classify it in its appropriate category”?”    

The approach to solve the problem is simple. We have a finite set of topic that are the hidden variables acting on the words that are the observables. We can draw a simple Bayesian network to represent the interactions between the topics and the words. 

<img src="https://github.com/allarassemjonathan/Bayes_Naive_classifier/blob/main/PictureBayesian.png">

The task will be to maximize the value <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/6fe719eda4ce62ee2f2104455abc5233fdf69e01"> using the following equation:

<img src="https://github.com/allarassemjonathan/Bayes_Naive_classifier/blob/main/Equation(1).PNG">


We learn the posteriors probabilities distribution by counting the number of words occurring in each document and removing the stop words. We end up with a probability distribution for each of our topic, a sort of table that map the probabilities of word occurring with the condition of it being used in that topic. 
For example, after iterating through 20 we have the following distribution of words depending on the topic:
<img src="https://github.com/allarassemjonathan/Bayes_Naive_classifier/blob/main/PictureBayesian.png">



