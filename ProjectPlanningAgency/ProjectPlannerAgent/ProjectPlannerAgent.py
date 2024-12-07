from agency_swarm.agents import Agent


class ProjectPlannerAgent(Agent):
    def __init__(self):
        super().__init__(
            name="ProjectPlannerAgent",
            description="This agent is responsible for managing the entire project planning process from collecting ideas to finalizing the project plan.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
        )
        
    def response_validator(self, message):
        return message
