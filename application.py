import json
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__, static_folder="static")

@app.route('/chat/home',methods = ['POST', 'GET'])
def initialize():
    return render_template('chatHome.html')

@app.route('/chat/newAccount',methods = ['POST', 'GET'])
def newAccount():
    return render_template('SignUp.html')
    
    
@app.route('/chat/signup',methods = ['POST', 'GET'])
def signUp():
    username = request.form["username"].strip().lower()
    password = request.form["password"].strip().lower()
    readFile = open("static/chat_data/data.json", "r")
    readStr = readFile.read()
    dataDict = json.loads(readStr)
    readFile.close()
    if username not in dataDict["UserData"].keys():
        dataDict["UserData"][username] = password
        jsonDict = json.dumps(dataDict)
        writeFile = open("static/chat_data/data.json", "w")
        writeFile.write(jsonDict)
        writeFile.close()
        return render_template('choose.html', sender = username, senderDisplay = username[0].upper() + username[1:])
    else:
        error = "Username already exists!"
        return render_template('SignUpError.html', message = error)
    
@app.route('/chat/login',methods = ['POST', 'GET'])
def login():
    username = request.form["username"].strip().lower()
    password = request.form["password"].strip().lower()
    readFile = open("static/chat_data/data.json", "r")
    readStr = readFile.read()
    dataDict = json.loads(readStr)
    readFile.close()
    if username in dataDict["UserData"].keys() and dataDict["UserData"][username] == password:
        contactList = []
        for chatList in dataDict["ChatData"]:
            if username == chatList[0][0].strip().lower():
                contactList.append(chatList[0][1].strip()[0].upper() + chatList[0][1].strip()[1:].lower())
            elif username == chatList[0][1].strip().lower():
                contactList.append(chatList[0][0].strip()[0].upper() + chatList[0][0].strip()[1:].lower())
                
        return render_template('choose.html', sender = username,  senderDisplay = username[0].upper() + username[1:] , contacts = contactList)
    else:
        error = "Incorrect! Retry"
        return render_template('LoginError.html', message = error)


@app.route("/chat/choose" ,  methods =["POST", "GET" ])
def choose():
    convoList = []
    receiver = request.form["receiver"].strip().lower()
    sender = request.form["sender"].strip().lower()
    chatFile = open("static/chat_data/data.json" , "r")
    readChat = chatFile.read()
    masterData = json.loads(readChat)
    chatFile.close()
    chatLists = masterData["ChatData"]
    for chatList in chatLists:
        user1,user2 = chatList[0] 
        if (user1.lower() == sender.lower() and user2.lower() == receiver.lower()) or (user2.lower() == sender.lower() and user1.lower() == receiver.lower()):
            convoList = chatList[1]
            break
    
    return render_template('chat.html', sender = sender, receiver = receiver, chatList = convoList, senderDisplay = sender[0].upper() + sender[1:] , receiverDisplay = receiver[0].upper() + receiver[1:])

    
@app.route("/chat/send",methods = ['POST', 'GET'])
def sendText():
    sender = request.form["sender"].strip().lower()
    receiver = request.form["receiver"].strip().lower()
    text = request.form["tt"]
    chatFile = open("static/chat_data/data.json" , "r")
    readChat = chatFile.read()
    masterData = json.loads(readChat)
    chatFile.close()
    chatLists = masterData["ChatData"]
    chatExists = False
    for chatList in chatLists:
        user1,user2 = chatList[0]
        chatExists =  (user1.lower() == sender.lower() and user2.lower() == receiver.lower()) or (user2.lower() == sender.lower() and user1.lower() == receiver.lower())
        if chatExists:
            chatList[1].append([sender , text])
            convoList = chatList[1]
            break
    if not chatExists:
        chatLists.append([(sender, receiver) , [(sender , text)] ])
        convoList = [(sender , text)] 
    masterData["ChatData"] = chatLists
    chatJson = json.dumps(masterData)
    returnFile = open("static/chat_data/data.json" , "w")
    returnFile.write(chatJson)
    returnFile.close()

    return render_template('chat.html', sender = sender, receiver = receiver, chatList = convoList, senderDisplay = sender[0].upper() + sender[1:] , receiverDisplay = receiver[0].upper() + receiver[1:])

    
    
    
        
        
    

        
app.debug = True
app.run()

