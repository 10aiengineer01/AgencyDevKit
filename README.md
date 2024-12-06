# Agency Swarm Setup Workflow with Cursor

This repository contains a Python script designed to streamline the setup process for creating and managing agencies using the Agency Swarm framework. It integrates with the Cursor environment to minimize the amount of manual programming required, allowing you to focus on high-level planning and development.

## What Does This Script Do?

### Dependency Management:
- Checks and installs required packages (`agency-swarm`, `openai`, `python-dotenv`), ensuring a smooth start without manual intervention.

### Virtual Environment Setup:
- Creates a Python virtual environment (`env`) and installs all dependencies inside it, isolating project libraries from your system environment.

### Configuration Files Creation:
- Generates essential configuration files:
  - `requirements.txt` containing the list of dependencies.
  - `.composer` providing guidance and best practices for using Agency Swarm and defining agents, tools, and agencies.
  - `.gitignore` to exclude `.composer` from version control.
- It will also prompt you for your OpenAI API key and store it in a `.env` file if not already present.

### Composer Prompt Generation:
- Prompts you for a description of your project, then generates a `composer_prompt.md` file. This file gives a detailed development plan and specification, helping you use Cursor or other tools to accelerate agency development.

### Self-Deletion:
- Once setup is complete, the script deletes itself, leaving your project directory clean and ready for action.

## Why This Matters
Working with Agency Swarm can involve multiple steps—defining agents, building tools, and structuring the agency. By leveraging this script, you significantly reduce the amount of manual coding. Combined with Cursor, you can iterate faster on your agency’s design and implementation.

## Prerequisites
- **Python 3.9+:** Ensure you have a recent version of Python.
- **Git:** For cloning this repository.
- **OpenAI API Key:** Obtain one from the OpenAI Dashboard.

## Getting Started

### Clone the Repository:
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### Run the Setup Script:
```bash
python run.py
```
- This will:
  - Check and install necessary dependencies.
  - Create and populate a virtual environment.
  - Prompt for your OpenAI API key (if needed).
  - Ask for a project description to generate the `composer_prompt.md`.
  - Remove the script after completion.

### Activate the Virtual Environment (If Needed):

On Windows:
```bash
env\Scripts\activate
```

On macOS/Linux:
```bash
source env/bin/activate
```

You now have a `requirements.txt`, `.composer`, `.gitignore`, and `composer_prompt.md` set up. You can use these files as reference points to develop your agency with Agency Swarm, aided by Cursor to reduce coding overhead.

## Next Steps
- Review `composer_prompt.md` for a detailed roadmap of your project.
- Follow the instructions in `.composer` to structure your agents, tools, and agency.
- Use Cursor or other AI-driven development tools to speed up coding tasks.

## Troubleshooting
- If dependencies fail to install automatically, run:
  ```bash
  pip install agency-swarm openai python-dotenv
  ```
- Ensure you have the necessary permissions to create and delete files.
- If the script fails to delete itself, you can remove it manually.

## Contributing
Feedback and improvements are welcome! Submit issues or pull requests to help enhance this workflow.

## License
This project is licensed under the MIT License.