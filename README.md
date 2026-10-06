# Adaptive Learning Assistant

## Project Overview

The Adaptive Learning Assistant is a Python and Streamlit application
developed to demonstrate an adaptive user interface in the context of
human-computer interaction (HCI).

The application monitors a user's performance while completing a short
learning assessment and adapts the level of assistance provided based on
the user's results.

The purpose of the project is to demonstrate how an interface can change
during runtime based on user interactions and performance.

## Features

- Interactive five-question learning assessment
- Real-time performance tracking
- Adaptive learning levels
- Beginner, Intermediate, and Advanced modes
- Adaptive hints and explanations
- Personalized learning recommendations
- Progress tracking
- Final learning assessment
- Restart learning session functionality

## Adaptive User Interface

The application uses the user's current assessment performance to determine
the appropriate level of assistance.

### Beginner Mode

Score below 50%.

The application provides:
- Detailed explanations
- Additional learning support
- More detailed hints
- Beginner-level recommendations

### Intermediate Mode

Score between 50% and 79%.

The application provides:
- Moderate learning assistance
- Standard explanations
- Moderate-level learning recommendations

### Advanced Mode

Score of 80% or higher.

The application provides:
- Reduced assistance
- Less detailed feedback
- Advanced learning recommendations
- More challenging learning activities

This demonstrates adaptive HCI because the application's behavior changes
during runtime according to the user's interactions and performance.

## Technologies Used

- Python
- Streamlit
- Visual Studio Code
- Git
- GitHub

## Project Structure

AI-Adaptive-Learning-Assistant/

- app.py
- adaptive_engine.py
- requirements.txt
- README.md
- screenshots/
  - initial-state.png
  - beginner-mode.png
  - intermediate-mode.png
  - advanced-mode.png
  - final-results.png

## Installation

1. Download or clone the repository.

2. Open the project directory.

3. Install the required dependency:

   pip install -r requirements.txt

4. Run the application:

   streamlit run app.py

5. Open the local Streamlit URL in a web browser.

## How the Adaptive Logic Works

The application tracks the number of questions answered correctly and
calculates the user's current performance percentage.

The adaptive engine categorizes performance into three levels:

- Below 50% = Beginner
- 50% to 79% = Intermediate
- 80% to 100% = Advanced

The interface then modifies the amount of assistance, explanations,
feedback, and learning recommendations displayed to the user.

## Testing

The application was tested by intentionally creating different performance
levels.

During testing, the system successfully transitioned through:

Beginner -> Intermediate -> Advanced

This demonstrated that the interface responds dynamically to changes in
user performance.

## AI Assistance Disclosure

OpenAI's ChatGPT was used during the development of this project to assist
with brainstorming, code development, debugging, documentation, and
explanations related to adaptive user interfaces and human-computer
interaction.

AI-generated suggestions were reviewed and tested before being incorporated
into the final project.

## Author

Keerthi Nami Reddy