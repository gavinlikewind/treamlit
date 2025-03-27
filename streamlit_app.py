import streamlit as st
import importlib.util
import sys

# Load the recommender function from the uploaded file
file_path = "content_based_descriptor_recommender.py"
spec = importlib.util.spec_from_file_location("recommender_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Streamlit UI
def main():
    st.title("Content-Based Recommender System")
    st.write("Enter an item or description to get recommendations.")
    
    user_input = st.text_input("Enter item description:", "")
    
    if st.button("Get Recommendations"):
        if user_input:
            recommendations = module.content_recommender(user_input)
            st.write("### Recommended Items:")
            for rec in recommendations:
                st.write(f"- {rec}")
        else:
            st.warning("Please enter a valid input.")

if __name__ == "__main__":
    main()
