import google.generativeai as genai
from config.config import GEMINI_API_KEY
from src.utils.db_handler import get_collection, update_document

class GeminiAnalyzer:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
        self.analysis_collection = get_collection('analysis')

    def generate_insights(self, toxic_comments):
        """
        Generate insights from a list of toxic comments
        
        Args:
            toxic_comments (list): List of toxic comment dictionaries
            
        Returns:
            dict: Analysis results including summary and recommendations
        """
        # Prepare the prompt
        comments_text = "\n".join([f"- {comment['text']}" for comment in toxic_comments])
        prompt = f"""
        Analyze the following toxic comments from a YouTube video and provide:
        1. A summary of the main themes and patterns in the toxic comments
        2. Potential reasons for the toxicity
        3. Recommendations for the content creator to address or prevent such comments
        
        Comments:
        {comments_text}
        
        Please provide a structured analysis with clear sections.
        """
        
        try:
            # Generate analysis
            response = self.model.generate_content(prompt)
            analysis_text = response.text
            
            # Create analysis document
            analysis = {
                'video_id': toxic_comments[0]['video_id'] if toxic_comments else None,
                'analysis_text': analysis_text,
                'num_comments_analyzed': len(toxic_comments),
                'timestamp': datetime.utcnow().isoformat()
            }
            
            # Store in database
            analysis_id = self.analysis_collection.insert_one(analysis).inserted_id
            analysis['_id'] = analysis_id
            
            return analysis
            
        except Exception as e:
            print(f"Error generating insights: {e}")
            return None

    def get_analysis(self, video_id):
        """
        Get the most recent analysis for a video
        
        Args:
            video_id (str): YouTube video ID
            
        Returns:
            dict: Analysis document or None if not found
        """
        return self.analysis_collection.find_one(
            {'video_id': video_id},
            sort=[('timestamp', -1)]
        )

    def analyze_channel(self, video_ids):
        """
        Analyze toxic comments across multiple videos
        
        Args:
            video_ids (list): List of video IDs to analyze
            
        Returns:
            dict: Channel-wide analysis
        """
        all_toxic_comments = []
        
        # Collect toxic comments from all videos
        for video_id in video_ids:
            comments = self.analysis_collection.find({'video_id': video_id, 'is_toxic': True})
            all_toxic_comments.extend(list(comments))
        
        # Generate channel-wide analysis
        return self.generate_insights(all_toxic_comments)

if __name__ == "__main__":
    # Example usage
    analyzer = GeminiAnalyzer()
    test_comments = [
        {'text': 'This video is terrible!', 'video_id': 'test123'},
        {'text': 'Worst content ever', 'video_id': 'test123'}
    ]
    analysis = analyzer.generate_insights(test_comments)
    print("Analysis:", analysis['analysis_text']) 