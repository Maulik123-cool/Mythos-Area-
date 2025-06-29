# Mythos-Area-
Step into the Mythos Arena, where gods and monsters throw down in a no-nonsense battle to see who’s the ultimate boss! Pick your attack — a zap of lightning or a fiery smash — and watch your opponent’s health bar drop like a bad joke. It’s fast, it’s fun, and yes, it’s all happening live in your browser. 

![image](https://github.com/user-attachments/assets/df005e1a-7e52-475c-8c2b-e22bd3b015f2)

![image](https://github.com/user-attachments/assets/9d0bd757-2ea1-400c-9eec-e2f59063c1ef)

![image](https://github.com/user-attachments/assets/18868471-f6a8-4bad-9f18-955f72805c0b)

![image](https://github.com/user-attachments/assets/3f6e812f-f824-46ca-ba1c-e0f3c0569b90)


# Mythos Arena

Welcome to **Mythos Arena** — where gods and monsters throw down in a no-nonsense battle for glory!

## What is this?

Mythos Arena is a real-time multiplayer browser game where you pick attacks like lightning zaps or fiery smashes and try to beat your opponent by smashing their health bar to zero.

It’s fast, it’s fun, and it’s all happening live thanks to Python, Flask, and SocketIO magic.

## How to Play

1. Run the backend server with:

   ```bash
   python app.py

## Why did I build this?

I wanted to create a project that was challenging and rewarding — something that would take a good chunk of time (15-20 hours) to build from scratch, combining backend and frontend skills.

I thought: what’s more fun than a game? And what’s cooler than making a multiplayer game that actually works in real time?

So I decided to make **Mythos Arena** — a game where mythical powers meet coding wizardry. It pushed me to learn:

- Real-time communication using WebSockets with Python Flask-SocketIO  
- Frontend animations and UI design with HTML/CSS/JavaScript  
- Synchronizing game state between multiple players live in the browser  

It’s been an amazing learning experience and a great way to showcase complex programming skills in a fun way.

---

## How does it work?

- The backend is powered by Python Flask with Flask-SocketIO for real-time communication.  
- Players connect through the browser, which loads the game UI built with HTML, CSS, and JavaScript.  
- When a player clicks an attack button, the browser sends a message to the server via WebSockets.  
- The server broadcasts the damage to all connected clients, updating health bars instantly.  
- Two players can open the game in different tabs or on separate devices and battle live!

---

## How to run Mythos Arena locally

1. Make sure you have Python 3 installed and added to your system PATH.  
2. Install required packages:

   ```bash
   pip install flask flask-socketio

