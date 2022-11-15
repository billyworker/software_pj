import model

def controller():
    while True:
        command = input()
        model.commandTranslator(command.upper())    #allow either upper case or lower case input
        pass

model.init()
controller()