import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train_face_recognition_model(dataset_file):
    df = pd.read_csv(dataset_file)

    X = df.drop(['label', 'person_name'], axis=1)
    y = df['label'] 

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    svm_classifier = SVC(kernel='linear', probability=True)

    svm_classifier.fit(X_train, y_train)

    y_pred = svm_classifier.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model accuracy: {accuracy:.2f}')

    joblib.dump(svm_classifier, 'face_recognition_model.pkl')
    print('Trained model saved as face_recognition_model.pkl')

