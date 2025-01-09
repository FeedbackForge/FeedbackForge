# FeedbackForge: A Modular Library for User Feedback Loops

**Feedback Forge** is a Python library designed to streamline the development of applications that rely on user feedback loops. It enables developers to track user interactions, system states, and outcomes with precise time management. The library's extensibility allows seamless integration with recommendation algorithms, making it ideal for applications leveraging reinforcement learning, recommender systems, and multi-armed bandits.


 > *Forging Better Feedback, One Loop at a Time.*
  
## Key Features

- **Flexible Contexts**: Define and manage the environment in which interactions occur.
- **Timed States**: Track states and their transitions with precise timing information.
- **Action-Outcome Linking**: Model actions and their outcomes for detailed feedback loops.
- **Extensible Design**: Abstract base classes for customization across different applications.
- **Time Management**: Built-in tools for absolute and relative timestamp handling.
- **Serialization Support**: Convert interactions and their components to dictionaries for easy storage and processing.

### Modular Architecture
- **Abstract Base Classes**: Easily define custom `Context`, `State`, `Action`, and `Outcome` tailored to your application.
- **Interaction Class**: Centralize user feedback loops, linking context, initial state, actions, and outcomes.

### Integration with Recommendation Algorithms
- **State-of-the-Art Ready**: Feedback Forge integrates seamlessly with advanced algorithms in reinforcement learning and recommendation systems, enabling applications to adapt dynamically and optimize user experiences.
- **Customizability**: Developers can connect their systems with multi-armed bandit models, reinforcement learning algorithms, or recommendation engines for tailored user feedback.

### Extensibility
- **Generic**: Suitable for diverse domains, from agriculture and education to healthcare and e-commerce.
- **Scakakve**: Built with scalability and adaptability in mind, allowing developers to plug and play.

## Getting Started

### Installation
Clone the repository:
```bash
git clone https://gitlab.com/your-repo-name/feedback-forge.git
```

Navigate to the project directory and install dependencies:
```bash
cd feedback-forge
pip install -r requirements.txt
```

### Usage
Here is a quick example of how to use Feedback Forge:

#### Groww Application Example
This example simulates a crop monitoring system:

```python
from datetime import datetime, timedelta
from feedback_forge import GrowwContext, GrowwState, GrowwAction, GrowwOutcome
from feedback_forge import StateWithTime, ActionWithTime, OutcomeWithTime, Timestamp, Interaction

# Context setup
groww_context = GrowwContext(region="Europe", user_expertise="Intermediate")

# Initial state with timestamp
initial_state = GrowwState(plant_stage="Seedling", dap=10)
state_timestamp = Timestamp(
    absolute_time=datetime(2025, 1, 5),
    relative_to="planting",
    relative_offset=timedelta(days=10)
)
initial_state_with_time = StateWithTime(initial_state, state_timestamp)

# Action with timestamp
action = GrowwAction(action_type="Watering")
action_timestamp = Timestamp(
    absolute_time=datetime(2025, 1, 6),
    relative_to="planting",
    relative_offset=timedelta(days=11)
)
action_with_time = ActionWithTime(action, action_timestamp)

# Outcome with timestamp
outcome = GrowwOutcome(yield_score=85)
outcome_timestamp = Timestamp(
    absolute_time=datetime(2025, 1, 7),
    relative_to="planting",
    relative_offset=timedelta(days=12)
)
outcome_with_time = OutcomeWithTime(outcome, outcome_timestamp)

# Interaction setup
interaction = Interaction(
    context=groww_context,
    initial_state=initial_state_with_time,
    action=action_with_time
)
interaction.record_outcome(resulting_state=initial_state_with_time, outcome=outcome_with_time)

# Serialize interaction to a dictionary
print(interaction.to_dict())
```

#### Plantix Application Example
For pest management and monitoring:

```python
from datetime import datetime, timedelta
from feedback_forge import PlantixContext, PlantixState, PlantixAction, PlantixOutcome
from feedback_forge import StateWithTime, ActionWithTime, OutcomeWithTime, Timestamp, Interaction

# Context setup
plantix_context = PlantixContext(recent_weather="Rainy")

# Initial state with timestamp
initial_state = PlantixState(pest_detected="Aphids", severity=3)
state_timestamp = Timestamp(
    absolute_time=datetime(2025, 1, 10)
)
initial_state_with_time = StateWithTime(initial_state, state_timestamp)

# Action with timestamp
action = PlantixAction(control_method="Pesticide Spray")
action_timestamp = Timestamp(
    absolute_time=datetime(2025, 1, 11)
)
action_with_time = ActionWithTime(action, action_timestamp)

# Outcome with timestamp
outcome = PlantixOutcome(effectiveness_score=90)
outcome_timestamp = Timestamp(
    absolute_time=datetime(2025, 1, 12)
)
outcome_with_time = OutcomeWithTime(outcome, outcome_timestamp)

# Interaction setup
interaction = Interaction(
    context=plantix_context,
    initial_state=initial_state_with_time,
    action=action_with_time
)
interaction.record_outcome(resulting_state=initial_state_with_time, outcome=outcome_with_time)

# Serialize interaction to a dictionary
print(interaction.to_dict())
```

### Contribution
Contributions are welcome! If you have ideas, feel free to open an issue or submit a pull request.

### License
This project is licensed under the MIT License. See the `LICENSE` file for details.
