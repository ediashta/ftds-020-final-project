# **Final Project - Customer Churn Classification and Clustering**

**Ediashta Revindra Amirussalam** <br>
FTDS - 020 - RMT

## 01. Dashboard
Dashboard link - [Hugging Face](https://huggingface.co/spaces/Ediashta/CreditCardChurnPrediction-FinalProject)

## 02. Project Description

An attrited customer, also known as a churned customer, is a business term that refers to a customer who has discontinued doing business with a company or organization. This could indicate that they have canceled their subscription, stopped purchasing products or services, or otherwise terminated their relationship with the company.

Customer attrition, or churn, is an important metric for businesses to track because it has a direct impact on revenue and growth. Customer attrition rates that are high may indicate issues with customer satisfaction, service quality, or competition. Retaining existing customers is often less expensive than acquiring new ones, so businesses typically invest time and effort in determining why customers leave and implementing strategies to reduce attrition and retain valuable customers.


In this task, we will build a model to predict customer churn classification and then cluster churned customers using the following model:

**Classification**
* SVC
* Decision Tree
* Random Forest
* XGBoost

We will use recall as the primary evaluation metric. In the context of churn prediction, false negatives could result in missing actual churn cases, which is undesirable. By optimizing recall, the model aims to capture a higher proportion of actual churn cases, reducing the risk of misclassifying customers who are actually about to churn.

**Clustering**
* K-Means

We can see the behavior of our churning customers and advise a strategy to maintain them as customers based on their cluster.

## 03. Project Results

### Modeling
From the 4 model we have tested, the best model we get is XGBoost with following parameter:
* **learning_rate** : 0.1
* **max_depth** : 3
* **n_estimators** : 100
* **subsample** : 0.9

The performance of the model is as follow:
|   | precision | recall | f1-score  | support |
|---|---        |---     |---        |  ---     |
|           | 0 | 0.98 | 1.00 | 0.99 | 2551 |
|           | 1 | 1.00 | 0.98 | 0.99 | 2549 |
|    accuracy |   |   | 0.99 | 5100 |
|   macro avg | 0.99 | 0.99  | 0.99  | 5100 |                    
|weighted avg | 0.99 | 0.99  | 0.99  |  5100 |                     

**Precision**
* For class 0, the precision is 0.98, and for class 1, it's 1.00. 
* Precision indicates how many of the instances predicted as a certain class are actually that class. In this case, for class 0, out of all instances predicted as class 0, **98% are truly class 0**. For class 1, **100% of predicted class 1 instances are truly class 1**.

**Recall** 
* For class 0, the recall is 1.00, and for class 1, it's 0.98. 
* Recall indicates how many of the actual instances of a certain class were correctly predicted as that class. In this case, for class 0, **100% of actual class 0 instances were correctly predicted**, and for class 1, **98% of actual class 1 instances were correctly predicted**.

**Accuracy** 
* The overall accuracy of the model is 0.99, which means that the model's predictions were correct for approximately 99% of the instances.

In summary, this classification report indicates that the model has achieved high precision, recall, and F1-score for both classes, suggesting strong performance in correctly classifying instances from both classes. The overall accuracy of 99% further supports the model's effectiveness.

However, even our classification model performance is already excellent, it still can be improved a little bit for the clustering. there are several things worth to note for our clustering model.
* The model still had difficulties in cluster on the data given, it might need more data
* The characteristic of each cluster are not clearly defined and have many overlapping characteristics
* We need to improve the feature selection for our clustering to make sure we get a good result on sillhouete score

### Business
Here are some recommendations to help reduce churn among customers in both low and high credit limit clusters:

#### For Cluster 1 - Customers with High Credit Limit:

* **Rewards and Recognition**: Offer loyalty rewards, discounts, or exclusive perks to incentivize them to continue using your services. Recognize their high-value status and show appreciation.
* **Tailored Financial Solutions**: Provide personalized financial solutions like investment advice, premium account services, or tailored credit options that align with their financial goals.
* **Financial Education**: Offer educational resources to help them make informed financial decisions. Webinars, articles, and workshops can empower them to manage their wealth more effectively.

#### For Cluster 2 - Customers with Low Credit Limit:

* **Improved Credit Opportunities**: Provide opportunities for customers to increase their credit limit based on responsible financial behavior over time. This can help them meet their financial needs without the frustration of a low limit.

* **Value Proposition**: Communicate the value of your services to this cluster. Offer them benefits that resonate with their needs, such as simplified account management, digital tools, and cost-saving features.
* **Fee Structure Review**: Review and optimize fee structures for this cluster. Consider offering fee waivers or lower minimum balance requirements to make your services more accessible.
* **Financial Planning Assistance**: Provide financial planning resources to help them make the most of their resources. Empower them to grow their financial health and eventually move into higher-spending categories.

As for general churned customer, here are some advised recommendation:
* **Exit Surveys**: Conduct exit surveys to understand why customers left. Use their feedback to address pain points and improve services to prevent future churn.
* **Win-Back Campaigns**: Identify and reach out to churned customers with targeted win-back campaigns. Offer them incentives to return, such as fee waivers, exclusive offers, or improved account terms.

*We need to take a note that a comprehensive approach is essential. Each recommendation should be aligned with Danamon Bank business's goals, values, and customer segments. Continuously analyze the effectiveness of your strategies and adapt as necessary to keep your customers engaged and satisfied.*