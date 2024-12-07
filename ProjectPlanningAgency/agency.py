from ProjectPlanningAgency.ProjectPlannerAgent import ProjectPlannerAgent
from agency_swarm import Agency, set_openai_key

class create_initiall_prompt:

    def __init__(self) -> None:
        self.project_planner_agent = ProjectPlannerAgent()

        self.agency = Agency([self.project_planner_agent],
                        shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                        temperature=0.3,  # default temperature for all agents
                        )

    def run(self, prompt: str, key: str) -> str:
        set_openai_key(key)
        return self.agency.get_completion(prompt)
