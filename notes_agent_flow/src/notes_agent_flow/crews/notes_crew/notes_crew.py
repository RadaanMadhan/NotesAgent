from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
from crewai_tools import FileWriterTool
from dotenv import load_dotenv
import os
import glob


load_dotenv()

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class NotesCrew:
    """Notes Crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    knowledge_path = "knowledge"

    pdf_files = glob.glob(os.path.join(knowledge_path, "*.pdf"))
    pdf_filenames = [os.path.basename(f) for f in pdf_files]

    pdf_source = PDFKnowledgeSource(
        file_paths= pdf_filenames
    )


    @agent
    def notes_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["notes_agent"],
            knowledge_sources=[self.pdf_source],
        )
    
    @agent
    def notes_correction_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["notes_correction_agent"],
        )
    
    @agent
    def notes_write_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["notes_write_agent"],
            tools=[FileWriterTool()],
        )

    @task
    def notes_task(self) -> Task:
        return Task(
            config=self.tasks_config["notes_task"],
        )
    
    @task
    def notes_correction_task(self) -> Task:
        return Task(
            config=self.tasks_config["notes_correction_task"],
        )

    @task
    def notes_write_task(self) -> Task:
        return Task(
            config=self.tasks_config["notes_write_task"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
