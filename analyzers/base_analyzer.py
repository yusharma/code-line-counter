from abc import ABC, abstractmethod
from typing import Set
from pathlib import Path

from classifiers.base_line_classifier import LineClassifier
from models.line_stats import LineStats

class LanguageAnalyzer(ABC):
    """Interface of language analysis algorithm"""
    
    def __init__(self):
        self.classifier = self._create_classifier()
        self.stats = LineStats()
    
    @abstractmethod
    def _create_classifier(self) -> LineClassifier:
        """Factory method for creating language-specific classifier"""
        pass
    
    @abstractmethod
    def get_file_extensions(self) -> Set[str]:
        """Return supported file extensions"""
        pass
    
    def analyze_file(self, file_path: Path) -> LineStats:
        """Method defines the analysis workflow"""
        self.stats = LineStats()
        
        try:
            # Read the file
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            # Iterate over each line and classify
            for line in lines:
                self._classify_line(line.rstrip('\n\r'))
                
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")
            
        return self.stats
    
    def _classify_line(self, line: str):
        """Classify a single line"""
        self.stats.total += 1
        
        if self.classifier.is_blank(line):
            self.stats.blank += 1
        elif self.classifier.is_comment(line):
            self.stats.comments += 1
        elif self.classifier.has_code(line):
            self.stats.code += 1