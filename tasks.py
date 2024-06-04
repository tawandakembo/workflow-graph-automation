from crewai import Task
from textwrap import dedent

class Tasks():

    # Task for gathering requirements
    def gather_requirements_task(self, requirement_analyst, user_problem):
        return Task(
            description=dedent(f"""\
                Generate detailed requirements for an app that solves the problem: {user_problem}. 
                Consider functional requirements, non-functional requirements, and any constraints or assumptions.
                Your final output should be a detailed list of requirements.
                """
            ),
            expected_output=dedent(f"""\
                A detailed list of software requirements to solve {user_problem}.',
                agent=requirement_analyst,
                """
            ),
            agent=requirement_analyst,
            output_file='output/technical_requirements.md'
        )

    # Task for documenting SRS
    def document_srs_task(self, technical_writer, user_problem):
        return Task(
            description=dedent(f"""\
                Based on the gathered requirements, create a comprehensive Software Requirements Specification (SRS) document to solve the problem: {user_problem}. 
                The document should be structured and formatted as a markdown file, including sections for Introduction,
                Overall Description, Functional Requirements, Non-functional Requirements, and any other relevant sections. 
                """
            ),
            expected_output='A structured SRS document in markdown format.',
            agent=technical_writer,
            output_file='output/software_requirements_specification.md'
        )

    # Task for generating workflow graphs
    def generate_workflow_graphs_task(self, workflow_automation_engineer, user_problem):
        return Task(
            description=dedent(f"""\
                Create workflow diagrams or flowcharts to visualize the app's functionality and user interactions for the problem: {user_problem} from the software requirements specification (SRS).
                Consider different user scenarios and system components to create detailed and informative diagrams.
                The graphs should visualize the workflows and processes described in the SRS.
                Use Mermaid to generate the workflow automation diagrams and save them in a markdown file.
                """
            ),
            expected_output='Workflow diagrams or flowcharts illustrating the app functionality and user interactions in markdown format.',
            agent=workflow_automation_engineer,
            output_file='output/workflow_automation_graphs.md'
        )
    
    # Task for evaluating system performance
    def evaluate_system_performance_task(self, performance_evaluator, user_problem):
        return Task(
            description=dedent(f"""\
                Evaluate the system performance requirements for the app that solves the problem: {user_problem}. 
                Consider factors like response time, throughput, resource utilization, and scalability.
                Provide recommendations for optimizing the system performance based on the requirements and constraints.
                Research relevant Smart Evaluation Techniques and save the results in a markdown file.
                """
            ),
            expected_output='A performance evaluation report with recommendations for optimizing system performance.',
            agent=performance_evaluator,
            output_file='output/performance_evaluation_report.md'
        )