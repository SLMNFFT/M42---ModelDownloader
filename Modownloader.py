import streamlit as st
from huggingface_hub import snapshot_download, login
import os

# Define the local download directory
DOWNLOAD_DIR = "/path/2ur/Image models/"

st.title("🕵️‍♀️ M42 -  AI 🤗 Model Downloader 📥 ")

# Input for Hugging Face token (if needed for private models)
hf_token = st.text_input("🔑 Hugging Face Token (Required for private models)", type="password")

# Text input for the model repository (e.g., "username/model_name")
model_repo = st.text_input("Enter the Hugging Face model repository (e.g., username/model_name):")

# Button to start download
if st.button("Download Model"):
    if not model_repo:
        st.error("❌ Please specify a model repository!")
    else:
        # Create a safe folder name by replacing '/' with '_'
        folder_name = model_repo.replace("/", "_")
        save_path = os.path.join(DOWNLOAD_DIR, folder_name)
        os.makedirs(save_path, exist_ok=True)

        st.write(f"📡 Downloading model from repository: `{model_repo}` ...")
        
        try:
            # Authenticate if a token is provided
            if hf_token:
                login(token=hf_token)
            
            # Download the model repository to the local directory
            snapshot_download(repo_id=model_repo, local_dir=save_path, local_dir_use_symlinks=False)
            st.success(f"✅ Model downloaded successfully! Saved to: {save_path}")
        except Exception as e:
            st.error(f"❌ Error downloading the model: {e}")
