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
            self.information = self._shared_state.get("information")+"\n"+self.information
            self._shared_state.set("information", self.information)
        else:        
            self._shared_state.set("information", self.information)
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                "role": "system",
                "content": [
                    {
                    "type": "text",
                    "text": "Your job is to plan a project. You will get 'information' the user already provided. Your job is to tell, which information is missing to to create a plan for the project. INFORMATION: "+self._shared_state.get("information")
                    }
                ]
                },
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": self.information
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

        return response.choices[0].message