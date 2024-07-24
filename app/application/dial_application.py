import json
from typing import Any, Optional, Tuple

from aidial_sdk.chat_completion import ChatCompletion, Choice, Message, Request, Response
from aidial_sdk.utils.action_registry import ActionRegistry


class DialApplication(ChatCompletion):
    action_registry = ActionRegistry()

    async def chat_completion(self, request: Request, response: Response) -> None:
        user_message = request.messages[-1]
        user_query = user_message.content or ""

        action_id, action_response = self.process_action(user_message)

        with response.create_single_choice() as choice:
            if action_id:
                choice.append_content(f"Action call: {action_id}, response: [ {action_response} ]")
            else:
                choice.append_content(f"Hello from DIAL application. You said: '{user_query}', right?")
            self.add_actions(choice)

    def process_action(self, user_message: Message) -> Tuple[Optional[str], Optional[Any]]:
        if user_message.action_call and user_message.action_call.action_id:
            action_id = user_message.action_call.action_id

            try:
                arguments = json.loads(user_message.action_call.arguments or "")
            except (json.JSONDecodeError, TypeError) as e:
                print(f"Error parsing arguments '{user_message.action_call.arguments}': {e}")
                arguments = {}

            try:
                action_response = self.action_registry.call_action(action_id, **arguments)
            except Exception as e:
                print(f"Error calling action '{action_id}': {e}")
                action_response = None

            return action_id, action_response

        return None, None

    def add_actions(self, choice: Choice):
        actions = [
            {"name": "Send the message: 'Hi there!'", "function": action_func_1},
            {"name": "Call the Action", "function": action_func_2}
        ]
        choice.set_actions(self.action_registry.set_actions(actions))


def action_func_1():
    return "Hi there!"


def action_func_2():
    return "Action called"
