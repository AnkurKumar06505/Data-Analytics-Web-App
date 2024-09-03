Data Analysis Portal
The Data Analysis Portal is a robust and user-friendly Streamlit-based web application designed to simplify the process of data analysis. It provides an intuitive interface where users can upload datasets in CSV or Excel format, explore essential statistics, and generate insightful visualizations with ease. This tool is ideal for anyone looking to perform quick and comprehensive data analysis without writing a single line of code.

Features
1. File Upload
The application supports the upload of datasets in two common formats:

CSV (.csv)
Excel (.xlsx)
Once a file is uploaded, the app automatically processes and displays the data in a tabular format. This immediate feedback allows users to quickly verify their data and proceed with further analysis.

2. Data Overview
After the dataset is uploaded, the portal offers a detailed overview of the data, making it easy for users to understand the structure and contents of the dataset. The Data Overview includes:

Number of Rows and Columns: The total count of rows and columns is displayed to give users a quick understanding of the dataset size.
Statistical Summary: A comprehensive summary of numerical columns, including key statistics such as mean, median, standard deviation, min, max, and percentiles.
Top and Bottom Rows: Users can view the first few and last few rows of the dataset, making it easy to inspect the beginning and end of the data.
Data Types: A display of the data types for each column, helping users understand how the data is structured and identify any potential issues (e.g., numeric columns stored as strings).
List of Columns: A complete list of all column names, giving users a clear view of the dataset's structure.
3. Column Value Counts
The portal provides a powerful feature for analyzing the distribution of values within a specific column:

Select a Column: Users can choose any column in the dataset to analyze the frequency of its unique values.
View Results: The frequency count is displayed in a table, allowing users to quickly identify the most common values.
Visualizations: The frequency data can be visualized through various charts:
Bar Chart: Displays the count of each unique value using bars, ideal for comparing categories.
Line Chart: Plots the frequency of values on a line, providing a visual trend analysis.
Pie Chart: Represents the distribution of values as segments of a pie, useful for showing proportions.
4. Groupby Operations
This feature allows users to perform aggregation operations on the dataset based on one or more columns:

Groupby Columns: Users can select one or more columns to group the data.
Aggregation Operations: Perform operations such as sum, mean, min, max, median, and count on a chosen column.
Result Display: The grouped data is displayed in a table, showing the aggregated results for each group.
Visualizations: The summarized data can be visualized through several chart types:
Line Chart: Useful for showing trends over grouped data.
Bar Chart: Ideal for comparing the aggregated values across different groups.
Scatter Plot: Helps in identifying relationships and correlations between two numerical columns in the grouped data.
Pie Chart: Displays the proportion of each group in relation to the whole dataset.
Sunburst Chart: Visualizes hierarchical data through concentric rings, useful for showing multi-level groupings.
5. Interactive Visualizations
All the visualizations in the Data Analysis Portal are powered by Plotly, a library known for its interactive and dynamic charts:

Interactivity: Users can hover over charts to see detailed data points, zoom in and out for better clarity, and even pan across the visualizations to explore specific areas of interest.
Customization: The visualizations are generated based on user selections, allowing for a high degree of customization without requiring any coding skills.
Responsive Design: The charts adjust automatically to fit the browser window, ensuring a seamless experience across different devices and screen sizes.

Usage
Upload a File: Start by uploading a CSV or Excel file.
Explore the Data: Use the tabs to view data summaries, data types, and specific rows.
Analyze Column Values: Select a column to see the distribution of its values, along with corresponding visualizations.
Group and Summarize Data: Use the Groupby feature to aggregate data and create custom summaries, which can then be visualized using various chart types.
Interactive Charts: Explore the generated visualizations to gain insights into your data.
