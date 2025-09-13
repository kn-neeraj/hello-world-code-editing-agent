import os
import sys
from typing import Tuple
import anthropic

class Agent:
    def __init__(self, client:anthropic.Anthropic,get_user_message):
        """
        Initialize the agent with:
        - client: Anthropic API client for talking to Claude
        - get_user_message: Function that reads user input
        """
        self.client = client
        self.get_user_message = get_user_message
    
    def run(self):
        """
        Main agent loop - we'll implement this in the next step
        """
        print("Chat with Claude (press Ctrl+D or Ctrl+C to exit):")
        conversation = []
        # Main conversation loop
        while True:
            print("\033[94mYou\033[0m: ", end="", flush=True)

            user_message, ok = self.get_user_message()
            if not ok:
                print("\nExiting chat.")
                break
            
            # Add user message to conversation history
            conversation.append({"role": "user", "content": user_message})

            # Send the conversation to Claude and get a response
            try:
                message = self.run_inference(conversation) 
            except Exception as e:
                print("Error calling Claude:", e)
                return

            # Extract the text content from Claude's response
            assistant_content = ""
            for content in message.content:
                if content.type == "text":
                    assistant_content += content.text
        

            # Add Claude's response to conversation history
            conversation.append({"role": "assistant", "content": assistant_content})
            
            # Print Claude's response 
            for content in message.content: 
                if content.type == "text": 
                    print("\033[92mClaude\033[0m:", content.text)
        
    def run_inference(self, conversation):
        """
        Send the conversation history to Claude and get a response.
        """
        message = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            messages=conversation,
            max_tokens=1024,
        )
        return message


def get_user_message() -> Tuple[str, bool]:
    """
    Read user input from the console.
    Returns a tuple of (message, success).
    - message: The user input string.
    - success: True if input was read successfully, False if exit command was given.
    """
    try:
        user_input = input()
        return user_input, True
    except (EOFError, KeyboardInterrupt):
        return "", False

def main():
    """
    Main entry point for the agent.
    - Reads the API key from environment variables.
    - Initializes the Anthropic client and the agent.
    - Starts the agent's run loop.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        sys.exit(1)  

    client = anthropic.Anthropic(api_key=api_key)
    agent = Agent(client=client, get_user_message=get_user_message)
    try:
        agent.run()
    except Exception as e:
        print("Error occurred while running the agent:", e)


if __name__ == "__main__":
    main()
