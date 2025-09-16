from abc import ABC, abstractmethod

class LineClassifier(ABC):
    """Interface for line classification. Extend by creating new classifiers"""
    
    @abstractmethod
    def is_blank(self, line: str) -> bool:
        """Check if line is blank"""
        pass
    
    @abstractmethod
    def is_comment(self, line: str) -> bool:
        """Check if line is a comment without any code"""
        pass
    
    @abstractmethod
    def has_code(self, line: str) -> bool:
        """Check if line contains code"""
        pass
