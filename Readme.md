## HANDWRITTEN DIGIT RECOGNITION 
---
---
In this project i am using mnist dataset .it has set of 70,000 images and 784 feature.we say MNIST is a hello world in machine learning. it contain 28x28 pixel((white)0 to 255(black)).it is a classification problem.let's discuss how i approach toward this process.
i am follow mainly three step

* fetch the dataset using sklear library.
* Analysis the dataset and visualize the dataset using matplotlib library.
* train the model using logistic regression.

---

for fetching the dataset i am using:

```python
 from sklearn.dataset import fetch_openml
 MNIST=fetch_openml('mnist_784)
```

after that i am performing the analysis simply by shape discribe function.

In this dataset target feature and train feature has already spilted .60,000 for train feature and 10,000 for target feature.


for train the model i have used logistic regression

import logistic regression
```
from sklearn.linear_model import LogisticRegression
```
for checking the Accuracy
 i am using model selection

 ```
 from  sklearn.model_selection import cross_val_score 
 ```
 The Accuracy of this model that i have got is 95%.

