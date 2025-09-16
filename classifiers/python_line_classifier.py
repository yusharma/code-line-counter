from classifiers.base_line_classifier import LineClassifier

class PythonLineClassifier(LineClassifier):
    """Classifier for Python language"""
    
    def is_blank(self, line: str) -> bool:
        return len(line.strip()) == 0
    
    def is_comment(self, line: str) -> bool:
        stripped = line.strip()
        return stripped.startswith('#')
    
    def has_code(self, line: str) -> bool:
        if self.is_blank(line) or self.is_comment(line):
            return False
        return True