from pathlib import Path
from langchain.text_splitter import CharacterTextSplitter
import faiss
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import pickle
from langchain import OpenAI, LLMChain
from langchain.prompts import Prompt
from flask import Flask, request, jsonify
import os

index = faiss.read_index("training.index")

with open("faiss.pkl", "rb") as f:
  store = pickle.load(f)

store.index = index

with open("training/master.txt", "r") as f:
  promptTemplate = f.read()

prompt = Prompt(template=promptTemplate, input_variables=["history", "context", "question"])

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
  return "API Online"

@app.route("/", methods=["POST"])
def ask():
  reqData = request.get_json()
  if reqData['secret'] == os.environ["API_SECRET"]:
    try:
      llmChain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0.25, model_name="text-davinci-003", openai_api_key=os.environ["OPENAI_API_KEY"]))

      def onMessage(question, history):
        docs = store.similarity_search(question)
        contexts = []
        for i, doc in enumerate(docs):
          contexts.append(f"Context {i}:\n{doc.page_content}")
          answer = llmChain.predict(question=question, context="\n\n".join(contexts), history=history)
        return answer

      return jsonify({
        "answer": onMessage(reqData['question'], reqData['history']),
        "success": True
      })

    except:

      return jsonify({
        "answer": None, 
        "success": False,
        "message": "Error"
      }), 400

  else:

    return jsonify({
      "answer": None, 
      "success": False,
      "message": "Unauthorised"
    })

app.run(host="0.0.0.0", port=3000)