from typing import Optional, Dict
from pathlib import Path

from factory.analyzer_factory import AnalyzerFactory
from models.line_stats import LineStats

class App:
    """Main application class. Orchestrate the counting process"""
    
    def __init__(self):
        self.factory = AnalyzerFactory()
    
    def count_file_lines(self, file_path: str) -> Optional[LineStats]:
        """Count lines in a single file"""
        path = Path(file_path)
        
        if not path.exists():
            print(f"Error: File {file_path} does not exist")
            return None
        
        analyzer = self.factory.get_analyzer(path)
        if not analyzer:
            print(f"Error: No analyzer available for {path.suffix} files")
            return None
        
        return analyzer.analyze_file(path)
    
    def count_directory_file_lines(self, directory_path: str) -> Dict[str, LineStats]:
        """Count lines in all supported files in directory"""
        results = {}
        path = Path(directory_path)
        
        if not path.is_dir():
            print(f"Error: {directory_path} is not a directory")
            return results
        
        for file_path in path.rglob('*'):
            if file_path.is_file():
                analyzer = self.factory.get_analyzer(file_path)
                if analyzer:
                    stats = analyzer.analyze_file(file_path)
                    results[str(file_path)] = stats
        
        return results