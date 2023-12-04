import pandas as pd
import streamlit as st
import pickle

# Load the model
model = pickle.load(open('regressor.pkl', 'rb'))

# Define a mapping for Light_source
light_source_mapping = {'LED': 0, 'FL': 1, 'Halogen': 2}

# Streamlit settings
image_path = r'D:\PROJECT & INTERNSHIP\INDOOR\SBG\solar app\OIG.jpg'

# Display the image
st.image(image_path, use_column_width=True)
# Define the function to predict with the model
def predict_model(model, df):
    predictions = model.predict(df)
    return predictions[0]

# Create a Streamlit form
with st.form('PCE'):
    # Input fields
    
    Bandgap = st.number_input('Bandgap', min_value=1.2, max_value=2.0, value=1.2)
    HOMO = st.number_input('HOMO', min_value=0.0, max_value=1.50, value=0.5)
    LUMO = st.number_input('LUMO', min_value=-0.9, max_value=1.50, value=0.5)
    Light_source = st.selectbox('Light_source', ['LED', 'FL', 'Halogen'])
    Illuminance = st.number_input('Illuminance', min_value=-100, max_value=2000, value=1000)

    # Predict button
    predict_button = st.form_submit_button('Predict')

# Input dictionary
input_dict = {
    'Bandgap': Bandgap,
    'HOMO': HOMO,
    'LUMO': LUMO,
    'Light_source': light_source_mapping[Light_source],
    'Illuminance': Illuminance
}

# Input DataFrame
input_df = pd.DataFrame([input_dict])

# Predict if the button is pressed
if predict_button:
    output = predict_model(model, input_df)
    st.success(f"The predicted PCE is {output:.2f}")
