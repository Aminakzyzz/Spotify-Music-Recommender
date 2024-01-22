Ziehm, Leander, 22201349

Akziz, Amin, 22207319

Spotify Music Recommender

https://mygit.th-deg.de/lz24349/assistance-systems-recommendation-system


!!!!!!!!!!!! TODO PUT ACTUAL INFORMATION ON THE WIKI SO IT"S NOT SO EMPTY!!!!!!!!!!!!

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

!!!!!!!!! TODO: It describes what part of the code implements a request of the project.!!!!!!!!!

Part 02 Requests
Create a PyQt6 application that implements the following requests:
• A Desktop App with PyQT6 has to be developed.
• A requirements.txt file must be used to list the used Python modules.
• A README.md file must be created with the structure described in part 01.
• The module venv must be used.
• A free data source must be used. You may find it for example at Kaggle, SciKit (but not the built-in
ones), or other.
• There must be a data import (predefined format and content of CSV).
• The data must be read from a file after clicking on a (menu) button or directly after starting the app.
• The data must be analyzed with Pandas methods, so that a user gets on overview.
• You may use the functions dataframe.info(), dataframe.describe() and/or dataframe.corr()
for that.
• You may also use other metrics or diagrams to do this.
• Create several input widgets (at least 3, where 2 must be different) that change some feature variables.
• A Scikit training model algorithm (e.g. from Aurélien Géron, Chapter 4) must be applied.
• Create 1 or 2 output canvas, i.e. for data visualization
• At least 3 statistical metrics over the input data must be shown
• The app must react interactively to the change of input parameter with a new prediction with visual-
ization.





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
