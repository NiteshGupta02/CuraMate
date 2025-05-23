import streamlit as st
from app.symptoms import symptoms
import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from urllib.parse import urlencode
from data.ayurvedic_cure_data import ayurvedic_cures



disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
           'Peptic ulcer disease', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
           'Migraine', 'Cervical spondylosis', 'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria',
           'Chicken pox', 'Dengue', 'Typhoid', 'Hepatitis A', 'Hepatitis B', 'Hepatitis C', 'Hepatitis D',
           'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis', 'Common Cold', 'Pneumonia',
           'Dimorphic hemmorhoids(piles)', 'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism',
           'Hypoglycemia', 'Osteoarthristis', 'Arthritis', 'Paroymsal Positional Vertigo', 'Acne',
           'Urinary tract infection', 'Psoriasis', 'Impetigo']


tr = pd.read_csv("models/Testing.csv")
tr.replace({'prognosis': {1: 'Fungal infection', 2: 'Allergy', 3: 'GERD', 4: 'Chronic cholestasis', 5: 'Drug Reaction',
                          6: 'Peptic ulcer disease', 7: 'AIDS', 8: 'Diabetes', 9: 'Gastroenteritis', 10: 'Bronchial Asthma',
                          11: 'Hypertension', 12: 'Migraine', 13: 'Cervical spondylosis', 14: 'Paralysis (brain hemorrhage)',
                          15: 'Jaundice', 16: 'Malaria', 17: 'Chicken pox', 18: 'Dengue', 19: 'Typhoid', 20: 'Hepatitis A',
                          21: 'Hepatitis B', 22: 'Hepatitis C', 23: 'Hepatitis D', 24: 'Hepatitis E', 25: 'Alcoholic hepatitis',
                          26: 'Tuberculosis', 27: 'Common Cold', 28: 'Pneumonia', 29: 'Dimorphic hemmorhoids(piles)',
                          30: 'Heartattack', 31: 'Varicoseveins', 32: 'Hypothyroidism', 33: 'Hyperthyroidism', 34: 'Hypoglycemia',
                          35: 'Osteoarthristis', 36: 'Arthritis', 37: 'Paroymsal Positional Vertigo', 38: 'Acne',
                          39: 'Urinary tract infection', 40: 'Psoriasis', 41: 'Impetigo'}}, inplace=True)


df = pd.read_csv("models/Training.csv")
df.replace({'prognosis': {1: 'Fungal infection', 2: 'Allergy', 3: 'GERD', 4: 'Chronic cholestasis', 5: 'Drug Reaction',
                         6: 'Peptic ulcer disease', 7: 'AIDS', 8: 'Diabetes', 9: 'Gastroenteritis', 10: 'Bronchial Asthma',
                         11: 'Hypertension', 12: 'Migraine', 13: 'Cervical spondylosis', 14: 'Paralysis (brain hemorrhage)',
                         15: 'Jaundice', 16: 'Malaria', 17: 'Chicken pox', 18: 'Dengue', 19: 'Typhoid', 20: 'Hepatitis A',
                         21: 'Hepatitis B', 22: 'Hepatitis C', 23: 'Hepatitis D', 24: 'Hepatitis E', 25: 'Alcoholic hepatitis',
                         26: 'Tuberculosis', 27: 'Common Cold', 28: 'Pneumonia', 29: 'Dimorphic hemmorhoids(piles)',
                         30: 'Heartattack', 31: 'Varicoseveins', 32: 'Hypothyroidism', 33: 'Hyperthyroidism', 34: 'Hypoglycemia',
                         35: 'Osteoarthristis', 36: 'Arthritis', 37: 'Paroymsal Positional Vertigo', 38: 'Acne',
                         39: 'Urinary tract infection', 40: 'Psoriasis', 41: 'Impetigo'}}, inplace=True)


data = {'disease': 'No result yet'}

def message(symptom1, symptom2, symptom3, symptom4, symptom5):
    if all(symptom == "Select a Symptoms" for symptom in [symptom1, symptom2, symptom3, symptom4, symptom5]):
        return None
    else:
        return NaiveBayes(symptom1, symptom2, symptom3, symptom4, symptom5)
    
def NaiveBayes(symptom1, symptom2, symptom3, symptom4, symptom5):

    X_train = df[symptoms]
    y_train = df[["prognosis"]]
    X_test = tr[symptoms]
    y_test = tr[["prognosis"]]


    gnb = MultinomialNB()
    gnb.fit(X_train, np.ravel(y_train))

    
    psymptoms = [symptom1, symptom2, symptom3, symptom4, symptom5]
    l2 = [0] * len(symptoms)

    for k in range(0, len(symptoms)):
        for z in psymptoms:
            if z == symptoms[k]:
                l2[k] = 1

    inputtest = [l2]
    predicted_disease_name = gnb.predict(inputtest)[0]  

    return predicted_disease_name 


