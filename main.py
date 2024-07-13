import logging
import sys

logging.basicConfig(stream=sys.stdout,level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama_index.core import VectorStoreIndex,SimpleDirectoryReader 
from llama_index.llms.huggingface  import HuggingFaceLLM
from llama_index.core import Settings

documents=SimpleDirectoryReader("").load_data()

from llama_index.embeddings.fastembed import FastEmbedEmbeding 

embed_model=FastEmbedEmbeding(model_name="___")

Settings.embed_model=embed_model
Settings.chunk_size=512
