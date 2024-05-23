# importing all the required libraries
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter


def main():
    # Data ingestion using PyPDFLoader
    loader = PyPDFLoader("fine_tuning_bert.pdf")
    documents = loader.load()

    print("Data Ingestion successfully completed")

    # Creating Chunks of the Loaded data
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=250)
    final_documents = text_splitter.split_documents(documents)

    print("Chunking process Completed")

    # Creating Embeddings
    embeddings = OllamaEmbeddings(model="llama2")

    print("Embedding process Completed Successfully")

    # creating Vector Database
    database = Chroma.from_documents(final_documents, embeddings)

    print("Vector Database setup successfully")

    # Query for the Vector Database
    query = str(input("Kindly Enter the query you want to retrieve the answer for :"))

    # Retrieving the result from the Vector DB

    result = database.similary_search(query)

    print(result[0].page_content)


if __name__ == "__main__":
    main()
