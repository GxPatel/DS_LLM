import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Function to preprocess data based on user choices
def preprocess_data(df, fill_na, remove_na, remove_outliers, delete_invariant, drop_useless, check_datetime, one_hot_encode):
    if fill_na:
        df.fillna('NaN', inplace=True)

    if remove_na:
        df.dropna(how='any', inplace=True)

    if remove_outliers:
        for col in df.select_dtypes(include=np.number).columns:
            df = df[(np.abs(df[col] - df[col].mean()) <= (3 * df[col].std()))]

    if delete_invariant:
        df = df.loc[:, df.nunique() > 1]

    if drop_useless:
        useless_columns = st.text_input("Enter column names to drop (comma-separated):").split(',')
        df.drop(columns=[col.strip() for col in useless_columns if col.strip() in df.columns], inplace=True)

    if check_datetime:
        for col in df.columns:
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

    if one_hot_encode:
        df = pd.get_dummies(df)

    return df

# Function to visualize data
def visualize_data(df, chart_type, x_axis, y_axis):
    if chart_type == 'Line':
        fig = px.line(df, x=x_axis, y=y_axis)
    elif chart_type == 'Bar':
        fig = px.bar(df, x=x_axis, y=y_axis)
    elif chart_type == 'Scatter':
        fig = px.scatter(df, x=x_axis, y=y_axis)
    elif chart_type == 'Histogram':
        fig = px.histogram(df, x=x_axis)

    st.plotly_chart(fig)

# Streamlit UI
st.title("Data Preprocessing and Visualization Tool")

uploaded_file = st.file_uploader("Upload your dataset (CSV, XLSX, JSON)", type=['csv', 'xlsx', 'json'])

if 'prev_file_name' not in st.session_state:
    st.session_state.prev_file_name = None

if uploaded_file:
    if st.session_state.prev_file_name and uploaded_file.name != st.session_state.prev_file_name:
        st.warning("Please refresh the page before uploading a new dataset!")
        st.stop()
    else:
        # Update the file name in session state to track the current dataset
        st.session_state.prev_file_name = uploaded_file.name

        # Read the uploaded file
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file, encoding="ISO-8859-1")
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.json'):
            df = pd.read_json(uploaded_file)

    st.write("Original Data")
    st.write(df)

    st.sidebar.title("Preprocessing Options")

    fill_na = st.sidebar.checkbox("Fill empty cells with 'NaN'")
    remove_na = st.sidebar.checkbox("Remove rows/columns with missing data")
    remove_outliers = st.sidebar.checkbox("Remove outliers")
    delete_invariant = st.sidebar.checkbox("Delete invariant columns")
    drop_useless = st.sidebar.checkbox("Drop useless columns")
    check_datetime = st.sidebar.checkbox("Check if DateTime")
    one_hot_encode = st.sidebar.checkbox("One-hot encode")

    if st.sidebar.button("Apply Preprocessing"):
        df = preprocess_data(df, fill_na, remove_na, remove_outliers, delete_invariant, drop_useless, check_datetime, one_hot_encode)
        st.write("Preprocessed Data")
        st.write(df)

    st.write("Data Visualization")

    # Store state for chart type, x_axis, and y_axis
    if 'chart_type' not in st.session_state:
        st.session_state.chart_type = 'Line'
    if 'x_axis' not in st.session_state:
        st.session_state.x_axis = df.columns[0]
    if 'y_axis' not in st.session_state:
        st.session_state.y_axis = df.columns[1] if len(df.columns) > 1 else df.columns[0]

    # Use session state to maintain selections
    st.session_state.chart_type = st.selectbox("Select Chart Type", ['Line', 'Bar', 'Scatter', 'Histogram'], index=['Line', 'Bar', 'Scatter', 'Histogram'].index(st.session_state.chart_type))
    st.session_state.x_axis = st.selectbox("X-Axis", df.columns, index=list(df.columns).index(st.session_state.x_axis))
    st.session_state.y_axis = st.selectbox("Y-Axis", df.columns, index=list(df.columns).index(st.session_state.y_axis))

    # Button to update the chart based on selection
    if st.button("Update Chart"):
        visualize_data(df, st.session_state.chart_type, st.session_state.x_axis, st.session_state.y_axis)

# Footer
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: rgba(255,2555,255,35);
        text-align: center;
        padding: 10px;
        font-size: 12px;
        color: black;
    }
    </style>
    <div class="footer">
        <p> © 2024 All rights reserved. <a style='display: block; text-align: center;' href="https://github.com/GxPatel" target="_blank"> GxPatel </a></p>
    </div>
    """, unsafe_allow_html=True)
