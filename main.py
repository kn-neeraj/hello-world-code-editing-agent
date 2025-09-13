import os
import sys
from typing import Tuple
import anthropic

class ToolDefinition:
    """Defines a tool with a name and description."""
    def __init__(self, name: str, description: str, input_schema: dict, function: callable):
        self.name = name
        self.description = description
        self.input_schema = input_schema
        self.function = function

class Agent:
    def __init__(self, client:anthropic.Anthropic,get_user_message, tools: list[ToolDefinition]):
        """
        Initialize the agent with:
        - client: Anthropic API client for talking to Claude
        - get_user_message: Function that reads user input
        """
        self.client = client
        self.get_user_message = get_user_message
        self.tools = {tool.name: tool for tool in tools}
    
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
        Include tool definitions.
        """
        anthropic_tools = []
        for tool in self.tools.values():
            anthropic_tools.append({
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.input_schema
            })

        # Build the API call parameters
        api_params = {
            "model": "claude-sonnet-4-20250514",
            "messages": conversation,
            "max_tokens": 1024,
        } 

        if anthropic_tools:
            api_params["tools"] = anthropic_tools
        
        message = self.client.messages.create(**api_params)
        # message = self.client.messages.create(
        #     model="claude-sonnet-4-20250514",
        #     messages=conversation,
        #     max_tokens=1024,
        # )

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


# =============================================================================
# TOOL IMPLEMENTATIONS
# =============================================================================
def read_file(input_data: dict) -> str:
    """
    Read the contents of a file.
    This is the actual function that executes when Claude wants to read a file.
    
    Args:
        input_data: Dictionary containing the tool inputs from Claude
                   Expected format: {"path": "filename.txt"}
    
    Returns:
        String containing the file contents
    
    Raises:
        ValueError: If no path provided
        FileNotFoundError: If file doesn't exist
        Exception: For other file reading errors
    """
    path = input_data.get("path", "")
    if not path:
        raise ValueError("Path is required")
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            contents = f.read()
        return contents
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except UnicodeDecodeError:
        # Handle binary files
        with open(path, 'rb') as f:
            content = f.read()
        return f"<Binary file, {len(content)} bytes>"
    except Exception as e:
        raise Exception(f"Error reading file: {e}")

READ_FILE_DEFINITION = ToolDefinition(
    name="read_file",
    description="Read the contents of a given relative file path. Use this when you want to see what's inside a file. Do not use this with directory names.",
    input_schema={
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "The relative path of a file in the working directory."
            }
        },
        "required": ["path"]
    },
    function=read_file
)


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

    tools = [READ_FILE_DEFINITION]

    agent = Agent(client=client, get_user_message=get_user_message, tools=tools)
    try:
        agent.run()
    except Exception as e:
        print("Error occurred while running the agent:", e)


if __name__ == "__main__":
    main()
