from agency_swarm.tools import BaseTool
from pydantic import Field
import re
from openai import OpenAI
import os

class CheckRequirementsTool(BaseTool):
    """
    This tool analyzes project requirements to verify their completeness and feasibility.
    It identifies any missing or unclear elements that need further clarification.
    """

    information: str = Field(
        ..., description="The information from the user"
    )

    def run(self):
        """
        Analyzes the given requirements to identify missing or unclear elements.
        Returns a report highlighting areas that need further clarification.
        """
        if self._shared_state.get("information", None) is not None:
            past_information = self._shared_state.get("information")
            self._shared_state.set("information", past_information+"\n"+self.information)
        else:
            self._shared_state.set("information", self.information)
            past_information = ""
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                "role": "system",
                "content": [
                    {
                    "type": "text",
                    "text": """
                    You are a system whose task is to determine whether the currently available information is sufficient to create a final prompt for a coding agent. This coding agent will leverage the Agency Swarm Framework to establish an agency with the necessary tools. The basis for your analysis is the information stored in 'information'.

                    Evaluate the provided information against the following criteria, and then indicate whether additional details are needed. If so, specify exactly which details are missing.

                    Project Goals and Objectives:

                    Is there a clearly defined purpose for the agency?
                    Is the overall assignment or the desired end result precisely described?
                    Roles and Agent Structure:

                    Are the intended agent roles (e.g., CEO, Developer, Virtual Assistant, etc.) clearly named and described?
                    Is the communication flow between agents defined (i.e., which agent can communicate with whom, and who initiates communication)?
                    Tools and Their Applications:

                    Have the required tools been identified or must additional tools still be defined?
                    Are there specifications regarding special functions, interfaces (OpenAPI schemas), databases, or external services needed?
                    Technical Parameters:

                    Is it specified which model will be used?
                    Are parameters such as temperature, token limits, or other settings defined?
                    User Requirements and Input Formats:

                    Are all user-provided details sufficiently described so that the context, purpose, and tasks are clearly communicated to the agency?
                    Is it clear in what form user inputs will be provided to the agency (prompts, commands, files, etc.)?
                    Missing Information and Next Steps:

                    If information is missing, explicitly identify what is needed (e.g., “A detailed description of the required tools is missing,” or “The agent roles are not clearly defined yet.”)
                    If all requirements are met, confirm that no additional information is necessary.
                    Your Task:
                    Analyze the available information and map it to these criteria. Then provide a precise statement indicating which, if any, additional details need to be requested to form a complete and actionable prompt. If all relevant details are present, state that no further information is required.
                    INFORMATION: """+past_information
                    }
                ]
                },
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": "New information: "+self.information
                    }
                ]
                },
            ],
            response_format={
                "type": "text"
            },
            temperature=0,
            max_tokens=16383,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return response.choices[0].message.content
