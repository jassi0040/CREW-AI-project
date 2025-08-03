# crew_runner.py
from crewai import Crew
from agents import get_topic_researcher, get_scriptwriter, get_voice_synth
from tasks import tasks

# Initialize agents
agents = [get_topic_researcher(), get_scriptwriter(), get_voice_synth()]

# Create Crew workflow
crew = Crew(
    agents=agents,
    tasks=tasks
)

def run_crew():
    results = crew.run()
    print('--- Podcast Generation Results ---')
    for result in results:
        print(result)

if __name__ == '__main__':
    run_crew()
