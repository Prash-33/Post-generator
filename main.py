import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
from PIL import Image

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English"]

# Main app layout
def main():
    st.subheader("LinkedIn Post Generator:")

    # Create three columns for the dropdowns
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()

    with col1:
        # Dropdown for Topic (Tags)
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        # Dropdown for Length
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        # Dropdown for Language
        selected_language = st.selectbox("Language", options=language_options)

    # Generate Button
    if st.button("Generate"):
        api_key = "Your api key"
        post_text, image_path = generate_post(selected_length, selected_language, selected_tag, api_key)

        # Display Post Text
        st.write(post_text)

        # Display Image
        img = Image.open(image_path)
        st.image(img, caption="Generated Image", use_container_width=True)


# Run the app
if __name__ == "__main__":
    main()
