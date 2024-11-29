class SentimentAnalysisResponse:
    """Class to represent a single sentiment analysis response."""
    
    def __init__(self, label: str, score: float):
        self.label = label
        self.score = score

    @classmethod
    def from_dict(cls, data: dict):
        """Create an instance from a dictionary."""
        return cls(label=data.get("label"), score=data.get("score"))

class SentimentAnalysisResponses:
    """Class to handle multiple `sentiment analysis` responses."""
    
    def __init__(self, responses: list):
        self.responses = [SentimentAnalysisResponse.from_dict(item) for item in responses]
        
        
        self.negative = self.get_sentiment_score("negative")
        self.neutral = self.get_sentiment_score("neutral")
        self.positive = self.get_sentiment_score("positive")

    def get_sentiment_score(self, sentiment_label: str):
        """Get the score for a specific sentiment label."""
        for resp in self.responses:
            if resp.label == sentiment_label:
                return resp.score
        return 0  

    def __str__(self):
        return "\n".join(f"Label: {resp.label}, Score: {resp.score}" for resp in self.responses)