#!/usr/bin/env python
from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from crews.notes_crew.notes_crew import NotesCrew


class NotesState(BaseModel):
    notes: str = ""


class NotesAgentFlow(Flow[NotesState]):

    @start()
    def create_notes(self):
        print("Generating notes...")
        crew = NotesCrew()
        user_input = input("What topic do you want to take notes on? ")
        inputs = {
            "topic" : user_input,
        }
        notes = crew.crew().kickoff(inputs=inputs)
        self.state.notes = notes
        print("Notes generated.")


def kickoff():
    notes_agent_flow = NotesAgentFlow()
    notes_agent_flow.kickoff()


def plot():
    notes_agent_flow = NotesAgentFlow()
    notes_agent_flow.plot()


if __name__ == "__main__":
    kickoff()
