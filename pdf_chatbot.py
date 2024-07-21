from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os
import openai

# Set the API key for OpenAI
os.environ["OPENAI_API_KEY"] = "Input you API key"

class PDFChatbot:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.llm = OpenAI(model_name="gpt-4")  # Use the latest LLM model version
        self.embeddings = OpenAIEmbeddings()
        self.text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=800,
            chunk_overlap=200,
            length_function=len
        )
        self.vectorstore = None  # Will be initialized with actual content

        self.prompt_template = PromptTemplate(
            template="Answer the following question based on the provided text: {text}\n\nQuestion: {question}\n\nAnswer:",
            input_variables=["text", "question"]
        )
        self.qa_chain = None  

    def extract_text_from_pdf(self, pdf_file_path):
        pdfreader = PdfReader(pdf_file_path)
        raw_text = ''
        for page in pdfreader.pages:
            content = page.extract_text()
            if content:
                raw_text += content
        
        chunks = self.text_splitter.split_text(raw_text)
        self.vectorstore = FAISS.from_texts(chunks, self.embeddings)  
        
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever()
        )

    def get_response(self, user_input):
        if self.qa_chain is None:
            return "Please upload a PDF file first."
        response = self.qa_chain.run(query=user_input)
        return response
