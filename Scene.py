from pygame import *
from abc import ABC, abstract method

# Represents a game scene
# Scenes must inherit this class's functions in order to be used to create menus, graphics, logic, etc.

# This class represents a game scene and is abstract

class Scene(ABC):
    # Instantiates a Scene object. Takes in a director object as a parameter.
    @abstractmethod
    def __init__(self, director):
        self.director = director

    # Called by Director and defined on the subclass
    @abstractmethod
    def on_update(self):
        
        raise NotImplementedError("on_update abstract method must be defined in subclass")

    # Called to check for events (inputs)
    @abstractmethod
    def on_event(self, event):
        
        raise NotImplementedError("on_event abstract method must be defined in subclass")

    # Is called when you want to draw on the screen
    @abstractmethod
    def on_draw(self, screen):
        
        raise NotImplementedError("on_Draw abstract method must be defined in subclass")
