# NotesAgent

NotesAgent is an autonomous agent designed to help you generate, correct, and write notes on any topic. Powered by [CrewAI](https://docs.crewai.com/), it leverages a multi-agent architecture and integrates knowledge from all PDF files in the `knowledge` directory to provide intelligent, context-aware note-taking assistance.

## How It Works (Agent Mode)

- **Autonomous Workflow:**
	- The agent interacts with you to receive a topic.
	- It uses specialized sub-agents for generating, correcting, and writing notes.
	- All agents share access to a knowledge base built from your PDF files.

- **Knowledge Integration:**
	- Every PDF in the `knowledge` folder is automatically included as a knowledge source.
	- The agent can reference and synthesize information from these documents to enhance your notes.

- **Extensible Agent Crew:**
	- The system is built on CrewAI's agent/task/crew abstractions, making it easy to add new agents or tasks for more advanced workflows.

## Project Structure

```
NotesAgent/
│
├── knowledge/                      # Place your PDF files here
│
├── notes_agent_flow/
│   └── src/
│       └── notes_agent_flow/
│           ├── main.py             # Entry point: launches the agent
│           └── crews/
│               └── notes_crew/
│                   ├── notes_crew.py   # Crew and agent definitions
│                   └── knowledge/      # (symlink or copy of root knowledge folder)
│
├── config/
│   ├── agents.yaml                 # Agent configuration (YAML)
│   └── tasks.yaml                  # Task configuration (YAML)
│
├── .env                            # Environment variables (optional)
└── README.md
```

## Getting Started

1. **Install dependencies**  
	 Make sure you have Python 3.8+ and install requirements:
	 ```bash
	 pip install -r requirements.txt
	 ```

2. **Add Knowledge**  
	 Place your PDF files in the `knowledge/` directory at the project root.

3. **Configure Agents and Tasks**  
	 Edit `config/agents.yaml` and `config/tasks.yaml` as needed.

4. **Run the Agent**
	 ```bash
	 python notes_agent_flow/src/notes_agent_flow/main.py
	 ```

5. **Interact**  
	 The agent will prompt you for a topic and autonomously generate, correct, and write notes using its knowledge base.

## Customization

- **Knowledge Source:**  
	By default, all PDFs in the `knowledge` folder are used. To change this, modify the `knowledge_path` in `notes_crew.py`.

- **Agents & Tasks:**  
	You can add or modify agents and tasks by editing the YAML files in the `config/` directory.

## Requirements

- Python 3.8+
- [CrewAI](https://docs.crewai.com/)
- [pydantic](https://docs.pydantic.dev/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [crewai_tools](https://pypi.org/project/crewai-tools/)

## License

MIT License

---

*Built as an autonomous agent with [CrewAI](https://docs.crewai.com/)*