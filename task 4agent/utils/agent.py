import google.generativeai as genai
import os
from dotenv import load_dotenv
from agents import Agent, function_tool
from agents.extensions.models.litellm_model import LitellmModel

# configure API
genai.configure(api_key="AIzaSyA6rNJO0xhcTe2hR_dqjxcCk84O84zfEyY")

def generate_summary(text):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Summarize this:\n{text}")
    return response.text

def generate_quiz(text):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Create 5 quiz questions from this text:\n{text}"
    response = model.generate_content(prompt)
    return response.text
