from langchain_community.llms import OpenAI
from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

def generate_vectordb_from_yt_url(video_url: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100)
    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)
    return db

def get_response_from_query(db, query, k):
    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])

    llm = OpenAI(model = "gpt-3.5-turbo-instruct")

    user_prompt = PromptTemplate(
        input_variables= ["question", "docs"],
        template= """
        You are a helpful YouTube assistant that can answer questions about videos based on the video's transcript.

        Answer the following question: {question}
        By searching the following video transcript: {docs}

        Only use the facyual information from the transcript to answer the question.

        if you feel like you don't have enough information to answer the question, say "I don't know".

        Your answers should be detailed.
        """
    )

    user_chain = LLMChain(llm = llm, prompt = user_prompt)
    response = user_chain.run(question = query, docs = docs_page_content)
    response.replace("\n", "")
    return response, docs