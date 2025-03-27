'''from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import time
import speech_recognition as sr
import webbrowser
from nltk.tokenize import word_tokenize
from openai import OpenAI
import pyautogui
import time
import requests
from bs4 import BeautifulSoup




# Enter your Assistant ID here.
ASSISTANT_ID = "asst_1wrWuCGlp0c7mmdWfV4ONKdC"

# Enter your OpenAI API key here.
API_KEY = "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"

# Create an instance of the OpenAI client with your API key.
client = OpenAI(api_key=API_KEY)
chatStr = ""
query = ""

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://nishchal:nishchaltendulkar@cluster0.imkrbqd.mongodb.net/AI_Desktop_Assistant"
mongo = PyMongo(app)

@app.route("/")
def home():
    return render_template("landing.html")


@app.route("/index")
def index():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html", myChats=myChats)

@app.route("/todoList")
def todoList():
    return render_template("ToDoList1.html")

@app.route("/Dalle")
def Dalle():
    return render_template("Dalle.html")

@app.route("/process_voice_input", methods=["POST"])
def qa():
    if request.method == "POST":
        try:
            question = request.json.get("question")
            question = question.lower()
            chat = mongo.db.chats.find_one({"question": question})

            if "open" in question:
                sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ["hotstar", "https://www.hotstar.com/in"]]

                for site in sites:
                    if f"open {site[0]}".lower() in question.lower():
                        webbrowser.open(site[1])
                        return jsonify({"response": f"Opening {site[0]} sir..."})

            if "click my photo" in question:
                pyautogui.press("super")
                pyautogui.typewrite("camera")
                pyautogui.press("enter")
                pyautogui.sleep(2)
                pyautogui.press("enter")

            if chat:
                data = {"question": question, "answer": chat["answer"]}
                return jsonify(data)

            if "open app" in question:   #EASY METHOD
                    question = question.replace("open app","")
                    pyautogui.press("super")
                    pyautogui.typewrite(question)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")

            if "temperature" in question:
                url = f"https://www.google.com/search?q={question}"
                webbrowser.open(url)

            if "weather" in question:
                url = f"https://www.google.com/search?q={question}"
                webbrowser.open(url)


            else:
                # Create a thread with the user's question.
                thread = client.beta.threads.create(
                    messages=[
                        {
                            "role": "user",
                            "content": question,
                        }
                    ]
                )

                # Submit the thread to the assistant.
                run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=ASSISTANT_ID)

                # Wait for the assistant to respond.
                while run.status != "completed":
                    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
                    time.sleep(1)

                # Get the latest message from the thread.
                message_response = client.beta.threads.messages.list(thread_id=thread.id)
                latest_message = message_response.data[0]

                # Extract the assistant's response from the latest message.
                assistant_response = latest_message.content[0].text.value

                # Save the conversation in MongoDB.
                mongo.db.chats.insert_one({"question": question, "answer": assistant_response})

                return jsonify({"answer": assistant_response})
        except Exception as e:
            print(f"Error during API request: {e}")
            return jsonify({"error": "Internal server error"}), 500



    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss?"}
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True, port=5001)

'''


from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import webbrowser
import pyautogui
import os
import google.generativeai as genai



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://nishchal:nishchaltendulkar@cluster0.imkrbqd.mongodb.net/AI_Desktop_Assistant"
mongo = PyMongo(app)

@app.route("/")
def home():
    return render_template("landing.html")


@app.route("/index")
def index():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html", myChats=myChats)

@app.route("/todoList")
def todoList():
    return render_template("ToDoList1.html")

@app.route("/Dalle")
def Dalle():
    return render_template("Dalle.html")

@app.route("/process_voice_input", methods=["POST"])
def qa():
    if request.method == "POST":
        try:
            question = request.json.get("question")
            question = question.lower()
            chat = mongo.db.chats.find_one({"question": question})

            if "open" in question:
                sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                         ["google", "https://www.google.com"], ["hotstar", "https://www.hotstar.com/in"]]

                for site in sites:
                    if f"open {site[0]}".lower() in question.lower():
                        webbrowser.open(site[1])
                        return jsonify({"response": f"Opening {site[0]} sir..."})

            if "click my photo" in question:
                pyautogui.press("super")
                pyautogui.typewrite("camera")
                pyautogui.press("enter")
                pyautogui.sleep(2)
                pyautogui.press("enter")

            if chat:
                data = {"question": question, "answer": chat["answer"]}
                return jsonify(data)

            if "open app" in question:
                    question = question.replace("open app","")
                    pyautogui.press("super")
                    pyautogui.typewrite(question)
                    pyautogui.sleep(0)
                    pyautogui.press("enter")


            if "temperature" in question:
                url = f"https://www.google.com/search?q={question}"
                webbrowser.open(url)
            if "search" and "on google" in question:
                url = f"https://www.google.com/search?q={question}"
                webbrowser.open(url)
            if "search" and "on youtube" in question:
                url = f"https://www.youtube.com/search?q={question}"
                webbrowser.open(url)
            if "weather" in question:
                url = f"https://www.google.com/search?q={question}"
                webbrowser.open(url)

            else:
                genai.configure(api_key=os.environ["gemini_api"])

                # Create the model
                generation_config = {
                    "temperature": 1,
                    "top_p": 0.95,
                    "top_k": 40,
                    "max_output_tokens": 8192,
                    "response_mime_type": "text/plain",
                }

                model = genai.GenerativeModel(
                    model_name="gemini-2.0-flash-exp",
                    generation_config=generation_config,
                )

                chat_session = model.start_chat(
                    history=[]
                )

                response_text = chat_session.send_message(question)

                # Save the conversation in MongoDB.
                mongo.db.chats.insert_one({"question": question, "answer": response_text.text})

                return jsonify({"answer": response_text.text})

        except Exception as e:
            print(f"Error during API request: {e}")
            return jsonify({"error": "Internal server error"}), 500

    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss?"}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=5001)

