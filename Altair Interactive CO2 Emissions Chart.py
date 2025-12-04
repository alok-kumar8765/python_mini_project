import altair as alt
import pandas as pd

# --- Project 20: Altair Interactive CO2 Emissions Chart ---

# NOTE: This script is typically run in a Jupyter Notebook or environment
# that supports Altair/Vega-Lite rendering. If run directly via the command
# line, it may output a JSON specification or require a renderer setup.

# Sample data for CO2 Emissions by Country
data = pd.DataFrame({
    "Country":["USA","China","India","Germany","Brazil"],
    "CO2":[5000, 10000, 2500, 800, 400]
})

# 1. Create a selection widget (dropdown) bound to the 'Country' field
dropdown = alt.binding_select(options=data["Country"].tolist(), name='Country:')
selector = alt.selection_single(fields=['Country'], bind=dropdown, empty='none')

# 2. Create the base bar chart
chart = alt.Chart(data).mark_bar().encode(
    # X-axis for Country names
    x=alt.X('Country:N', sort=data["Country"].tolist()),
    # Y-axis for CO2 values
    y='CO2:Q',
    # Color bars by Country (useful even when unfiltered)
    color='Country:N',
    # Add tooltip for interactivity
    tooltip=['Country', 'CO2']
).properties(
    title='CO2 Emissions By Country (Interactive Filter)'
)

# 3. Add the selection and filter transformation
# The chart is filtered based on the selection from the dropdown
final_chart = chart.add_selection(selector).transform_filter(selector)

# Display the chart (this command works in environments like Jupyter)
final_chart.show()
