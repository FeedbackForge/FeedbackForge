from structures import Context, State, Action, Outcome, StateWithTime, ActionWithTime, TimeStamp, Interaction


class GrowwContext(Context):
    def __init__(self, region: str, user_expertise: str):
        self.region = region
        self.user_expertise = user_expertise
    def to_dict(self) -> Dict[str, Any]:
        return {"region": self.region, "user_expertise": self.user_expertise}

class GrowwState(State):
    def __init__(self, plant_stage: str, dap: int):
        self.plant_stage = plant_stage
        self.dap = dap
    def to_dict(self) -> Dict[str, Any]:
        return {"plant_stage": self.plant_stage, "dap": self.dap}

class GrowwAction(Action):
    def __init__(self, action_type: str):
        self.action_type = action_type
    def to_dict(self) -> Dict[str, Any]:
        return {"action_type": self.action_type}

class GrowwOutcome(Outcome):
    def __init__(self, yield_score: int):
        self.yield_score = yield_score
    def to_dict(self) -> Dict[str, Any]:
        return {"yield_score": self.yield_score}


# Example Usage
if __name__ == "__main__":

  from datetime import datetime, timedelta

  groww_context = GrowwContext(region="Europe", user_expertise="Intermediate")
  initial_state = GrowwState(plant_stage="Seedling", dap=10)
  initial_state_with_time = StateWithTime(
      state=initial_state,
      timestamp=Timestamp(datetime(2025, 1, 5), relative_to="planting", relative_offset=timedelta(days=10))
  )
  
  action = GrowwAction(action_type="Watering")
  action_with_time = ActionWithTime(
      action=action,
      timestamp=Timestamp(datetime(2025, 1, 6), relative_to="planting", relative_offset=timedelta(days=11))
  )
  
  resulting_state = GrowwState(plant_stage="Vegetative", dap=15)
  resulting_state_with_time = StateWithTime(
      state=resulting_state,
      timestamp=Timestamp(datetime(2025, 1, 10), relative_to="planting", relative_offset=timedelta(days=15))
  )
  
  outcome = GrowwOutcome(yield_score=80)
  outcome_with_time = OutcomeWithTime(
      outcome=outcome,
      timestamp=Timestamp(datetime(2025, 1, 10))
  )
  
  interaction = Interaction(
      context=groww_context,
      initial_state=initial_state_with_time,
      action=action_with_time
  )
  interaction.record_outcome(resulting_state_with_time, outcome_with_time)
  
  print(interaction.to_dict())
