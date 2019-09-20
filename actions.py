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

bnp = BNP()
raphael = RaphaelPhrases()


class ActionHelloWorld(Action):

        def name(self) -> Text:
            return "action_bnp"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            rentabilidade_dia = bnp.rentabilidade_dia()
            dispatcher.utter_message("A rentabiliade no dia de hoje foi de {}".format(rentabilidade_dia))

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
