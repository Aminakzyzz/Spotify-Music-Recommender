Ziehm, Leander, 22201349

Akziz, Amin, 22207319

Spotify Music Recommender

https://mygit.th-deg.de/lz24349/assistance-systems-recommendation-system

https://mygit.th-deg.de/lz24349/assistance-systems-recommendation-system/-/wikis/home

# Project description

This application serves as a personalized musing recommender using the Spotify API. Users input an input song and adjust some parameters through sliders to tailor the recommendations to their own preferences. The application generates a list of 10 recommended songs, presenting aswell detailed information in a table layout. A visual representation of the input song and the recommendations is displayed though a plot. The layout enhances user experience and provides a user-friendly interface for discovering new music.


# Prerequisites

This was tested in python versions 3.12.1 and 3.9.0

This are the libraries saved in the "requirements.txt": (They shoudn't need any specific version)

- PyQt6
- pandas
- matplotlib
- numpy
- scikit-learn
- requests

# Installation

git clone https://mygit.th-deg.de/lz24349/assistance-systems-recommendation-system.git

**Ubuntu/Linux:**

1. python3 -m venv ./venv
2. source ./venv/bin/activate
3. pip install -r requirements.txt 


**Windows:**

1. python -m venv musicRecommenderVenv
2. musicRecommenderVenv\Scripts\activate.bat
3. pip install -r requirements.txt

# Basic Usage

To launch the application, run "python main.py".
Start giving an input song and press the button "Get Song Data". 
Once the song data loads, adjust the parameters "Danceability, Tempo, Popularity and Energy" using the provided sliders.
Subsequently after pressing the "Recommend" button, wait for some seconds and explore the recommended songs displayed in the table, accompanied by detailed information.
Visualize the relationship between the input song and recommendations in the plot.



# Implementation of the Requests

At first, we searched for a data source on Kaggle and found a Spotify Song Dataset. 

We downloaded it and implemented the data loading directly after the user executes the main.py file. The actual csv data loading logic is contain, loaded recomendationskNrearest.py script, which gets triggered as it is imported in main.py.

We analyzed our dataset using Pandas functions like dataframe.info(), dataframe.describe() and dataframe.corr(). The output can be also be found on the wiki on GitLab.

After analyzing we chose to use K-nearest neighbors instead of linear regression due to the amount of loosely connected data in the data set. To still get a well-informed and useful recommendation to the user, we retrieve metadata about songs the user searches for using the Spotify Api in the mySpotify.py script. We use this data in combination with the dataset to train and fit the scikit algorithm to the data using K-nearest neighbors. The output from this training and recommendation, we plot a diagram in the plotManager.py script to show a visual representation of the data and its distances to the user. This diagram gets then visualized in our application. Additionally, the user also gets the distances of each recommeded song compared to the originally searched song. 

After that, we developed a desktop application using python and PyQT6. The user can search using the two three widgets: search bar represented by QLineEdit, multiple sliders represented by QSlider, and two buttons represented by QPushButton. Our app interactivly reacts to the user's input, firstly by adjusting the slider values automatically after a user searched for a song and metadata got retrieved from the Spotify Api. The second way our ui changes is after each recommendation diagram changes and new data gets filled in the output table represented by a QTableWidget.



# Work done

Amin Akziz:

1. Graphical User Interface
2. Pandas with Numpy

Leander Ziehm:

3. Visualization
4. Scikit-Learn

Both: 7) General Python Programming.

# Additional Descriptions

The application is composed of other four files:

- main.py contains all the user interface and connects the sliders to the recomender system.

- mySpotify.py interacts with the spotify api to search and retrieve the song metadata to update the sliders.

- plotManager.py generates the plot shown in the user interface.

- recomandationskNrearest.py implements k-nearest neighbors algorithm to privide recomendations for similar songs to the given one in the input, based on specified parameters.
