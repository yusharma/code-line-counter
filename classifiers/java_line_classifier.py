from classifiers.base_line_classifier import LineClassifier

class JavaLineClassifier(LineClassifier):
    """Classifier for Java language"""
    
    def is_blank(self, line: str) -> bool:
        return len(line.strip()) == 0
    
    def is_comment(self, line: str) -> bool:
        stripped = line.strip()
        
        # TODO: Support for only single-line comment for now,
        # could be extended for multiple-line comments
        return stripped.startswith('//')
    
    def has_code(self, line: str) -> bool:
        # TODO: This method could be updated for supporting more granular breakup
        if self.is_blank(line) or self.is_comment(line):
            return False
        return True
