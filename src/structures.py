# Flexible Library Prototype with Time Management Enhancements

## Core Definitions

from typing import Any, Dict, List, Optional, Tuple, Callable
from datetime import datetime, timedelta
from abc import ABC, abstractmethod



class Timestamp:
    """
    Represents a point in time, with both absolute and relative times.
    """
    def __init__(
        self, 
        absolute_time: datetime, 
        relative_to: Optional[str] = None, 
        relative_offset: Optional[timedelta] = None
    ):
        """
        :param absolute_time: The absolute time (e.g., a specific datetime).
        :param relative_to: The name of the reference event (e.g., "planting").
        :param relative_offset: The time offset relative to the event (e.g., days after planting).
        """
        self.absolute_time = absolute_time
        self.relative_to = relative_to
        self.relative_offset = relative_offset

    def to_dict(self) -> dict:
        return {
            "absolute_time": self.absolute_time.isoformat(),
            "relative_to": self.relative_to,
            "relative_offset_days": self.relative_offset.days if self.relative_offset else None,
        }
    
    def __repr__(self):
        return f"Timestamp(absolute={self.absolute_time}, relative_to={self.relative_to}, offset={self.relative_offset})"


class Context(ABC):
    """Abstract base class for a context."""
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Serialize context to a dictionary."""
        pass

class State(ABC):
    """Abstract base class for a state."""
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Serialize state to a dictionary."""
        pass

class Action(ABC):
    """Abstract base class for an action."""
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Serialize action to a dictionary."""
        pass

class Outcome(ABC):
    """Abstract base class for an outcome."""
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Serialize outcome to a dictionary."""
        pass


class ActionWithTime(Action):
    def __init__(self, action: Action, timestamp: Timestamp):
        self.action = action
        self.timestamp = timestamp
    
    def to_dict(self) -> dict:
        return {
            "action": self.action.to_dict(),
            "timestamp": self.timestamp.to_dict(),
        }

class OutcomeWithTime(Outcome):
    def __init__(self, outcome: Outcome, timestamp: Timestamp):
        self.outcome = outcome
        self.timestamp = timestamp
    
    def to_dict(self) -> dict:
        return {
            "outcome": self.outcome.to_dict(),
            "timestamp": self.timestamp.to_dict(),
        }

class StateWithTime(State):
    def __init__(self, state: State, timestamp: Timestamp):
        self.state = state
        self.timestamp = timestamp
    
    def to_dict(self) -> dict:
        return {
            "state": self.state.to_dict(),
            "timestamp": self.timestamp.to_dict(),
        }



## Core Classes

class Interaction:
    """Represents an interaction of a user with the system."""
    def __init__(
        self,
        context: Context,
        initial_state: StateWithTime,
        action: ActionWithTime,
        resulting_state: Optional[StateWithTime] = None,
        outcome: Optional[OutcomeWithTime] = None,
    ):
        self.context = context
        self.initial_state = initial_state
        self.action = action
        self.resulting_state = resulting_state
        self.outcome = outcome

    def record_outcome(self, resulting_state: StateWithTime, outcome: OutcomeWithTime):
        """Record the outcome and resulting state of an interaction."""
        self.resulting_state = resulting_state
        self.outcome = outcome

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the interaction to a dictionary."""
        return {
            "context": self.context.to_dict(),
            "initial_state": self.initial_state.to_dict(),
            "action": self.action.to_dict(),
            "resulting_state": self.resulting_state.to_dict() if self.resulting_state else None,
            "outcome": self.outcome.to_dict() if self.outcome else None,
        }
