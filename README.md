
  <h1>Waste Management &amp; Collection Dashboard</h1>
  <p>
    This project demonstrates how local governments can use machine learning and geospatial visualisation to optimise municipal waste collection.
    The dashboard highlights bins that will reach capacity soon, allowing city administrators to prioritise collection routes and allocate resources
    efficiently. The app is built with Streamlit and uses a synthetic dataset of bins across multiple cities.
  </p>

  <h2>Project Structure</h2>
  <table>
    <thead>
      <tr><th>File</th><th>Description</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><code>waste_bins_multi.csv</code></td>
        <td>Synthetic dataset containing bins for three cities (Karachi, Lahore and Sargodha). Each record includes the bin’s location, capacity,
          current fill level, average daily waste increase and a calculated priority class (High/Medium/Low).</td>
      </tr>
      <tr>
        <td><code>waste_dashboard.py</code></td>
        <td>Streamlit app that loads the dataset, trains a logistic regression model to predict bin priority, and displays the results on an
          interactive map. It also provides a city selector, a table of bins needing immediate collection and a summary of bins by priority.</td>
      </tr>
      <tr>
        <td><code>waste_bins.csv</code></td>
        <td>(Optional) Legacy single-city dataset. If present, the dashboard will fall back to this file when the multi-city dataset is unavailable.</td>
      </tr>
      <tr>
        <td><code>waste_management_collection_dashboard.md</code></td>
        <td>This document, explaining the project and how to run it.</td>
      </tr>
    </tbody>
  </table>

  <h2>Features</h2>
  <ul>
    <li><strong>Multi-city support</strong> – The dataset includes bins from Karachi, Lahore and Sargodha. A drop-down in the sidebar lets you view
      the map and tables for a specific city.</li>
    <li><strong>Interactive map</strong> – Bin locations are plotted on a map using Folium. Markers are coloured red (High priority), orange
      (Medium priority) or green (Low priority) based on the model’s prediction. Clicking on a marker displays details such as bin ID, area and
      predicted days until the bin is full.</li>
    <li><strong>Machine-learning model</strong> – A logistic regression model is trained to classify bins into priority categories using
      features derived from the dataset (fill ratio, average daily increase, area and city). The dashboard reports the model’s accuracy.</li>
    <li><strong>Top bins list</strong> – The top ten bins with the lowest predicted days to full are listed so that collection teams can prioritise them.</li>
    <li><strong>Priority summary</strong> – A simple table counts how many bins fall into each priority category for the selected city.</li>
  </ul>

  <h2>Installation</h2>
  <p>You will need Python 3.7 or newer. Install the required libraries with <code>pip</code>:</p>
  <pre><code>python -m pip install streamlit pandas numpy scikit-learn folium streamlit-folium</code></pre>
  <p>If the <code>streamlit</code> command is not recognised, use <code>python -m streamlit</code> instead.</p>

  <h2>Running the Dashboard</h2>
  <ol>
    <li>Download or clone this project and ensure <code>waste_dashboard.py</code> and <code>waste_bins_multi.csv</code> are in the same directory.</li>
    <li>Open a terminal or command prompt and navigate to that directory.</li>
    <li>Launch the dashboard using Streamlit:
      <pre><code>python -m streamlit run waste_dashboard.py</code></pre>
    </li>
    <li>A local URL (typically <code>http://localhost:8501</code>) will appear. Open it in your web browser. Select a city from the sidebar to view its bins, map and summaries.</li>
  </ol>

  <h2>Customising the Dataset</h2>
  <p>The provided <code>waste_bins_multi.csv</code> is synthetic. To adapt the dashboard to your own municipality:</p>
  <ol>
    <li>Create a CSV file with the following columns:
      <ul>
        <li><code>bin_id</code> – unique identifier for each bin.</li>
        <li><code>city</code> – name of the city.</li>
        <li><code>area</code> – neighbourhood or district within the city.</li>
        <li><code>latitude</code>, <code>longitude</code> – geographic coordinates.</li>
        <li><code>capacity_kg</code> – bin capacity in kilograms.</li>
        <li><code>current_fill_kg</code> – current amount of waste (kg).</li>
        <li><code>avg_daily_increase_kg</code> – average daily increase in waste (kg).</li>
        <li><code>days_to_full</code> – estimated days until the bin is full (optional; the model will learn this if omitted).</li>
        <li><code>priority</code> – (optional) label indicating urgency (High/Medium/Low). If provided, the model will be trained to predict this column.</li>
      </ul>
    </li>
    <li>Replace <code>waste_bins_multi.csv</code> with your own CSV file. Ensure the file name matches what is loaded in <code>waste_dashboard.py</code> or adjust the code accordingly.</li>
    <li>Restart the Streamlit app to load the new data. The logistic regression model will retrain automatically on the new dataset.</li>
  </ol>

  <h2>License and Acknowledgements</h2>
  <p>This project is provided for educational purposes and may be adapted for real‑world use. The dataset is synthetic and does not reflect actual
    waste management data. You may modify and redistribute the code under your preferred licence.</p>
