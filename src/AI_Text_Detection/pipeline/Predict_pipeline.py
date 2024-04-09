import os
from AI_Text_Detection.utils.common import load_object

class PredictPipeline:
    def __init__(self) -> None:
        pass

    def predict(self, text):
        # model = load_object(os.path.join("artifacts","model_training","model.pkl"))
        model = load_object(os.path.join("model","model.pkl"))
        result = model.predict(text)
        if result[0] == 0:
            result = "Human"
        else:
            result = "AI"
        
        return result
        
