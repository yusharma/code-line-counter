from typing import Set

from classifiers.java_line_classifier import JavaLineClassifier
from classifiers.base_line_classifier import LineClassifier
from analyzers.base_analyzer import LanguageAnalyzer

class JavaAnalyzer(LanguageAnalyzer):
    """Analyzer implementation for Java language"""
    
    def _create_classifier(self) -> LineClassifier:
        return JavaLineClassifier()
    
    def get_file_extensions(self) -> Set[str]:
        return {'.java'}