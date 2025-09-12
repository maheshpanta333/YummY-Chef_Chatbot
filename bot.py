from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot_corpus
import time

def create_bot(namebot):
    bot=ChatBot(name=namebot, read_only=False,
                logic_adapters=[
                    'chatterbot.logic.BestMatch',
                    'chatterbot.logic.MathematicalEvaluation'
                ],
                storage_adapter="chatterbot.storage.SQLStorageAdapter")
    return bot

def train_bot(Bot):
    corpus_trainer=ChatterBotCorpusTrainer(Bot)
    corpus_trainer.train('chatterbot.corpus.english')



def custom_train(Bot,conversation):
    from chatterbot.trainers import ListTrainer
    trainer=ListTrainer(Bot)
    trainer.train(conversation)

def bot_response(Bot, userinput):
    greetings=['hi','hello','good morning','chef','ahoy','namaste','namaskar']
    bye=['bye','bye bye','see ya','c ya','farwell chef','sayonara']
    if userinput.lower().strip() in greetings:
        return f"Hello, I am your chef, throw me your questions!"
    elif userinput in bye:
        return f"see you fellow food enthusiast! Would love to see you again!"
    else:
        response=Bot.get_response(userinput)
        return response

    