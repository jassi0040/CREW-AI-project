# agents.py
from crewai import Agent

# Topic Researcher Agent
def get_topic_researcher():
    return Agent(
        role='Topic Researcher',
        goal='Find trending topics for podcasts',
        backstory='Expert in identifying what is currently popular online.',
        tools=['web_search']
    )

# Scriptwriter Agent
def get_scriptwriter():
    script = Agent(
        role='Scriptwriter',
        goal='Write engaging podcast scripts based on topics',
        backstory='Skilled writer with experience in podcast scripting.'
    )
    print(script)  # Add this line to print the script
    return script

# Voice Synth Agent
#def get_voice_synth():
    return Agent(
        role='Voice Synth Agent',
        goal='Convert podcast scripts into audio',
        backstory='Specialist in text-to-speech and audio generation.'
    )
