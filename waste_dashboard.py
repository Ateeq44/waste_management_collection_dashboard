"""
Waste Management & Collection Dashboard
======================================

This Streamlit application demonstrates how machine learning and
geospatial visualisation can assist local governments in optimising
municipal waste collection.  The dashboard uses a synthetic dataset
(`waste_bins.csv`) of waste bins with attributes such as capacity,
current fill level, average daily waste increase and geographic
coordinates.  A logistic regression model is trained to classify
bins into three priority categories (High, Medium, Low) indicating
how soon they will need to be emptied.  The dashboard features:

* **Interactive map** – Bin locations are displayed on a map with
  colour‑coded markers (red, orange and green) based on their
  predicted priority.
* **Model evaluation** – Displays the accuracy of the logistic
  regression model used to predict bin priority.
* **Top bins list** – Shows the bins most urgently requiring
  collection (shortest predicted days to full).
* **Summary table** – Counts bins in each priority category.

To run the dashboard, install the required packages and execute:

```bash
streamlit run waste_dashboard.py
```

Dependencies:

* streamlit
* pandas
* numpy
* scikit‑learn
* folium
* streamlit‑folium

The dataset and the script should be placed in the same working
directory.
"""

import pandas as pd
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import folium
from streamlit_folium import st_folium


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def prepare_features(data: pd.DataFrame) -> tuple:
    """Prepare feature matrix and labels for logistic regression.

    Computes a fill ratio and one‑hot encodes both the area and city
    categorical variables.  Returns X, y and a label encoder for the
    priority column.
    """
    df = data.copy()
    df['fill_ratio'] = df['current_fill_kg'] / df['capacity_kg']
    # One‑hot encode area and city
    area_dummies = pd.get_dummies(df['area'], prefix='area')
    city_dummies = pd.get_dummies(df['city'], prefix='city')
    X = pd.concat([df[['fill_ratio', 'avg_daily_increase_kg']], area_dummies, city_dummies], axis=1)
    le = LabelEncoder()
    y = le.fit_transform(df['priority'])
    return X, y, le


def train_logistic_regression(X: pd.DataFrame, y: np.ndarray):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Create a logistic regression model without specifying multi_class for compatibility with older scikit-learn versions
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    return model, accuracy


def predict_priorities(model: LogisticRegression, X: pd.DataFrame, le: LabelEncoder) -> pd.Series:
    preds = model.predict(X)
    return le.inverse_transform(preds)


def main() -> None:
    st.set_page_config(page_title="Waste Management Dashboard", layout="wide")
    st.title("Waste Management & Collection Dashboard")
    # Load dataset (support multiple city dataset as well)
    try:
        data = load_data('waste_bins_multi.csv')
    except FileNotFoundError:
        try:
            data = load_data('waste_bins.csv')
        except FileNotFoundError:
            st.error("Neither 'waste_bins_multi.csv' nor 'waste_bins.csv' found in the working directory.")
            return
    # Train model on the entire dataset
    X, y, le = prepare_features(data)
    model, acc = train_logistic_regression(X, y)
    data['predicted_priority'] = predict_priorities(model, X, le)
    st.write(f"Model accuracy (predicting priority categories): {acc:.2f}")
    # Sidebar city selector if multiple cities exist
    cities = sorted(data['city'].unique()) if 'city' in data.columns else ['All']
    if len(cities) > 1:
        selected_city = st.sidebar.selectbox("Select City", cities)
        filtered_data = data[data['city'] == selected_city].copy()
    else:
        selected_city = cities[0]
        filtered_data = data.copy()
    # Map display
    st.subheader(f"Bin Locations and Priority – {selected_city}")
    # Determine map centre using filtered data
    center_lat = filtered_data['latitude'].mean()
    center_lon = filtered_data['longitude'].mean()
    m = folium.Map(location=[center_lat, center_lon], zoom_start=13)
    colour_map = {'High': 'red', 'Medium': 'orange', 'Low': 'green'}
    for _, row in filtered_data.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=5,
            popup=(f"Bin ID: {row['bin_id']}\n"
                   f"Area: {row['area']}\n"
                   f"Days to Full: {row['days_to_full']}\n"
                   f"Predicted Priority: {row['predicted_priority']}"),
            color=colour_map[row['predicted_priority']],
            fill=True,
            fill_color=colour_map[row['predicted_priority']],
            fill_opacity=0.7
        ).add_to(m)
    st_folium(m, width=800, height=450)
    # Top bins requiring collection (for selected city)
    st.subheader("Top Bins Needing Collection")
    top_bins = filtered_data.sort_values('days_to_full').head(10)
    st.table(top_bins[['bin_id', 'area', 'days_to_full', 'predicted_priority']].rename(
        columns={'bin_id': 'Bin ID', 'area': 'Area', 'days_to_full': 'Days to Full', 'predicted_priority': 'Priority'}))
    # Summary counts by priority (for selected city)
    st.subheader("Priority Summary")
    counts = filtered_data['predicted_priority'].value_counts().reset_index()
    counts.columns = ['Priority', 'Count']
    st.table(counts)


if __name__ == '__main__':
    main()