# assistance-systems-recommendation-system

Ziehm, Leander, 22201349
Akziz, Amin, 22207319


Spotify Music Recommender

# Project description

This PyQt6-based desktop application serves as a personalized music recommender using the Spotify API. Users input a seed song and adjust parameters through sliders to tailor recommendations to their preferences. The application generates a list of 10 recommended songs, presenting detailed information in a tabular layout. A visual representation of the seed song and recommendations is displayed through an interactive plot. The unique layout enhances user experience, providing a user-friendly and intuitive interface for discovering new music.


# Installation

**Ubuntu/Linux:**

python3 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt 

**Windows:**

python -m venv musicRecommenderVenv
pip install -r requirements.txt

# Requirements

This are the libraries saved in the requirements.txt

- PyQt6
- pandas
- matplotlib
- numpy
- scikit-learn
- requests

This was tested in python versions 3.12.1 and 3.9.0

# Basic Usage

How to start the chatbot after installation is complete ()

Example of a typical conversation

# Implementation of the Requests


# Work done

Amin Akziz:
1) Graphical User Interface
2) Pandas with Numpy

Leander Ziehm:
3) Visualization
4) Scikit-Learn

Both: 7) General Python Programming.

2**

# Additional Descriptions

The application is composed of other four files:

- main.py contains all the user interface and connects the sliders to the recomender system.

- mySpotify.py interacts with the spotify api to search and retrieve the song metadata to update the sliders.

- plotManager.py generates the plot shown in the user interface

- recomandationskNrearest.py implements k-nearest neighbors algorithm to privide recomendations for similar songs to the given one in the input, based on specified parameters

