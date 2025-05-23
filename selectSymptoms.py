# import streamlit as st
# from app.symptoms import symptoms
# import numpy as np
# import pandas as pd


# data={}
# def SymptomSelection():

#     disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
#              'Peptic ulcer disease','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
#              ' Migraine','Cervical spondylosis',
#              'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','Hepatitis A',
#              'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
#              'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
#              'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
#              'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
#              'Impetigo']

#     l2=[]
#     for x in range(0,len(symptoms)):
#       l2.append(0)

# # TESTING DATA
#     tr = pd.read_csv("models/Testing.csv")
#     tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
#                'Peptic ulcer disease':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
#                'Migraine':11,'Cervical spondylosis':12,'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,
#                'Chicken pox':16,'Dengue':17,'Typhoid':18,'Hepatitis A':19,'Hepatitis B':20,'Hepatitis C':21,
#                'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,'Common Cold':26,
#                'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
#                'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
#                '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
#                'Impetigo':40}},inplace=True)

#     X_test= tr[symptoms]
#     y_test = tr[["prognosis"]]
#     np.ravel(y_test)

# # TRAINING DATA
#     df=pd.read_csv("models/Training.csv")

#     df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
#                 'Peptic ulcer disease':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
#                 'Migraine':11,'Cervical spondylosis':12,
#                 'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'Hepatitis A':19,
#                 'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
#                 'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
#                 'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
#                 '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
#                 'Impetigo':40}},inplace=True)

#     X= df[symptoms]

#     y = df[["prognosis"]]
#     np.ravel(y)

#   #  # selectSymtomps.py
#   #   def message(symptom1, symptom2, symptom3, symptom4, symptom5):
#   #     if all(symptom == "Select a Symptom" for symptom in [symptom1, symptom2, symptom3, symptom4, symptom5]):
#   #        return None  # Means no valid symptoms selected
#   #     else:
#   #       return NaiveBayes(symptom1, symptom2, symptom3, symptom4, symptom5)
    
#     def  message():
#         if (symptom1 == "None" and  symptom2 == "None" and symptom3 == "None" and symptom4 == "None" and symptom5 == "None"):
#         # messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
#           print("No output")
#         else :
#           NaiveBayes()


#     def NaiveBayes():
#       from sklearn.naive_bayes import MultinomialNB
#       gnb = MultinomialNB()
#       gnb=gnb.fit(X,np.ravel(y))
#       from sklearn.metrics import accuracy_score
#       y_pred = gnb.predict(X_test)
#       print(accuracy_score(y_test, y_pred))
#       print(accuracy_score(y_test, y_pred, normalize=False))

#       psymptoms = [symptom1,symptom2,symptom3,symptom4,symptom5]

#       for k in range(0,len(symptoms)):
#         for z in psymptoms:
#             if(z==symptoms[k]):
#                 l2[k]=1

#       inputtest = [l2]
#       predict = gnb.predict(inputtest)
#       predicted=predict[0]
#       disease_name = None
#       for a in range(0, len(disease)):
#         if predicted == a:
#             disease_name = disease[a]
#             break

#       if disease_name:
#         return {'disease': disease_name}
#       else:
#         return {'disease': 'NO such disease'}

#     if st.button("Submit"):
#        predicted_data = NaiveBayes()
#        result(predicted_data)


#       h='no'
#       for a in range(0,len(disease)):
#         if(disease[predicted] == disease[a]):
#             h='yes'
#             break

#       if (h=='yes'):
       
#          data={'disease':disease[a]
#               }
#       else:
#          data={'disease':'NO such disease'}
# if st.button("Submit"):
#         # model integration
#         result(data)
