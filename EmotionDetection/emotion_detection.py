import requests
import json

def emotion_detector(text_to_analyse):
    
    URL= "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    Input = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL, json = Input, headers=Headers)  # Send a POST request to the API with the text and headers

    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        dominant_emotion = max(formatted_response['emotionPredictions'][0]['emotion'], key=formatted_response['emotionPredictions'][0]['emotion'].get)

    elif response.status_code == 400:
        return "Invalid text! Please try again!"

    return {'anger': anger_score, 'disgust': disgust_score,'fear': fear_score, 'joy': joy_score,'sadness': sadness_score,'dominant_emotion': dominant_emotion}  # Return the response text from the API