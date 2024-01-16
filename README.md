# assistance-systems-recommendation-system

Ziehm, Leander, 22201349

Akziz, Amin, 22207319

Spotify Music Recommender

link to my git repository still

# Project description

This application serves as a personalized musing recommender using the Spotify API. Users input an input song and adjust some parameters through sliders to tailor the recommendations to their own preferences. The application generates a list of 10 recommended songs, presenting aswell detailed information in a table layout. A visual representation of the input song and the recommendations is displayed though a plot. The layout enhances user experience and provides a user-friendly interface for discovering new music.


# Installation

git clone https://mygit.th-deg.de/lz24349/assistance-systems-recommendation-system.git

**Ubuntu/Linux:**

1. python3 -m venv ./venv
2. source ./venv/bin/activate
3. pip install -r requirements.txt 


**Windows:**

1. python -m venv musicRecommenderVenv
2. windowsVenv\Scripts\activate.bat
3. pip install -r requirements.txt

# Basic Usage

To launch the application, run "python main.py".
Start giving an input song and press the button "Get Song Data". 
Once the song data loads, adjust the parameters "Danceability, Tempo, Popularity and Energy" using the provided sliders.
Subsequently after pressing the "Recommend" button, wait for some seconds and explore the recommended songs displayed in the table, accompanied by detailed information.
Visualize the relationship between the input song and recommendations in the plot.

# Work done

Amin Akziz:

1. Graphical User Interface
2. Pandas with Numpy

Leander Ziehm:

3. Visualization
4. Scikit-Learn

Both: 7) General Python Programming.

# requirements

This are the libraries saved in the "requirements.txt":

- PyQt6
- pandas
- matplotlib
- numpy
- scikit-learn
- requests

This was tested in python versions 3.12.1 and 3.9.0

# Additional Descriptions

The application is composed of other four files:

- main.py contains all the user interface and connects the sliders to the recomender system.

- mySpotify.py interacts with the spotify api to search and retrieve the song metadata to update the sliders.

- plotManager.py generates the plot shown in the user interface.

- recomandationskNrearest.py implements k-nearest neighbors algorithm to privide recomendations for similar songs to the given one in the input, based on specified parameters.
