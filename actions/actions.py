
from typing import Any, Text, Dict, List
from similarity.main import CalculateSimilarity
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import csv, random
import os
import sys

QUESTIONS_FINAL = []
ANSWERS_FINAL = []
USER_DICT = {}
Q_dict = {}
A_dict = {}
csv_data = []
anslist =[]
RAND_ID_LIST=[]
user_input=[]
FINAL_SCORE = []
DOMAIN = None


class ActionReady(Action):
    def name(self) -> Text:
        return "action_ready"

    def get_question(self):
        with open(os.path.join(os.path.dirname(__file__),"python_demo.csv"), "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                csv_data.append(row)
                Q_dict[row[1]] = row[4]
        RAND_ID_LIST.extend(random.sample(list(Q_dict.keys()), 5))
        for i in RAND_ID_LIST:
            QUESTIONS_FINAL.append(Q_dict[i])

        for k, v in Q_dict.items():
            a_list = []
            for row in csv_data:
                if str(k) == str(row[1]):
                    a_list.append(row[6])

            A_dict[k] = a_list


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        self.get_question()

        return []


def send_question():
    for question in QUESTIONS_FINAL:
        yield question

next_question = send_question()


class ActionAskQuestion(Action):
    def name(self) -> Text:
        return "action_ask_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = next(next_question)
        dispatcher.utter_message(text=question)

        return []


class ActionGetAnswer(Action):
    def name(self) -> Text:
        return "get_answer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = tracker.latest_message['text']

        ANSWERS_FINAL.append(message)

        return []

class ActionGetSimilarity(Action):
    def name(self) -> Text:
        return "get_similarity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(RAND_ID_LIST)
        for i in range(0, len(RAND_ID_LIST)):
            USER_DICT[RAND_ID_LIST[i]] = ANSWERS_FINAL[i]

        for k, v in USER_DICT.items():
            anslist = A_dict[k]
            user_input.append(v)
            print("entering run1")
            result ='Marks given:' + str(CalculateSimilarity(RAND_ID_LIST,anslist,user_input))
            FINAL_SCORE.append(result)

        dispatcher.utter_message(text=str(FINAL_SCORE))
        return []
