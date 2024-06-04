from crewai import Agent
from crewai_tools.tools import WebsiteSearchTool, SerperDevTool, FileReadTool

web_search_tool = WebsiteSearchTool()
seper_dev_tool = SerperDevTool()

class Agents():
    # Creating a requirement analyst agent
    def requirement_analyst(self):
        return Agent(
            role='Requirement Analyst',
            goal='Gather and analyze software requirements based on user description.',
            verbose=True,
            memory=True,
            backstory=(
                "You are a detail-oriented analyst with a knack for understanding user needs "
                "and translating them into technical requirements."
            ),
            tools=[web_search_tool, seper_dev_tool],
            allow_delegation=False
        )

    # Creating a technical writer agent
    def technical_writer(self):
        return Agent(
            role='Technical Writer',
            goal='Document the gathered requirements into a structured SRS markdown file.',
            verbose=True,
            memory=True,
            backstory=(
                "You have a strong background in technical writing, capable of creating clear and comprehensive documentation."
            ),
            tools=[
                FileReadTool(
                    file_path='reference/software_requirements_specification_example.md',
                    description='A tool to read the software requirements specification example file.'
                ),
                FileReadTool(
                    file_path='output/technical_requirements.md',
                    description='The requirements .'
                )
            ],
            allow_delegation=False
        )
    
    # Creating a workflow automation engineer agent
    def workflow_automation_engineer(self):
        return Agent(
            role='Workflow Automation Engineer',
            goal='Generate workflow diagrams or flowcharts based on the SRS.',
            verbose=True,
            memory=True,
            backstory=(
                "You specialize in creating visual representations of complex systems and processes."
            ),
            tools=[
                FileReadTool(
                    file_path='output/software_requirements_specification.md',
                    description='The SRS document.'
                ),
                web_search_tool,
                seper_dev_tool
            ],
            allow_delegation=False
        )
    
    # Creating a performance evaluator agent
    def performance_evaluator(self):
        return Agent(
            role='Performance Evaluator',
            goal='Evaluate the system performance requirements and provide optimization recommendations.',
            verbose=True,
            memory=True,
            backstory=(
                "You have expertise in evaluating system performance and optimizing software applications."
            ),
            tools=[
                FileReadTool(
                    file_path='output/software_requirements_specification.md',
                    description='The SRS document.'
                ),
                FileReadTool(
                    file_path='output/technical_requirements.md',
                    description='The technical requirements.'
                ),
                FileReadTool(
                    file_path='output/workflow_automation_graphs.md',
                    description='The workflow graphs.'
                ),
                web_search_tool,
                seper_dev_tool
            ],
            allow_delegation=False
        )
