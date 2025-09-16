from typing import Set

from analyzers.base_analyzer import LanguageAnalyzer
from classifiers.base_line_classifier import LineClassifier
from classifiers.python_line_classifier import PythonLineClassifier

class PythonAnalyzer(LanguageAnalyzer):
    """Analyzer implementation for Python language"""
    
    def _create_classifier(self) -> LineClassifier:
        return PythonLineClassifier()
    
    def get_file_extensions(self) -> Set[str]:
        return {'.py'}