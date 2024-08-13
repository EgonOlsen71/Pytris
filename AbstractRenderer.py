from abc import ABC, abstractmethod

#   @author EgonOlsen71
#
class AbstractRenderer(ABC):

    @abstractmethod
    def render(self, block):
        pass

    @abstractmethod
    def derender(self, block):
        pass