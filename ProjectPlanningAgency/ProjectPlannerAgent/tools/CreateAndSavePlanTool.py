from agency_swarm.tools import BaseTool
from pydantic import Field
import os

class CreateAndSavePlanTool(BaseTool):
    """
    This tool compiles all gathered information and requirements into a coherent project plan.
    It also provides functionality to save this plan in a specified format and location.
    """

    gathered_information: str = Field(
        ..., description="The gathered information and requirements to be compiled into a project plan."
    )
    file_format: str = Field(
        ..., description="The format in which to save the project plan, e.g., 'txt', 'md'."
    )
    file_path: str = Field(
        ..., description="The file path where the project plan should be saved."
    )

    def run(self):
        """
        Compiles the gathered information into a project plan and saves it in the specified format and location.
        Returns a confirmation message with the file path.
        """
        # Compile the project plan
        project_plan = f"Project Plan:\n\n{self.gathered_information}"

        # Determine the file extension based on the specified format
        if self.file_format not in ['txt', 'md']:
            return "Unsupported file format. Please use 'txt' or 'md'."

        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        # Save the project plan to the specified file
        with open(f"{self.file_path}.{self.file_format}", 'w') as file:
            file.write(project_plan)

        return f"Project plan saved successfully at {self.file_path}.{self.file_format}"