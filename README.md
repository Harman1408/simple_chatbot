# 🗨️ Rule-Based Chatbot  

A simple **rule-based chatbot** built in **Python** using only basic concepts like functions, loops, and conditions (no external libraries).  

This project demonstrates how chatbots can respond to user queries using **predefined rules and keyword matching**.  

---

## 🚀 Features  
- Greets the user (e.g., hello, hi).  
- Introduces itself when asked *"Who are you?"*.  
- Responds to common queries like time and weather.  
- Provides default replies when it doesn’t understand.  
- Ends the chat when the user types **"bye"**.  

---

## 📂 Project Structure  

RuleBasedChatbot/
│── chatbot.py # Main Python code
│── README.md # Project documentation


---

## 🛠️ How It Works  
1. The chatbot takes user input inside a loop.  
2. It checks for **keywords** in the input (like "hello", "weather").  
3. If a keyword is found → it replies with a fixed response.  
4. If no keyword matches → it replies with a default message.  
5. The conversation ends when the user types **bye**.  

---

## ▶️ Usage  

### Run the program and Example Interaction:  
```bash
python chatbot.py

Example Interaction:

Chatbot: Hello! I am your assistant. Type 'bye' to end the chat.

You: hi  
Chatbot: Hi there! How can I help you today?  

You: who are you  
Chatbot: I am a simple rule-based chatbot created in Python.  

You: weather  
Chatbot: It's always sunny inside my program ☀️  

You: bye  
Chatbot: Goodbye! Have a great day 😊

