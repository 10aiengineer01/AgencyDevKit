import sys
import subprocess
from pathlib import Path
import os

def check_and_install_dependencies():
    """Check and install required dependencies"""
    required_packages = [
        'agency-swarm',
        'openai',
        'python-dotenv'
    ]
    
    try:
        # Try importing each package
        missing_packages = []
        for package in required_packages:
            try:
                __import__(package)
            except ImportError:
                missing_packages.append(package)
        
        if missing_packages:
            print("📦 Installing required packages...")
            for package in missing_packages:
                try:
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
                except subprocess.CalledProcessError:
                    print(f"⚠️ Failed to install {package}")
                    return False
            print("✅ Dependencies installed successfully")
            return True
        
        return True
    except Exception as e:
        print(f"⚠️ Error checking dependencies: {str(e)}")
        print("\nPlease install the required packages manually using:")
        print("pip install agency-swarm openai python-dotenv")
        return False

# Check dependencies before importing
if check_and_install_dependencies():
    from dotenv import load_dotenv
    from openai import OpenAI
else:
    sys.exit(1)

class start_dev:
    def __init__(self) -> None:
        self.base_path = Path.cwd()
        self.env_path = self.base_path / '.env'
        self.venv_path = self.base_path / 'env'
        self.composer_path = self.base_path / '.composer'
        self.requirements_path = self.base_path / 'requirements.txt'

    def setup_virtual_env(self):
        """Create and activate virtual environment"""
        if not self.venv_path.exists():
            subprocess.run([sys.executable, '-m', 'venv', 'env'])
            print("✅ Created virtual environment")

        # Install dependencies
        pip_cmd = str(self.venv_path / 'Scripts' / 'pip') if os.name == 'nt' else str(self.venv_path / 'bin' / 'pip')
        subprocess.run([pip_cmd, 'install', 'agency-swarm'])
        subprocess.run([pip_cmd, 'install', 'openai'])
        print("✅ Installed dependencies")

    def create_requirements_file(self):
        """Create requirements.txt file"""
        requirements_content = """agency-swarm>=0.1.0
openai>=1.3.0
python-dotenv>=1.0.0"""
        
        with open(self.requirements_path, 'w', encoding='utf-8') as f:
            f.write(requirements_content)
        print("✅ Created requirements.txt")

    def create_composer_file(self):
        """Create composer.json file"""
        composer_content = """
        # AI Agent Creator Instructions for Agency Swarm Framework

        Agency Swarm is a framework that allows anyone to create a collaborative swarm of agents (Agencies), each with distinct roles and capabilities. Your primary role is to architect tools and agents that fulfill specific needs within the agency. This involves:

        1. **Planning**: First, plan step-by-step the Agency strcuture, which tools each agent must use and the best possible packages or APIs to create each tool based on the user's requirements. Ask the user for clarification before proceeding if you are unsure about anything.
        2. **Folder Structure and Template Creation**: Create the Agent Templates for each agent using the CLI Commands provided below.
        3. **Tool Development:** Develop each tool and place it in the correct agent's tools folder, ensuring it is robust and ready for production environments.
        4. **Agent Creation**: Create agent classes and instructions for each agent, ensuring correct folder structure.
        5. **Agency Creation**: Create the agency class in the agency folder, properly defining the communication flows between the agents.
        6. **Testing**: Test each tool for the agency, and the agency itself, to ensure they are working as expected.
        7. **Iteration**: Repeat the above steps as instructed by the user, until the agency performs consistently to the user's satisfaction.

        You will find a detailed guide for each of the steps below.

        # Step 1: Planning

        Before proceeding with the task, make sure you have the following information:

        - The mission and purpose of the agency.
        - Description of the operating environment of the agency.
        - The roles and capabilities of each agent in the agency.
        - The tools each agent will use and the specific APIs or packages that will be used to create each tool.
        - Communication flows between the agents.

        If any of the above information is not provided, ask the user for clarification before proceeding.

        # Step 2: Folder Structure and Template Creation

        To create the folder structure and agent templates, follow these steps:

        1. Create the main folder for the agency with the following command:

        ```bash
        mkdir <agency_name>
        ```

        2. Create the Agent Templates inside the agency folder for each agent using the CLI command below:

        ```bash
        agency-swarm create-agent-template --name "AgentName" --description "Agent Description" --path "/path/to/agency/folder"
        ```

        You must repeat this step for each agent in the agency. Make sure to correctly specify the path to the agency folder.

        ### Understanding the Folder Structure

        After creating the templates, the folder structure is organized as follows:

        ```
        agency_name/
        ├── agent_name/
        │   ├── __init__.py
        │   ├── agent_name.py
        │   ├── instructions.md
        │   └── tools/
        │       ├── tool_name1.py
        │       ├── tool_name2.py
        │       ├── tool_name3.py
        │       ├── ...
        ├── another_agent/
        │   ├── __init__.py
        │   ├── another_agent.py
        │   ├── instructions.md
        │   └── tools/
        │       ├── tool_name1.py
        │       ├── tool_name2.py
        │       ├── tool_name3.py
        │       ├── ...
        ├── agency.py
        ├── agency_manifesto.md
        ├── requirements.txt
        └──...
        ```

        - Each agency and agent has its own dedicated folder.
        - Within each agent folder:

        - A 'tools' folder contains all tools for that agent.
        - An 'instructions.md' file provides agent-specific instructions.
        - An '**init**.py' file contains the import of the agent.

        - Tool Import Process:

        - Create a file in the 'tools' folder with the same name as the tool class.
        - Tools are automatically imported to the agent class.
        - All new requirements must be added to the requirements.txt file.

        - Agency Configuration:
        - The 'agency.py' file is the main file where all new agents are imported.
        - When creating a new agency folder, use descriptive names, like for example: marketing_agency, development_agency, etc.

        Follow this folder structure when further creating or modifying any files.

        # Step 3: Tool Creation

        Tools are the specific actions that agents can perform. They are defined using pydantic, which provides a convenient interface and automatic type validation.

        #### 1. Import Necessary Modules

        Start by importing `BaseTool` from `agency_swarm.tools` and `Field` from `pydantic`. These imports will serve as the foundation for your custom tool class. Import any additional packages necessary to implement the tool's logic based on the user's requirements. Import `load_dotenv` from `dotenv` to load the environment variables.

        ```python
        from agency_swarm.tools import BaseTool
        from pydantic import Field
        import os
        from dotenv import load_dotenv

        load_dotenv() # always load the environment variables
        ```

        #### 2. Define Your Tool Class and Docstring

        Create a new class that inherits from `BaseTool`. Write a clear docstring describing the tool’s purpose. This docstring is crucial as it helps agents understand how to use the tool. `BaseTool` extends `BaseModel` from pydantic.

        ```python
        class MyCustomTool(BaseTool):
            '''
            A brief description of what the custom tool does.
            The docstring should clearly explain the tool's purpose and functionality.
            It will be used by the agent to determine when to use this tool.
            '''
        ```

        #### 3. Specify Tool Fields

        Define the fields your tool will use, utilizing Pydantic's `Field` for clear descriptions and validation. These fields represent the inputs your tool will work with, including only variables that vary with each use. Define any constant variables globally.

        ```python
        example_field: str = Field(
            ..., description="Description of the example field, explaining its purpose and usage for the Agent."
        )
        ```

        #### 4. Implement the `run` Method

        The `run` method is where your tool's logic is executed. Use the fields defined earlier to perform the tool's intended task. It must contain the actual fully functional correct python code. It can utilize various python packages, previously imported in step 1.

        ```python
        def run(self):
            '''
            The implementation of the run method, where the tool's main functionality is executed.
            This method should utilize the fields defined above to perform the task.
            '''
            # Your custom tool logic goes here
        ```

        ### Best Practices

        - **Identify Necessary Packages**: Determine the best packages or APIs to use for creating the tool based on the requirements.
        - **Documentation**: Ensure each class and method is well-documented. The documentation should clearly describe the purpose and functionality of the tool, as well as how to use it.
        - **Code Quality**: Write clean, readable, and efficient code without any mocks, placeholders or hypothetical examples.
        - **Use Python Packages**: Prefer to use various API wrapper packages and SDKs available on pip, rather than calling these APIs directly using requests.
        - **Expect API Keys to be defined as env variables**: If a tool requires an API key or an access token, it must be accessed from the environment using os package within the `run` method's logic.
        - **Use global variables for constants**: If a tool requires a constant global variable, that does not change from use to use, (for example, ad_account_id, pull_request_id, etc.), define them as constant global variables above the tool class, instead of inside Pydantic `Field`.
        - **Add a test case at the bottom of the file**: Add a test case for each tool in if **name** == "**main**": block. It will be used to test the tool later.

        ### Complete Example of a Tool File

        ```python
        # MyCustomTool.py
        from agency_swarm.tools import BaseTool
        from pydantic import Field
        import os
        from dotenv import load_dotenv

        load_dotenv() # always load the environment variables

        account_id = "MY_ACCOUNT_ID"
        api_key = os.getenv("MY_API_KEY") # or access_token = os.getenv("MY_ACCESS_TOKEN")

        class MyCustomTool(BaseTool):
            '''
            A brief description of what the custom tool does.
            The docstring should clearly explain the tool's purpose and functionality.
            It will be used by the agent to determine when to use this tool.
            '''
            # Define the fields with descriptions using Pydantic Field
            example_field: str = Field(
                ..., description="Description of the example field, explaining its purpose and usage for the Agent."
            )

            def run(self):
                '''
                The implementation of the run method, where the tool's main functionality is executed.
                This method should utilize the fields defined above to perform the task.
                '''
                # Your custom tool logic goes here
                # Example:
                # do_something(self.example_field, api_key, account_id)

                # Return the result of the tool's operation as a string
                return "Result of MyCustomTool operation"

        if __name__ == "__main__":
            tool = MyCustomTool(example_field="example value")
            print(tool.run())
        ```

        Remember, each tool code snippet you create must be fully ready to use. It must not contain any mocks, placeholders or hypothetical examples. Ask user for clarification if needed.

        # Step 4: Agent Creation

        Each agent has it's own unique role and functionality and is designed to perform specific tasks. To create an agent:

        1. **Create an Agent class in the agent's folder.**

        To create an agent, import `Agent` from `agency_swarm` and create a class that inherits from `Agent`. Inside the class you can adjust the following parameters:

        ```python
        from agency_swarm import Agent

        class CEO(Agent):
            def __init__(self):
                super().__init__(
                    name="CEO",
                    description="Responsible for client communication, task planning and management.",
                    instructions="./instructions.md", # instructions for the agent
                    tools_folder="./tools", # folder containing the tools for the agent
                    temperature=0.5,
                    max_prompt_tokens=25000,
                )
        ```

        - **name**: The agent's name, reflecting its role.
        - **description**: A brief summary of the agent's responsibilities.
        - **instructions**: Path to a markdown file containing detailed instructions for the agent.
        - **tools_folder**: A folder containing the tools for the agent. Tools will be imported automatically. Each tool class must be named the same as the tool file. For example, if the tool class is named `MyTool`, the tool file must be named `MyTool.py`.
        - **Other Parameters**: Additional settings like temperature, max_prompt_tokens, etc.

        Make sure to create a separate folder for each agent, as described in the folder structure above. After creating the agent, you need to import it into the agency.py file.

        2. **Create an `instructions.md` file in the agent's folder.**

        Each agent also needs to have an `instructions.md` file, which is the system prompt for the agent. Inside those instructions, you need to define the following:

        - **Agent Role**: A description of the role of the agent.
        - **Goals**: A list of goals that the agent should achieve, aligned with the agency's mission.
        - **Process Workflow**: A step by step guide on how the agent should perform its tasks. Each step must be aligned with the other agents in the agency, and with the tools available to this agent.

        Use the following template for the instructions.md file:

        ```md
        # Agent Role

        A description of the role of the agent.

        # Goals

        A list of goals that the agent should achieve, aligned with the agency's mission.

        # Process Workflow

        1. Step 1
        2. Step 2
        3. Step 3
        ```

        Be conscience when creating the instructions, and avoid any speculation.

        #### Code Interpreter and FileSearch Options

        To utilize the Code Interpreter tool (the Jupyter Notebook Execution environment, without Internet access) and the FileSearch tool (a Retrieval-Augmented Generation (RAG) provided by OpenAI):

        1. **Import the tools:**

        ```python
        from agency_swarm.tools import CodeInterpreter, FileSearch
        ```

        2. **Add the tools to the agent's tools list:**

        ```python
        agent = Agent(
            name="MyAgent",
            tools=[CodeInterpreter, FileSearch],
            # ... other agent parameters
        )
        ```

        Typically, you only need to add the Code Interpreter and FileSearch tools if the user requests you to do so.

        # Step 5: Agency Creation

        Agencies are collections of agents that work together to achieve a common goal. They are defined in the `agency.py` file, which you need to create in the agency folder.

        1. **Create an `agency.py` file in the agency folder.**

        To create an agency, import `Agency` from `agency_swarm` and create a class that inherits from `Agency`. Inside the class you can adjust the following parameters:

        ```python
        from agency_swarm import Agency
        from CEO import CEO
        from Developer import Developer
        from VirtualAssistant import VirtualAssistant

        dev = Developer()
        va = VirtualAssistant()

        agency = Agency([
                ceo,  # CEO will be the entry point for communication with the user
                [ceo, dev],  # CEO can initiate communication with Developer
                [ceo, va],   # CEO can initiate communication with Virtual Assistant
                [dev, va]    # Developer can initiate communication with Virtual Assistant
                ],
                shared_instructions='agency_manifesto.md', #shared instructions for all agents
                temperature=0.5, # default temperature for all agents
                max_prompt_tokens=25000 # default max tokens in conversation history
        )

        if __name__ == "__main__":
            agency.run_demo() # starts the agency in terminal
        ```

        #### Communication Flows

        In Agency Swarm, communication flows are directional, meaning they are established from left to right in the `agency_chart` definition. For instance, in the example above, the CEO can initiate a chat with the developer (dev), and the developer can respond in this chat. However, the developer cannot initiate a chat with the CEO. The developer can initiate a chat with the virtual assistant (va) and assign new tasks.

        To allow agents to communicate with each other, simply add them in the second level list inside the `agency_chart` like this: `[ceo, dev], [ceo, va], [dev, va]`. The agent on the left will be able to communicate with the agent on the right.

        2. **Define the `agency_manifesto.md` file.**

        Agency manifesto is a file that contains shared instructions for all agents in the agency. It is a markdown file that is located in the agency folder. Please write the manifesto file when creating a new agency. Include the following:

        - **Agency Description**: A brief description of the agency.
        - **Mission Statement**: A concise statement that encapsulates the purpose and guiding principles of the agency.
        - **Operating Environment**: A description of the operating environment of the agency.

        # Step 6: Testing

        The final step is to test each tool for the agency, to ensure they are working as expected.

        1. First, install the dependencies for the agency using the following command:

        ```bash
        pip install -r agency_name/requirements.txt
        ```

        2. Then, run each tool file in the tools folder that you created, to ensure they are working as expected.

        ```bash
        python agency_name/agent_name/tools/tool_name.py
        ```

        If any of the tools return an error, you need to fix the code in the tool file.

        3. Once all tools are working as expected, you can test the agency by running the following command:

        ```bash
        python agency_name/agency.py
        ```

        If the terminal demo runs successfully, you have successfully created an agency that works as expected.

        # Step 7: Iteration

        Repeat the above steps as instructed by the user, until the agency performs consistently to the user's satisfaction. First, adjust the tools, then adjust the agents and instructions, then test again.

        # Notes

        IMPORTANT: NEVER output code snippets or file contents in the chat. Always create or modify the actual files in the file system. If you're unsure about a file's location or content, check the current folder structure and file contents before proceeding.

        When creating or modifying files:

        1. Use the appropriate file creation or modification syntax (e.g., ```python:path/to/file.py for Python files).
        2. Write the full content of the file, not just snippets or placeholders.
        3. Ensure all necessary imports and dependencies are included.
        4. Follow the specified file creation order rigorously: 1. tools, 2. agents, 3. agency, 4. requirements.txt.

        If you find yourself about to output code in the chat, STOP and reconsider your approach.
        """
        
        with open(self.composer_path, 'w', encoding='utf-8') as f:
            f.write(composer_content)
        print("✅ Created composer")
        
    def create_gitignore_file(self):
        """Create .gitignore file and add .composer entry"""
        gitignore_content = ".composer\n"
        gitignore_path = self.base_path / '.gitignore'
        
        with open(gitignore_path, 'w', encoding='utf-8') as f:
            f.write(gitignore_content)
        print("✅ Created .gitignore and added .composer")

    def handle_api_key(self):
        """Handle the OpenAI API key setup"""
        load_dotenv()
        api_key = os.getenv('OPENAI_API_KEY')
        
        if not api_key:
            print("⚠️ No OpenAI API key found in .env file")
            api_key = input("Please enter your OpenAI API key: ")
            
            # Create or append to .env file
            if not self.env_path.exists():
                with open(self.env_path, 'w', encoding='utf-8') as f:
                    f.write(f'OPENAI_API_KEY={api_key}\n')
            else:
                with open(self.env_path, 'a', encoding='utf-8') as f:
                    f.write(f'\nOPENAI_API_KEY={api_key}')
        
        # Set environment variable
        if os.name == 'nt':  # Windows
            subprocess.run(['setx', 'OPENAI_API_KEY', api_key])
        else:  # Unix-like
            with open(os.path.expanduser('~/.bashrc'), 'a', encoding='utf-8') as f:
                f.write(f'\nexport OPENAI_API_KEY={api_key}')
        print("✅ Set up API key")
        return api_key

    def create_composer_prompt(self, project_description: str, api_key: str) -> str:
        """Create a detailed prompt for the Cursor composer based on project description"""
        try:
            client = OpenAI(api_key=api_key)
            
            messages = [
                {"role": "system", "content": "You are an expert at creating detailed project specifications and development plans. Your task is to create a comprehensive prompt for the Cursor composer based on the project description provided."},
                {"role": "user", "content": f"""Please create a detailed development plan and specification for the following project:

                {project_description}

                Include the following aspects:
                1. Project Overview
                2. Technical Requirements
                3. Architecture Design
                4. Key Features and Components
                5. Development Phases
                6. Testing Strategy
                7. Dependencies and Tools
                8. Security Considerations
                9. Performance Requirements
                10. Deployment Strategy

                Format the response in a clear, structured manner suitable for a development team."""}
            ]

            response = client.chat.completions.create(
                model="o1-preview",
                messages=messages,
            )

            composer_prompt = response.choices[0].message.content
            
            # Save the composer prompt to a file
            prompt_file = self.base_path / 'composer_prompt.md'
            with open(prompt_file, 'w', encoding='utf-8') as f:
                f.write(composer_prompt)
            
            print("✅ Created composer prompt and saved to composer_prompt.md")
            return composer_prompt

        except Exception as e:
            print(f"⚠️ Error creating composer prompt: {str(e)}")
            return None

    def run(self):
        """Run the setup process"""
        print("🚀 Starting development environment setup...")
        
        # Create configuration files
        self.create_requirements_file()
        self.create_composer_file()
        self.create_gitignore_file()  # Create .gitignore and add .composer
        
        # Setup virtual environment and install dependencies
        self.setup_virtual_env()
        
        # Handle API key
        api_key = self.handle_api_key()
        
        # Get project description and create composer prompt
        print("\n📝 Please provide a description of your project:")
        project_description = input("> ")
        
        if project_description:
            composer_prompt = self.create_composer_prompt(project_description, api_key)
            if composer_prompt:
                print("\n📋 Composer prompt has been created and saved to 'composer_prompt.md'")
                print("You can now use this prompt with the Cursor composer to start your project.")
        # Self-delete the script
        script_path = os.path.abspath(__file__)
        print(f"🗑️ Deleting the setup script: {script_path}")
        os.remove(script_path)
        print("\n✨ Setup complete! Your development environment is ready.")

if __name__ == "__main__":
    setup = start_dev()
    setup.run()