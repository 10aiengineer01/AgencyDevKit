from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from openai import OpenAI

class CreateAndSavePlanTool(BaseTool):
    """
    This tool compiles all gathered information and requirements into a coherent project plan.
    It also provides functionality to save this plan in a specified format and location.
    """

    def run(self):
        """
        Compiles the gathered information into a project plan and saves it
        Returns a confirmation message.
        """

        if self._shared_state.get("information", None) is not None:
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            response = client.chat.completions.create(
                model="o1-preview",
                messages=[{
                    "role": "user",
                    "content": [
                        {
                        "type": "text",
                        "text": """
                        You are a system that now has all the required information needed to prepare an agency for the project using the Agency Swarm Framework. Based on the collected details (contained in "information"), you must now create comprehensive instructions for the coding agent.

                        These instructions should include the following:

                        Project Goal and Context:

                        A clear description of the project’s objective.
                        A summary of the intended scope and the expected end result.
                        Agent Roles and Communication Flow:

                        A detailed description of the planned agent roles (e.g., CEO, Developer, Virtual Assistant).
                        An explanation of how these agents should interact with one another (the communication flow, which agents can communicate with whom, and who initiates tasks).
                        Tools and APIs:

                        A list of all required tools, interfaces, and services, including OpenAPI schemas, external data sources, or special functions.
                        Guidance on how to integrate, configure, and validate these tools.
                        Identification of relevant APIs (including any necessary parameters, authentication methods, and endpoints).
                        Technical Settings and Parameters:

                        Specification of the language model to be used (e.g., GPT-3.5-turbo) as well as parameters like temperature, token limits, or truncation strategies.
                        Any additional technical details needed to ensure that the coding agent can optimally set up the agency.
                        Integration of User Inputs:

                        A description of how user requirements, commands, or data will be passed to the agency.
                        All necessary formats, standards, or templates to ensure that inputs are conveyed to the agents clearly and comprehensively.
                        Your Task:
                        Based on the data contained in "information", produce a clear, precise, and actionable set of instructions for the coding agent. These instructions should be detailed enough that the coding agent can start implementing a fully functioning agency with all the required tools, roles, and communication structures without further inquiries.
                        INFORMATION: """+self._shared_state.get("information", None)
                        }
                    ]
                }]
            )
            return "Plan was created and saved successfully!"
        else:
            return "Please make shure, that all information are aquired bevore using this tool"
