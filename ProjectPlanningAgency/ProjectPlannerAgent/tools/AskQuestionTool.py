from agency_swarm.tools import BaseTool
from pydantic import Field

class AskQuestionTool(BaseTool):
    """
    This tool facilitates the gathering of additional information by allowing the agent to pose questions
    to stakeholders or other agents. It records the questions and the responses received.
    """

    question: str = Field(
        ..., description="The question to be posed to stakeholders or other agents."
    )

    def run(self):
        """
        Records the question and the response received. Returns a log of the interaction.
        """
        print(self.question)
        result = input("👤User: ")

        return result
