Quick Force Python
==================

A Python version of [quick-force-node](https://github.com/jamesward/quick-force-node).
The quickest and easiest way to start a Python web app that uses the Force.com REST APIs.


### Usage

(This app works with both Python 2 and 3)

1. [![Deploy on Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
2. View the newly deployed application and follow the instructions to setup an OAuth Connected App in Salesforce and then set the config in your Heroku app
3. Setup a local development environment by downloading your app's source: https://download-heroku-source.herokuapp.com/
4. Unzip the archive and run command:

    ```
    $ pip install -r requirements.txt
    $ heroku local web
    ```

5. Check out the local app at: [http://localhost:5000](http://localhost:5000)
6. Again follow the instructions in your local app to setup another OAuth Connected App for local development
7. Make and test some local changes to the app
8. Deploy those changes from Atom using the Heroku menu (Login, then Deploy)
