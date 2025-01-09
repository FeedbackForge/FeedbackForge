from structures import Context, State, Action, Outcome, StateWithTime, ActionWithTime, TimeStamp, Interaction

class PlantixContext(Context):
    def __init__(self, recent_weather: str):
        self.recent_weather = recent_weather
    def to_dict(self) -> Dict[str, Any]:
        return {"recent_weather": self.recent_weather}

class PlantixState(State):
    def __init__(self, pest_detected: str, severity: int):
        self.pest_detected = pest_detected
        self.severity = severity
    def to_dict(self) -> Dict[str, Any]:
        return {"pest_detected": self.pest_detected, "severity": self.severity}

class PlantixAction(Action):
    def __init__(self, control_method: str):
        self.control_method = control_method
    def to_dict(self) -> Dict[str, Any]:
        return {"control_method": self.control_method}

class PlantixOutcome(Outcome):
    def __init__(self, effectiveness_score: int):
        self.effectiveness_score = effectiveness_score
    def to_dict(self) -> Dict[str, Any]:
        return {"effectiveness_score": self.effectiveness_score}


# Example Usage
if __name__ == "__main__":

  plantix_context = PlantixContext(recent_weather="Rainy")
initial_state = PlantixState(pest_detected="Aphids", severity=7)
initial_state_with_time = StateWithTime(
    state=initial_state,
    timestamp=Timestamp(datetime(2025, 2, 1))
)

  action = PlantixAction(control_method="Neem Oil Spray")
  action_with_time = ActionWithTime(
      action=action,
      timestamp=Timestamp(datetime(2025, 2, 2))
  )
  
  resulting_state = PlantixState(pest_detected="None", severity=0)
  resulting_state_with_time = StateWithTime(
      state=resulting_state,
      timestamp=Timestamp(datetime(2025, 2, 5))
  )
  
  outcome = PlantixOutcome(effectiveness_score=95)
  outcome_with_time = OutcomeWithTime(
      outcome=outcome,
      timestamp=Timestamp(datetime(2025, 2, 5))
  )
  
  interaction = Interaction(
      context=plantix_context,
      initial_state=initial_state_with_time,
      action=action_with_time
  )
  interaction.record_outcome(resulting_state_with_time, outcome_with_time)
  
  print(interaction.to_dict())
