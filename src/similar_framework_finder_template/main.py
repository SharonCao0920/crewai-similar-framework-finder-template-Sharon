#!/usr/bin/env python
import sys
import os
from dotenv import load_dotenv
from crew import SimilarFrameworkFinderTemplateCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information.

# Load environment variables from .env file
load_dotenv()

# Fetch API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OTHER_API_KEY = os.getenv("SERPER_API_KEY")  # Replace with other API names as needed

# Check if essential API keys are set
if not OPENAI_API_KEY:
    raise EnvironmentError("OPENAI_API_KEY is not set in the .env file.")
if not OTHER_API_KEY:
    raise EnvironmentError("OTHER_API_KEY is not set in the .env file.")

def run():
    """
    Run the crew.
    """
    inputs = {
        "target_platform": "PaycheckManager.com",
        "pain_points": "Payroll management, tax compliance, and affordability for small businesses",
    }

    SimilarFrameworkFinderTemplateCrew().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "Payroll management and tax compliance solutions"}
    try:
        SimilarFrameworkFinderTemplateCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SimilarFrameworkFinderTemplateCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and return the results.
    """
    inputs = {"topic": "Payroll management and tax compliance solutions"}
    try:
        SimilarFrameworkFinderTemplateCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

run()
