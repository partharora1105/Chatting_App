import json

##chat = []
##jsonString = json.dumps(chat)
##jsonFile = open("chat.json", "w")
##jsonFile.write(jsonString)
##jsonFile.close()
##


chat = {"UserData": {"parth": "p", "richard": "r", "sub": "s", "pranjal": "p", "sarah": "s", "mohit": "m", "aadya": "a", "prabhav": "p", "asante": "a"}, "ChatData": [[["parth", "richard"], [["parth", "hi"], ["richard", "heyy"], ["parth", "how are you"], ["richard", "awesome"], ["richard", "how was your thanksgiving"], ["parth", "amazing "]]], [["parth", "sub"], [["parth", "hey sub!!"], ["sub", "hey, long time no see!"], ["parth", "how is your arm"], ["sub", "better"], ["sub", "thanks for asking"], ["parth", "get well soon"]]], [["aadya", "parth"], [["aadya", "hey"], ["parth", "heyyy"], ["parth", "where are you?"], ["aadya", "Atlantic Station"], ["aadya", "coming to dorm soon"], ["parth", "oh ohk, waiting"]]], [["parth", "pranjal"], [["parth", "heyyyyy"], ["pranjal", "heyyy"]]], [["asante", "parth"], [["asante", "look at my tik toks"]]]]}
jsonString = json.dumps(chat)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()


'''

{
"UserData": {"sanya": "s", "parth": "p", "jayanth": "j", "richard": "r"},
"ChatData": [
[["prabhav", "parth"],
[  ["prabhav", "hi"], ["prabhav", "hi"], ["prabhav", "hi"]  ]
],[
["prabhav", "richard"],
[["prabhav", "hi"], ["prabhav", "jj"]]
],[
["prabhav", "sanya"],
[["prabhav", "j"]]
]]}
'''

