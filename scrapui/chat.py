import nltk
from nltk.chat.util import Chat 

ref = {
        "you":'me',
}

pair = [
    [
        'Hi|hey|hello',
        [
            'Hello',
            'Hi,my name is trsh ,How can i help you?',
            'hey there',
        ]
    ],
    [
        'how are you?',
        [
            'i,m doing great',
            'fine',
            'good',
        ]
    ],
    
]


def chatbot(data):
    con = {}
    if data == None:
        con['message'] = 'I dont understand please provide something'
        return

    chat = Chat(pair,ref)

    chat.converse()

if __name__ == '__main__':
    chatbot('')

