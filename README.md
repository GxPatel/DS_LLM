# Data Preprocessing and Visualization Tool
This project is a user-friendly Data Preprocessing and Visualization Tool built using Streamlit, Pandas, and Plotly. It allows users to preprocess their datasets and generate various visualizations, all from a single interface. The tool supports multiple preprocessing options and lets users select the specific tasks they want to apply to their data.

### Features
#### 1. Data Preprocessing
The tool offers the following data preprocessing functionalities:

- Fill Empty Cells with 'NaN': Fill missing values with 'NaN' for easy identification of incomplete data.
- Remove Rows/Columns with Missing Data: Drop rows or columns containing missing values.
- Remove Outliers: Automatically remove outliers from numeric data based on z-scores.
- Delete Invariant Columns: Drop columns with only a single unique value.
- Drop Useless Columns: Allows users to specify columns they want to drop.
- Check if DateTime: Detect and convert columns to datetime format (if applicable).
- One-Hot Encoding: Convert categorical variables into one-hot encoded columns.

#### 2. Data Visualization
After preprocessing the data, users can generate different types of visualizations:

- Line Chart
- Bar Chart
- Scatter Plot
- Histogram

Users can choose the chart type, X-axis, and Y-axis dynamically from the available columns in the dataset.

### How It Works
- Upload Your Dataset: The tool accepts .csv, .xlsx, or .json files.
- Preprocess the Data: You can select the preprocessing options you want to apply through the sidebar.
- Visualize the Data: Select the desired chart type and set the X and Y axes for the chart. The visualization will automatically update based on your selections.

### Tech Stack
- Python: Main programming language.
- Streamlit: Used for building the interactive web app interface.
- Pandas: For data manipulation and preprocessing.
- Plotly: For interactive and customizable visualizations.

### Usage
- Upload your dataset.
- Select preprocessing options from the sidebar and click the "Apply Preprocessing" button.
- Choose your visualization type and set the X and Y axes to generate the desired chart.

### Example
- Upload a sample CSV file containing numeric and categorical data.
- Apply preprocessing steps such as normalizing the data, removing outliers, and one-hot encoding categorical variables.
- Visualize the relationship between two columns with a scatter plot, bar chart, or histogram.

### Screenshots
![Screenshot 2024-08-22 190136](https://github.com/user-attachments/assets/c6ec55ba-078d-4b2c-b556-91cd0afd5423)
![Screenshot 2024-08-22 190210](https://github.com/user-attachments/assets/28ded331-4772-4816-b720-5a1235e833bd)
![Screenshot 2024-08-22 190248](https://github.com/user-attachments/assets/b47e841d-a442-4ef7-ae09-f681198e2cb3)
![image](https://github.com/user-attachments/assets/8fcd0a2f-3501-43be-bddd-2ff92253d166)


### Future Enhancements
- Add more data visualization options.
- Support for additional preprocessing techniques like PCA or feature scaling.
- Provide downloadable processed data after preprocessing.

### Contributing
Feel free to submit pull requests or open issues for any improvements or bugs you encounter.

### License
This project is licensed under the MIT License.
