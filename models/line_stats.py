class LineStats:
    """Data model for line stats"""
    blank: int = 0
    comments: int = 0
    code: int = 0
    total: int = 0
    
    def __str__(self):
        return str({
            "blank": self.blank,
            "comments": self.comments,
            "code": self.code,
            "total": self.total
        })