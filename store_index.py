from src.helper import load_pdf,text_split,download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
import pinecone
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['PINECONE_API_KEY'] = os.getenv('PINECONE_API_KEY')

extracted_data=load_pdf('content/')
text_chunks=text_split(extract_data=extracted_data)
embedding=download_hugging_face_embeddings()


index_name = 'medical-chatbot'

# Convert text chunks to list of page contents
texts = [t.page_content for t in text_chunks]

# Set up Pinecone vector store
vectorstore_from_texts = Pinecone.from_texts(
    texts,
    index_name=index_name,
    embedding=embedding
)

