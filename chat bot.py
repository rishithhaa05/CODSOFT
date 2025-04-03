def chatbot():
    print("Simple Chatbot: Type 'bye' to exit")
while True:
    user_input=input("You:").lower()
    if user_input in['Hi','Hello','Hey','hey','hi','hello']:
        print("ChatBot:Hello! How can I help you")
    elif user_input in['How are you','How are you doing','how are you','how are you doing']:
        print("ChatBot:I'm just a Bot,but I'm doing well!How about you")
    elif user_input in['What is your name','Who are you ','what is your name','who are you']:
        print("ChatBot:I'm a simple Chatbot created to assist you!")
    elif user_input in['bye','exit','quit','Bye','Exit','Quit']:
        print("ChatBot:GoodBye! Have a great day!")
        break
    else:
        print("ChatBot:I'm sorry, I don't understand that.")
if __name__=="__main__":
    chatbot()
        
