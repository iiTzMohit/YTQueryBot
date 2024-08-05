# YouTube Assistant

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

## Code Overview
- **main.py**: Contains the Streamlit application code for the user interface and handling form submissions.
- **langchain_helper.py**: Includes functions for processing video transcripts, querying with OpenAI, and integrating FAISS for document retrieval.
  
## Contributing
- If you want to contribute to this project, please follow these steps:
- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Commit your changes (git commit -am 'Add new feature').
- Push to the branch (git push origin feature-branch).
- Create a new Pull Request.

## Contact
For any questions or issues, please reach out to mohitagrawal1618@gmail.com.
