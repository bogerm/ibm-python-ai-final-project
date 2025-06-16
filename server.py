from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detection
import os

base_dir = os.path.abspath(os.path.dirname(__file__))

# Explicitly set template folder
app = Flask("EmotionDetection", 
    template_folder=os.path.join(base_dir, "templates"),
    static_folder=os.path.join(base_dir, "static"))

@app.route("/emotionDetector")
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detection(text_to_analyze)
    
    if result is None or result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    else:
        formatted_output = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        return formatted_output

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)
