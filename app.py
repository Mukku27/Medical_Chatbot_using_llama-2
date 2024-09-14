from flask import Flask,render_template,jsonify,request
from src.helper import download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
import pinecone
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.llms import CTransformers
from dotenv import load_dotenv
from src.prompt import *
import os

app=Flask(__name__ )

load_dotenv()

os.environ['PINECONE_API_KEY'] = os.getenv('PINECONE_API_KEY')


embedding=download_hugging_face_embeddings()

index_name = 'medical-chatbot'

# Initialize document search using Pinecone
docsearch = Pinecone.from_existing_index(index_name, embedding)


PROMPT = PromptTemplate(template=prompt_template, input_variables=['context', 'question'])
chain_type_kwargs = {'prompt': PROMPT}

llm = CTransformers(model='TheBloke/Llama-2-7B-Chat-GGML',
                    model_type='llama',
                    config={'max_new_tokens': 512, 'temperature': 0.8})


 
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs,
)

@app.route("/")
def index():
    return render_template('chat.html')
 

if  __name__=='__main__':
   app.run(debug=True)