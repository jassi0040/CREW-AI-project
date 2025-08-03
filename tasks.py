# tasks.py
from crewai import Task
from agents import get_topic_researcher, get_scriptwriter, get_voice_synth

# Define tasks for each agent
topic_task = Task(
    description='Research and list 3 trending topics for podcasts.',
    agent=get_topic_researcher()
)

script_task = Task(
    description='Write a podcast script for one of the trending topics.',
    agent=get_scriptwriter()
)

audio_task = Task(
    description='Generate audio from the podcast script.',
    agent=get_voice_synth()
)

tasks = [topic_task, script_task, audio_task]
