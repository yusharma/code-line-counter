from typing import List, Optional
from pathlib import Path

from analyzers.base_analyzer import LanguageAnalyzer
from analyzers.java_analyzer import JavaAnalyzer
from analyzers.python_analyzer import PythonAnalyzer

class AnalyzerFactory:
    """Get appropriate analyzer based on file type.
    Add new analyzers without modifying factory logic"""
    
    def __init__(self):
        self._analyzers: List[LanguageAnalyzer] = []
        self._register_default_analyzers()
    
    def _register_default_analyzers(self):
        """Register built-in analyzers"""
        self.register(JavaAnalyzer())
        self.register(PythonAnalyzer())
    
    def register(self, analyzer: LanguageAnalyzer):
        """Register a new language analyzer (plugin system)"""
        self._analyzers.append(analyzer)
    
    def get_analyzer(self, file_path: Path) -> Optional[LanguageAnalyzer]:
        """Get appropriate analyzer for file"""
        file_ext = file_path.suffix.lower()
        
        for analyzer in self._analyzers:
            if file_ext in analyzer.get_file_extensions():
                return analyzer
        
        return None