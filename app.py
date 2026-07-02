import streamlit as st
import pandas as pd
import pickle

st.title("Laptop Price Prediction App")

pipe = pickle.load(open("pipe.pkl", "rb"))
df = pd.read_csv("Cleaned_data.csv")

brands = sorted(df["Brand"].unique())

brand = st.sidebar.selectbox("Select Brand", brands)

processor_speed = st.sidebar.number_input(
    "Processor Speed (GHz)",
    min_value=1.0,
    max_value=5.0,
    value=3.0,
    step=0.1
)

ram = st.sidebar.selectbox(
    "Select RAM Size (GB)",
    sorted(df["RAM_Size"].unique())
)

storage = st.sidebar.selectbox(
    "Select Storage Capacity (GB)",
    sorted(df["Storage_Capacity"].unique())
)

screen = st.sidebar.number_input(
    "Screen Size (inches)",
    min_value=10.0,
    max_value=18.0,
    value=15.6,
    step=0.1
)

weight = st.sidebar.number_input(
    "Weight (kg)",
    min_value=1.0,
    max_value=5.0,
    value=2.0,
    step=0.1
)

if st.sidebar.button("Predict Price"):

    st.write("### You have selected:")
    st.write(f"**Brand:** {brand}")
    st.write(f"**Processor Speed:** {processor_speed} GHz")
    st.write(f"**RAM:** {ram} GB")
    st.write(f"**Storage:** {storage} GB")
    st.write(f"**Screen Size:** {screen} inches")
    st.write(f"**Weight:** {weight} kg")

    myinput = [[
        brand,
        processor_speed,
        ram,
        storage,
        screen,
        weight
    ]]

    columns = [
        "Brand",
        "Processor_Speed",
        "RAM_Size",
        "Storage_Capacity",
        "Screen_Size",
        "Weight"
    ]

    myinput = pd.DataFrame(data=myinput, columns=columns)

    result = pipe.predict(myinput)

    if result[0] < 0:
        st.error("Sorry, the predicted price is negative. Please check your input values.")
    else:
        st.success(f"Predicted Laptop Price: ₹{round(result[0], 2)}")
