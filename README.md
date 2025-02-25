# M42---ModelDownloader
This tool is for automatical huggingFace AI - models download 


How This Works

    Hugging Face Token:
    If you need to access a private model, enter your Hugging Face token. The script logs in using this token.

    Model Repository:
    Simply input the full repository ID (e.g., username/model_name). The script uses this to download the model.

    Download Process:
    The model is downloaded to a folder created by replacing / with _ in the repository name, ensuring a valid folder name.

This setup allows you to download any model directly by entering its repository name.


# AI Model Downloader

This is a simple Streamlit application that allows you to download AI models from the Hugging Face Hub by entering the model repository name. It also supports private models by accepting a Hugging Face token for authentication.

## Features

- **Flexible Model Selection:**  
  Enter any Hugging Face model repository (e.g., `username/model_name`) directly into the text field.
  
- **Private Model Support:**  
  Provide your Hugging Face token if the model requires authentication.

- **Local Download:**  
  Downloads the model repository to a designated local directory.

## Prerequisites

- Python 3.7 or higher
- [Streamlit](https://streamlit.io/)  
- [huggingface_hub](https://github.com/huggingface/huggingface_hub)

## Installation

1. **Clone the repository** (if applicable) or download the script file.

2. **Install the required packages**:

   ```bash
   pip install streamlit huggingface_hub

    Update the download directory in the script if needed. The default is set to:

    DOWNLOAD_DIR = "/home/gringo/Image models/"

Usage

    Run the application using Streamlit:

streamlit run your_script_name.py
