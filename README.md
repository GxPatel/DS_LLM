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
![ss1](https://github.com/user-attachments/assets/47ded7bc-5aec-4d4e-b0c6-50da38a30a89)
![ss2](https://github.com/user-attachments/assets/975c2eb7-8dfb-4b3d-8011-a399b17cb15e)
![ss3](https://github.com/user-attachments/assets/a7849a95-c9a1-4539-94a5-f15fa526aac4)
![ss4](https://github.com/user-attachments/assets/5cfd2797-a499-44a6-99b4-597ae50c3017)
![ss5](https://github.com/user-attachments/assets/b62e081a-3c2b-4570-9a54-89a784137aba)


### Future Enhancements
- Add more data visualization options.
- Support for additional preprocessing techniques like PCA or feature scaling.
- Provide downloadable processed data after preprocessing.

### Contributing
Feel free to submit pull requests or open issues for any improvements or bugs you encounter.

### License
This project is licensed under the MIT License.
