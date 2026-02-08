Waste Management & Collection Dashboard

This project demonstrates how local governments can use machine learning and geospatial visualisation to optimise municipal waste collection. The dashboard highlights bins that will reach capacity soon, allowing city administrators to prioritise collection routes and allocate resources efficiently. The app is built with Streamlit and uses a synthetic dataset of bins across multiple cities.

Project Structure
File	Description
waste_bins_multi.csv	Synthetic dataset containing bins for three cities (Karachi, Lahore and Sargodha). Each record includes the bin’s location, capacity, current fill level, average daily waste increase and a calculated priority class (High/Medium/Low).
waste_dashboard.py	Streamlit app that loads the dataset, trains a logistic regression model to predict bin priority, and displays the results on an interactive map. It also provides a city selector, a table of bins needing immediate collection and a summary of bins by priority.
waste_bins.csv	(Optional) Legacy single‑city dataset. If present, the dashboard will fall back to this file when the multi‑city dataset is unavailable.
waste_management_collection_dashboard.md	This document, explaining the project and how to run it.
Features

Multi‑city support – The dataset includes bins from Karachi, Lahore and Sargodha. A drop‑down in the sidebar lets you view the map and tables for a specific city.

Interactive map – Bin locations are plotted on a map using Folium. Markers are coloured red (High priority), orange (Medium priority) or green (Low priority) based on the model’s prediction. Clicking on a marker displays details such as bin ID, area and predicted days until the bin is full.

Machine‑learning model – A logistic regression model is trained to classify bins into priority categories using features derived from the dataset (fill ratio, average daily increase, area and city). The dashboard reports the model’s accuracy.

Top bins list – The top ten bins with the lowest predicted days to full are listed so that collection teams can prioritise them.

Priority summary – A simple table counts how many bins fall into each priority category for the selected city.

Installation

You will need Python 3.7 or newer. Install the required libraries with pip:

python -m pip install streamlit pandas numpy scikit-learn folium streamlit-folium


If the streamlit command is not recognised, use python -m streamlit instead.

Running the Dashboard

Download or clone this project and ensure waste_dashboard.py and waste_bins_multi.csv are in the same directory.

Open a terminal or command prompt and navigate to that directory.

Launch the dashboard using Streamlit:

python -m streamlit run waste_dashboard.py


A local URL (typically http://localhost:8501) will appear. Open it in your web browser. Select a city from the sidebar to view its bins, map and summaries.

Customising the Dataset

The provided waste_bins_multi.csv is synthetic. To adapt the dashboard to your own municipality:

Create a CSV file with the following columns:

bin_id – unique identifier for each bin.

city – name of the city.

area – neighbourhood or district within the city.

latitude, longitude – geographic coordinates.

capacity_kg – bin capacity in kilograms.

current_fill_kg – current amount of waste (kg).

avg_daily_increase_kg – average daily increase in waste (kg).

days_to_full – estimated days until the bin is full (optional; the model will learn this if omitted).

priority – (optional) label indicating urgency (High/Medium/Low). If provided, the model will be trained to predict this column.

Replace waste_bins_multi.csv with your own CSV file. Ensure the file name matches what is loaded in waste_dashboard.py or adjust the code accordingly.

Restart the Streamlit app to load the new data. The logistic regression model will retrain automatically on the new dataset.

License and Acknowledgements

This project is provided for educational purposes and may be adapted for real‑world use. The dataset is synthetic and does not reflect actual waste management data. You may modify and redistribute the code under your preferred licence.
