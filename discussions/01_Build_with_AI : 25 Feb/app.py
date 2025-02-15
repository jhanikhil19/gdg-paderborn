from google import genai
from google.genai import types
import streamlit as st

# Initialize Gemini client (replace with your actual API key)
# client = genai.Client(api_key="GEMINI_API_KEY")  # Make sure you have the key

sys_instruct = """
                You are a Gym Trainer and PhD in sports and nutrition. 
                Your name is Jumbo. 
                You have good knowledge of nutrients, workouts, diet plans and life style management.
                
                If you have any questions for anything further, feel free to ask me those. 
                You are not supposed to assume anything. If something is missing ASK !!!!

            """

st.title("Jumbo's Fitness App")

# User input
name = st.text_input("Your Name")
age = st.number_input("Your Age", min_value=1, value=25)
weight = st.number_input("Your Weight (kg)", min_value=1, value=70)
steps = st.number_input("Average Daily Steps", min_value=0, value=5000)
origin = st.text_input("Your Origin Country")
workout_frequency = st.selectbox("Workout Frequency", ["Daily", "Several times a week", "Occasionally", "Never"]) #add workout frequency

if st.button("Get Personalized Recommendations"):
    user_info = f"""
            I am {name}, 
            I am {age} years old.
            I workout {workout_frequency} and walk an average of {steps} steps a day. 
            I am around {weight} kgs.
            I am {origin}.

            Suggest me in short: 
                1. Diet plan to come to my good BMI level 
                2. My target weight to be fit. 
                3. Life style changes. 
                4. 2 best easy to cook recipe based on my origin country. 
                5. Which food items should I avoid from my region? 
            """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", #or gemini-pro if you have access
            config=types.GenerateContentConfig(
                system_instruction=sys_instruct),
            contents=user_info
        )
        st.write(response.text)

    except Exception as e:  # Handle potential errors
        st.error(f"An error occurred: {e}")
        st.error("Please ensure your API key is correct and you have an internet connection.")


# Optional: Add more features like workout tracking, recipe database, etc.
# These would require more complex coding and potentially a database.