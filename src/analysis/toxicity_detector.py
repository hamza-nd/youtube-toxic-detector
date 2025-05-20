from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from config.config import BERT_MODEL_NAME, TOXICITY_THRESHOLD
from src.utils.db_handler import get_collection, update_document

class ToxicityDetector:
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.tokenizer = AutoTokenizer.from_pretrained(BERT_MODEL_NAME)
        self.model = AutoModelForSequenceClassification.from_pretrained(BERT_MODEL_NAME)
        self.model.to(self.device)
        self.comments_collection = get_collection('comments')

    def predict_toxicity(self, text):
        """
        Predict toxicity score for a given text
        
        Args:
            text (str): Text to analyze
            
        Returns:
            float: Toxicity score between 0 and 1
        """
        # Prepare input
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        
        # Get prediction
        with torch.no_grad():
            outputs = self.model(**inputs)
            scores = torch.sigmoid(outputs.logits)
            
        return scores[0][0].item()

    def is_toxic(self, text):
        """
        Determine if a text is toxic based on the threshold
        
        Args:
            text (str): Text to analyze
            
        Returns:
            bool: True if text is toxic, False otherwise
        """
        score = self.predict_toxicity(text)
        return score >= TOXICITY_THRESHOLD

    def analyze_comments(self, comments):
        """
        Analyze a list of comments for toxicity
        
        Args:
            comments (list): List of comment dictionaries
            
        Returns:
            list: List of comments with toxicity scores
        """
        analyzed_comments = []
        
        for comment in comments:
            toxicity_score = self.predict_toxicity(comment['text'])
            is_toxic = toxicity_score >= TOXICITY_THRESHOLD
            
            # Add toxicity information to comment
            comment['toxicity_score'] = toxicity_score
            comment['is_toxic'] = is_toxic
            
            # Update in database
            update_document(
                'comments',
                {'comment_id': comment['comment_id']},
                {'$set': {
                    'toxicity_score': toxicity_score,
                    'is_toxic': is_toxic
                }}
            )
            
            analyzed_comments.append(comment)
            
        return analyzed_comments

    def get_toxic_comments(self, video_id=None):
        """
        Get all toxic comments from the database
        
        Args:
            video_id (str, optional): Filter by video ID
            
        Returns:
            list: List of toxic comments
        """
        query = {'is_toxic': True}
        if video_id:
            query['video_id'] = video_id
            
        return list(self.comments_collection.find(query))

if __name__ == "__main__":
    # Example usage
    detector = ToxicityDetector()
    test_text = "This is a test comment"
    score = detector.predict_toxicity(test_text)
    print(f"Toxicity score: {score}")
    print(f"Is toxic: {detector.is_toxic(test_text)}") 