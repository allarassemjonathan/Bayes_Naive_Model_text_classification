# Bayes_Naive_Model_text_classification


Following is the statement of the problem: “Given a document, can we classify it in its appropriate category”?”               
The approach is to look at each category as a cause behind a certain document and the set of word in the document as the observables. Assuming that we will try to compute the expression in (1) for every single category. 
We assume the uniformity of the priors which means that all the elements of t are equally likely to produce the set of observables. We assume that the words occur independently from each other. Hence the presence of one word in a document does not at all impact the presence of another (which is not true obviously). For the causes, we assume that no two hypotheses can be true at the same time which is also not true since we can have articles that are about politics and sport at the same time for example. 

We learn the posteriors probabilities distribution by counting the number of words occurring in each document and removing the stop words. We end up with a probability distribution for each of our topic, a sort of table that map the probabilities of word occurring with the condition of it being used in that topic. 
For example, after iterating through 20 we have the following distribution of words depending on the topic:
<img src="https://github.com/allarassemjonathan/Bayes_Naive_classifier/blob/main/PictureBayesian.png">



