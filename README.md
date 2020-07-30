# SACATE

An easy-to-navigate website which can be used to donate food/clothes to the distribution centres as well as a direction to the well-funded PMCARES charitable trust.  You can always interact with our chatbot to know more about the COVID-19 pandemic and keep up-to-date with current happenings.


## Steps

1. Clone this repository to your local.

2. Open the project in an editor of your preference.

3. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

    ```bash
      pip install django
    ```
4. Run your server

   ```bash
      python manage.py runserver 
    ```
   or, the below command if your default python version is python2 use [python3](https://www.python.org/downloads/)

    ```bash
      python3 manage.py runserver 
    ```

5. Your server should be up and running now.




## SACBOT SERVICE AND SLACK
We provided two options for normal User to clarify their doubts. Both of them is discussed below. We have used **IBM Service** for Chatbot Services

+ **SACBOT**
        
    This is a BOT which will answer your all your Doubts regarding our Motive and guide you to Donation method. Also this BOT can give you Information about COVID 19  
  

+ **SLACK** 

  If normal user have any question or complain, then they can contact us in Slack. We have also Integrated SACBOT in SLACK. Users can also interact to SACBOT in SLACK


## Tables

+ **User**

  This table contains details of all user and their role.

+ **Contact** 

  This table contains queries that enduser will ask.

+ **DonatedCloth** 

  This table contains details of users and cloths donated.

+ **DonatedFood** 

  This table contains details of users and foods donated.


+ **NewsFeed** 

  This table contains message that donation camp wants to show to everyonw. Also it will contain thanks message by donation camp. It will motivate more perople to donate

+ **Notification** 

  This table contains details of users request.


## ABOUT DEPLOYMENT

   The Server is also hosted at [PythonAnywhere](https://www.pythonanywhere.com/). Click on the below links to use it directly from the hosted server.
   
   + [HOME PAGE](http://sac.pythonanywhere.com/)


   ***Note : All Data being used is dummy data.***
               


   **Thank You :)**
