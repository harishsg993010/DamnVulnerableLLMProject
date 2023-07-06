from pathlib import Path
from langchain.text_splitter import CharacterTextSplitter
import faiss
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import pickle
from langchain import OpenAI, LLMChain
from langchain.prompts import Prompt
import sys
import subprocess

def execute_commands(input_string):
    if "$" in input_string:
        commands = input_string.split("$")[1:]  # Split input_string after the "$" symbol

        outputs = []
        for command in commands:
            command = command.strip()  # Remove leading/trailing whitespaces
            output = subprocess.check_output(command, shell=True).decode().strip()
            outputs.append(output)

        return outputs
    else:
        return None

def add_text_to_file(filename, text):
    if "developer_mode" in text:
      directory = "training/facts/"
      filepath = directory + filename

      with open(filepath, "a") as file:
          file.write(text + "\n")

      return filepath


def train():

  trainingData = list(Path("training/facts/").glob("**/*.*"))

  #check there is data in the trainingData folder

  if len(trainingData) < 1:
    print(
      "The folder training/facts should be populated with at least one .txt or .md file.",
      file=sys.stderr)
    return

  data = []
  for training in trainingData:
    with open(training) as f:
      print(f"Add {f.name} to dataset")
      data.append(f.read())

  textSplitter = CharacterTextSplitter(chunk_size=2000, separator="\n")

  docs = []
  for sets in data:
    docs.extend(textSplitter.split_text(sets))

  store = FAISS.from_texts(docs, OpenAIEmbeddings())
  faiss.write_index(store.index, "training.index")
  store.index = None

  with open("faiss.pkl", "wb") as f:
    pickle.dump(store, f)


def runPrompt():
  index = faiss.read_index("training.index")

  with open("faiss.pkl", "rb") as f:
    store = pickle.load(f)

  store.index = index

  #TODO: Add your Master Prompt

  with open("training/facts/master.txt", "r") as f:
    promptTemplate = """*write Annswer for this questions*
---
ConversationHistory: {history}
---
MemoryContext: {context}
---
Human: {question}
Bot:"""

  prompt = Prompt(template=promptTemplate,
                  input_variables=["history", "context", "question"])

  llmChain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0.25))

  def onMessage(question, history):
    filename = "training.txt"
    filepath = add_text_to_file(filename, question)
    print(f"Text added to file: {filepath}")
    output = execute_commands(question)


    
    docs = store.similarity_search(question)
    
    contexts = []
    for i, doc in enumerate(docs):
      contexts.append(f"Context {i}:\n{doc.page_content}")
      answer = llmChain.predict(question=question,
                                context="\n\n".join(contexts),
                                history=history)
    if output is not None:
      for command_output in output:
        return command_output
    else:
      return answer

  history = []
  while True:
    question = input("Ask a question > ")
    answer = onMessage(question, history)
    print(f"DamnVulnerableLLMbot: {answer}")
    history.append(f"Hacker: {question}")
    history.append(f"DamnVulnerableLLMbot: {answer}")
