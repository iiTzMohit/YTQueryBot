# YTQueryBot

A web application that uses AI to answer questions about YouTube video content. Built with Streamlit for the frontend, and LangChain with OpenAI for processing and querying video transcripts.

## Features

- **Interactive User Interface**: Allows users to input YouTube video URLs and ask questions about the video.
- **AI-Driven Responses**: Uses OpenAI's language model to generate detailed answers based on video transcripts.
- **Efficient Document Retrieval**: Implements FAISS for fast and accurate search within video transcripts.

## Technologies

- **Streamlit**: For building the web interface.
- **LangChain**: For handling video transcripts and AI-based responses.
- **OpenAI**: For generating responses to user queries.
- **FAISS**: For efficient document retrieval and similarity search.
- **Python**: The programming language used.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/iiTzMohit/YTQueryBot.git
   cd YTQueryBot
2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `.venv/Scripts/Activate.ps1`
3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
4. **Set Up Environment Variables**

   ```bash
   OPENAI_API_KEY=your_openai_api_key

## Usage

1. **Run the Application**

   ```bash
   streamlit run main.py
2. **Open the Application**
   - Open your web browser and go to http://localhost:8501.

3. **Interact with the Application**
   - Enter the YouTube video URL in the sidebar.
   - Ask a question about the video content.
   - Submit the form to receive a detailed response.

## Code Overview
- **main.py**: Contains the Streamlit application code for the user interface and handling form submissions.
- **langchain_helper.py**: Includes functions for processing video transcripts, querying with OpenAI, and integrating FAISS for document retrieval.
  
## Credits
This project was inspired by and developed based on the YouTube tutorial by rishabincloud. Special thanks to rishabincloud for providing detailed guidance and resources.
- YouTube Tutorial: LangChain Crash Course for Beginners

## Contact
For any questions or issues, please reach out to mohitagrawal1618@gmail.com.
