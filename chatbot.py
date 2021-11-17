from nltk.chat.util import Chat, reflections

print(reflections)

pairs = [
    ['my name is (.*)', ['Hello ! %1']],
    ['(hi|hello|hey|holla|hola)', ['Hey there !', 'Hi  there !', 'Hey !']],
    ['(.*)your name ?', ['My name is Ree Cee']],
    ['(.*) do you do ?', ['We provide a platform for learn, with a wide range of options !']],
    ['(.*) created you ?', ['Rishi Ahuja created me using python and NLTK']]

]
Chat = Chat(pairs, reflections)
Chat.converse()
