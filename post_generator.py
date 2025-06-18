from llm_helper import llm
from few_shot import FewShotPosts
import requests
import base64

few_shot = FewShotPosts()

# Stability AI Image Generation
def generate_image(prompt, api_key):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "text_prompts": [{"text": prompt}],
        "cfg_scale": 7,
        "height": 1024,
        "width": 1024,
        "samples": 1
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.ok:
        image_data = response.json()["artifacts"][0]["base64"]
        with open("generated_image.png", "wb") as f:
            f.write(base64.b64decode(image_data))
        return "generated_image.png"
    else:
        raise Exception(f"Error: {response.text}")

# Post length helper
def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"

# Generate the post and image
def generate_post(length, language, tag, api_key):
    prompt = get_prompt(length, language, tag)
    response = llm.invoke(prompt)
    post_text = response.content
    print("Generated Post Text: ", post_text)
    
    # Generate the image based on the post content
    image_path = generate_image(post_text, api_key)
    print(f"Image generated and saved at: {image_path}")
    
    return post_text, image_path

# Construct the prompt
def get_prompt(length, language, tag):
    length_str = get_length_str(length)
    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.
    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    '''
    
    examples = few_shot.get_filtered_posts(length, language, tag)
    
    if len(examples) > 0:
        prompt += "4) Use the writing style as per the following examples."
        
    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i+1}: \n\n {post_text}'
        
        if i == 1:  # Use max two samples
            break

    return prompt

if __name__ == "__main__":
    api_key = "sk-rPj5FRVUHkzXjSMT2kJc25FD6vSzFnyTInNKWIGZtLfa9brA"  # Replace with your API key
    post_text, image_path = generate_post("Medium", "English", "Mental Health", api_key)
