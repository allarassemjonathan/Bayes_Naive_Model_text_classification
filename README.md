# Bayes_Naive_Model_text_classification


Following is the statement of the problem: “Given a document, can we classify it in its appropriate category”?”               
The approach is to look at each category as a cause behind a certain document and the set of word in the document as the observables. Assuming that we will try to compute the expression in (1) for every single category. 
We assume the uniformity of the priors which means that all the elements of t are equally likely to produce the set of observables. We assume that the words occur independently from each other. Hence the presence of one word in a document does not at all impact the presence of another (which is not true obviously). For the causes, we assume that no two hypotheses can be true at the same time which is also not true since we can have articles that are about politics and sport at the same time for example. 

From Bayes formula we can derive the expression to maximaze:
<img src="[https://latex.codecogs.com/png.image?1+sin^2(x)](https://latex.codecogs.com/svg.image?P(t|w)&space;=&space;\alpha&space;\prod_{j}^{n}P(w_{j}|t)&space;&space;=>&space;log(P(t|w))&space;=&space;\alpha&space;\sum_{j}^{n}&space;log(P(w_{j}|t))&space;)"/>



