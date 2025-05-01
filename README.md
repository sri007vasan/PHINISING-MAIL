<h1>PHINISING-MAIL</h1>

In this project i have created a Machine Learning model using Logistic Regression for classification of legid and phinising mail.i have attached the collab file where i have trained the LR model and then saved the model in a.pkl file.Then i have used the trained model to make a user interface for it so that the project becomes user friendly and easy to use.

The below image shows the user interface of the project 
![FRONT END](https://github.com/user-attachments/assets/d0f4fbda-1c07-4e41-8489-16dd406b97de)

<h1>Model Training </h1>
Firstly i have used mail_data.csv as the dataset and i have attached the dataset in this github folder.Then by importing the necessary libraries and data pre-processing i have created the test and training dataset for the model.
Then i have imported the Logistic Regression model and trained it with the training dataset(80% of origional dataset).
After the model gets trained i have saved it in the .pkl folder and saved it in my local computer disk for implementing this project with a good user interface created by flask.

<h1>Using Flask</h1>
firstly after training the model using google colab i have used Flask feature from python for hosting a webapp. I have created a user interface in a folder names templates and kept my UI inside that folder and named it as index.html.Then i have combined the model,UI using the Flask and have successfully created a localhost

So, once after clicking the run button the wesite is shown  and by clicking that we can reach to the UI page
In the enter the message button you can enter the email that you are doubted of and click the classify button to know the result 

<h1>DEMO VIDEO</h1>

