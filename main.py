from crewai import Agent, Crew, Task
 # main.py

topic_researcher = Agent(
    role='Topic Researcher',
    goal='Find trending topics for podcasts',
    backstory='Expert in identifying what is currently popular online.'
)

scriptwriter = Agent(
    role='Scriptwriter',
    goal='Write engaging podcast scripts based on topics',
    backstory='Skilled writer with experience in podcast scripting.'
)

voice_synth = Agent(
    role='Voice Synth Agent',
    goal='Convert podcast scripts into audio',
    backstory='Specialist in text-to-speech and audio generation.'
)

topic_task = Task(
    description='Research and list 3 trending topics for podcasts.',
    agent=topic_researcher,
    expected_output='A list of 3 trending podcast topics.'
)

script_task = Task(
    description='Write a podcast script for one of the trending topics.',
    agent=scriptwriter,
    expected_output='A podcast script for one selected topic.'
)

#audio_task = Task(
    #description='Generate audio from the podcast script.',
    #agent=voice_synth,
    #expected_output='Audio file or audio data generated from the script.'
#)

crew = Crew(
    agents=[topic_researcher, scriptwriter, voice_synth],
    tasks=[topic_task, script_task, ]
)

results = crew.kickoff()  # <--- Add this line

print(results)