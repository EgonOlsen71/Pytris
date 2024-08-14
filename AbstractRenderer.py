from abc import ABC, abstractmethod
#   "Interface" for a renderer. A renderer takes a block and
#   renders it the way it seems fitting.
#   @author EgonOlsen71
#
class AbstractRenderer(ABC):

    @abstractmethod
    def render(self, block):
        pass

    @abstractmethod
    def derender(self, block):
        pass