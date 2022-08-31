# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import CollectingDispatcher

allowed_insurance_type = ['health','home','life']
allowed_states = ['JHR','KDH']


class validateQuoteForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_quote_form"

    def validate_insurance_type(
         self,
         slot_value: Any,
         dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: DomainDict,
    ) -> Dict[Text,Any]:

        """Validate Insurance Type"""
        # insurance_type = tracker.get_slot("insurance_type")
        if slot_value.lower() not in allowed_insurance_type:
            dispatcher.utter_message(text=f"We only provide Health/Home/Life")
            return {"insurance_type":None}
        
        dispatcher.utter_message(text=f"Good Job! U have chosen {slot_value}.")
        return {"insurance_type":slot_value}

    def validate_state(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: DomainDict,
    ) -> Dict[Text,Any]:

        """Validate state"""
        # state = tracker.get_slot("ask_state")
        
        if slot_value not in allowed_states:
            dispatcher.utter_message(text=f"We only have JHR and KDH")
            return {"state":None}

        dispatcher.utter_message(text=f"Good Job! U have chosen {slot_value} as your state.")
        return {"state":slot_value}

        





    


