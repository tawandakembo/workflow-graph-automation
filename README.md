# Workflow graph automation

This project uses an agentic worflow to automate the workflow graph construction from Software Requirements Specicications. 
It uses the CrewAI agent framework and OpenAI's GPT4

# Running the product

## Starting the project

```
export SERPER_API_KEY=<YOUR SERPER_API KEY>
export OPENAI_API_KEY <YOUR OPENAI KEY>
git clone git@github.com:tkembo/workflow-graph-automation.git
cd workflow-graph-automation
pip install -r requirements.txt
python main.py
```

##  Upon starting the project
- You will be asked for a problem you would like solved using software. Just enter a one sentence description of what problem the software should solve.
- The project will then generate a SRS, an workflow automatin graph and make an evaluation of the workflow graph.

# Improvements I would have done if I had more more

- instead of generating the SRS from a one line prompt, the system should be improved to use an existing SRS, such as PROMISE Data Repository or GitHub repositories with detailed SRS documents.
- Instead of generating just one set of workflow graphs, we could generate two different sets using two different modules (perhaps GPT-4o and Claude 3 Opous) and then used semantic similarity to evaluate and improve both. Antother approach would be to use an example of an exisitng SRS and the corresponding workflow automation graphs to do some analysis of how well the graphs were created.
- Linting and unit testing
- A better alternative to Mermaid & Markdown for Workflow generation. Draw.io and Visio perhaps.

# Examples,

The examples folder contains an example of documents that were generated using the prompt: ** An app for keeping track of my personal expenses **
