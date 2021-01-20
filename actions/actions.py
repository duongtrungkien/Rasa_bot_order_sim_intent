# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

class ActionAuth(Action):

    def name(self) -> Text:
        return "action_auth"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        """
        Todo: Handle authentication flow and store the token
        """
        dispatcher.utter_message(text="Authenticate Success")

        return []


class ActionGetSIMAvailabilities(Action):

    def name(self) -> Text:
        return "action_get_sim_availabilities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        ToDo: Fetch the subscriptions and handle error
              GET /simcard/availabilities
        """
        # There are three available subscription in this case
        dummy_subs = [
            {"mobileNumber": "05123455436", "contacts": [{"contactId": 0, "address": {"stressAddress": "Testikatu 1"}}]},
            {"mobileNumber": "05156756754", "contacts": [{"contactId": 0, "address": {"stressAddress": "Testikatu 1"}}]},
            {"mobileNumber": "05966753129", "contacts": [{"contactId": 0, "address": {"stressAddress": "Testikatu 1"}}]}]

        dispatcher.utter_message(
            text="Please enter which number you want to get new card: {}, {}, {}".format(dummy_subs[0]["mobileNumber"],
                                                                                         dummy_subs[1]["mobileNumber"],
                                                                                         dummy_subs[2]["mobileNumber"]))
        return []

class ActionOrderSimCard(Action):

    def name(self) -> Text:
        return "action_order_sim_card"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        """
        ToDo: Order sim card for user and handle error
              POST /simcard/order
        """
        dispatcher.utter_message(text="Great! Read the instructions for activation from this link here."
                                 "\nHave a nice day! Thank you!")
        return []
