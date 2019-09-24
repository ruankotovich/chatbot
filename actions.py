# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from src.bnp import BNP
from src.raphael import RaphaelPhrases

raphael = RaphaelPhrases()


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_bnp"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        bnp = BNP()
        data = bnp.data()
        dispatcher.utter_template("utter_bnp",
                                  tracker,
                                  fund_name=data['fund_name'],
                                  current_day=data['current_day'],
                                  daily_profitability=data['daily_profitability'],
                                  monthly_profitability=data['monthly_profitability'])
        return []


class ActionRaphael(Action):

    def name(self) -> Text:
        return "action_raphael_phases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = raphael.predict()
        dispatcher.utter_message(text)

        return []
