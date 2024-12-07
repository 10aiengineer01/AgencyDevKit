from agency_swarm.tools import BaseTool
from pydantic import Field
import os

class CreateAndSavePlanTool(BaseTool):
    """
    This tool compiles all gathered information and requirements into a coherent project plan.
    It also provides functionality to save this plan in a specified format and location.
    """

    goal: str = Field(
        ..., description="The overall goal, what the user wants to develop"
    )

    def run(self):
        """
        Compiles the gathered information into a project plan and saves it
        Returns a confirmation message.
        """

        if self._shared_state.get("information", None) is not None:

            return "Plan was created and save successfully!"
        else:
            return "Please make shure, that all information are aquired bevore using this tool"
