from crewai import Crew, Process

from tasks import Tasks
from agents import Agents

requirement_analyst = Agents().requirement_analyst()
technical_writer = Agents().technical_writer()
workflow_automation_engineer = Agents().workflow_automation_engineer()
performance_evaluator= Agents().performance_evaluator()

user_problem = input("What problem should your app solve:\n")

gather_requirements_task = Tasks().gather_requirements_task(requirement_analyst, user_problem)
document_srs_task = Tasks().document_srs_task(technical_writer, user_problem)
generate_workflow_graphs_task = Tasks().generate_workflow_graphs_task(workflow_automation_engineer, user_problem)
evaluate_system_performance_task = Tasks().evaluate_system_performance_task(performance_evaluator, user_problem)

# Forming the SRS creation crew
srs_creation_crew = Crew(
    agents=[requirement_analyst, technical_writer, workflow_automation_engineer, performance_evaluator],
    tasks=[
        gather_requirements_task, 
        document_srs_task,
        generate_workflow_graphs_task,
        evaluate_system_performance_task
    ],
    process=Process.sequential
)

# Kickoff the crew with the user-provided description

result = srs_creation_crew.kickoff(inputs={'description': user_problem})
print(result)
