# Autinosis💙
An artificial intelligence algorithm to help speed autism diagnosis.
Website: millenaxavier.com/projects

Welcome to Autinosis GitHub repository. This is where all the components of the project are developed, reviewed and maintained.

Autinosis is algorithm to assist the screening process for autistic spectrum disorders using Machine Learning. This research focuses on observing data from autistic people and their behavioral patterns through data analysis and machine learning so that it is possible to recognize people with this disorder in all ages in a faster and more accessible form to the population.


**About the Problem**
The problem of the research is the lack of a satisfactory and accessible diagnosis for ASD, considering that from 2020 to 2022 the cases had an increase of 22% [8]. With this sporadic growth of the disorder, there is a huge lack of professionals and specialized centers able to make a proper diagnosis, in addition to the high cost and difficulty in obtaining treatment due to these factors, besides not being 100% accurate given the lack of specialization of some professionals in the area.

According to the research "Portrait of Autism in Brazil", about 2 million Brazilians are autistic. Even so, the carriers find it difficult to perceive the presence of ASD due to the lack of means of information dissemination about diagnostic medicine.

**About the Solution**
Based on the problems pointed out, the identification of behaviors of Autistic Spectrum Disorder through artificial intelligence would be facilitated and would make the diagnosis more effective. Thus, the research focuses on observing data from autistic people and their behavioral patterns through Machine Learning so that it is possible to recognize people with this disorder in a faster and more accessible form to the population. Thus, the research hypothesizes that Machine Learning methods would not only help evaluate the risk for Autism quickly and accurately but would also be essential to simplify the entire diagnostic process, making it less costly and reducing the stress patients and families deal with during too many clinical consultations.



**About the Data**
Name	Source	Test	Size (KB)
Child Dataset	Autism Screening for Toddlers	Q-CHAT-10	68.5
Adolescent Dataset	UCI Machine Learning Repository	AQ-10	14.5
Adult Dataset	UCI Machine Learning Repository	AQ-10	96.0


**Evaluation Results**
The screening process is evaluated using three metrics: accuracy, sensitivity and specificity.

Accuracy: The fraction of correct predictions over all the predictions
 

For the next metrics we are going to look at different ways of success and failure:

True positive: Neuroatypical patients who have been identified as having ASD traits.
False positive: Neurotypical patients who have been identified as having ASD traits.
True negative: Neurotypical patients whose ASD traits were not identified.
False positive: Neuroatypical patients whose ASD traits were not identified.
Sensitivity or Recall: Of all the neuroatypical patients (relevant elements), how many were we able to identify correctly?
 

Specificity or Recall of the negative class: Of all the neurotypical patients, how many were we able to identify correctly?
 

If the true status of the condition cannot be known, sensitivity and specificity can be defined relative to a "gold standard test" which is assumed correct. For all testing, both diagnostic and screening, there is usually a trade-off between sensitivity and specificity, such that higher sensitivities will mean lower specificities and vice versa.

 	Accuracy	Sensitivity	Specificity
Child	0.90	0.91	0.87
Adolescent	0.71	0.85	0.50
Adult	0.91	0.87	0.94
