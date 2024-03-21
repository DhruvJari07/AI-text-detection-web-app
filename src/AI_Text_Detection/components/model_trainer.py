import sys
import pandas as pd
from AI_Text_Detection import logger
from AI_Text_Detection.utils.common import save_object
from AI_Text_Detection.exception import CustomException
from AI_Text_Detection.entity.config_entity import ModelTrainingConfig
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB, ComplementNB
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import accuracy_score

class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def create_model_pipeline(self):
        '''
        creating the model pipeline using Naive Bayes, Complement Naive Bayes
        & Linear SVC algorithm
        '''
        try: 
            logger.info(f"model pipeline building initiated")

            clf1 = RandomForestClassifier(n_estimators=50, random_state=1)
            clf2 = LinearSVC()
            clf3 = ComplementNB()

            clf = VotingClassifier(estimators=[('RFC', clf1), ('SVC', clf2), ('CNB', clf3)], voting='hard')

            model_pipeline = Pipeline([
                ('count_vectorizer', CountVectorizer(stop_words='english')),  # Step 1: CountVectorizer
                ('tfidf_transformer', TfidfTransformer()),  # Step 2: TF-IDF Transformer
                ('Ensemble_Voting', clf)])
            
            logger.info(f"Model pipeline created")
            
            return model_pipeline #{'naive_bayes':pipelineMNB, 'Complement_Naive_Bayes':pipelineCNB, 'Linear SVC':pipelineSVC}


        except Exception as e:
            raise CustomException(e, sys)
        

    def initiate_model_training(self, X_train, y_train, X_test, y_test, model_pipeline):
        '''
        training the model on the transformed data
            
        '''
        try: 
            logger.info(f"model traininng initiated")

            model_pipeline.fit(X_train, y_train)
            y_pred = model_pipeline.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            """model_accuracy = {}
            for model_name, pipeline in model_pipeline.items():
                pipeline.fit(X_train, y_train)
                y_pred = pipeline.predict(X_test)
                accuracy = accuracy_score(y_test, y_pred)
                model_accuracy[model_name] = accuracy"""

            
            logger.info(f"model traininng completed")

            ## To get best model score from dict
            save_object(file_path=self.config.trained_model_path, obj=model_pipeline)
            logger.info(f"model have the accuracy of {accuracy}")
            logger.info(f"model saved to artifacts/model_training for prediction")

            return accuracy
        
    
        except Exception as e:
                raise CustomException(e, sys)

