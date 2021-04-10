import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import math
import spacy
import os
import sys

QUESTIONS_FINAL = []
ACTUAL_ANSWERS_DATASET=[]
TAGS_DATASET = []
SIMILARITY_RESULT=[]


def CalculateSimilarity(rand_id_list,anslist,user_input):
    print("entered run1")
    nlp = spacy.load('en_core_web_sm')
    glv_position = 0
    glv_score = 0
    glv_marks = 0

    python_merged_df = pd.read_csv(os.path.join(os.path.dirname(__file__),"Python_Cleaned_Questions.csv"))
    print("merged_df")
    for question_random_id in rand_id_list:
        answers_randID = python_merged_df[python_merged_df.Id == int(question_random_id)][['A_Score', 'P_A_Body_wo_freq']]
        answers_randID.A_Score -= answers_randID.A_Score.min()
        answers_randID.A_Score /= answers_randID.A_Score.max()
        answers_randID.A_Score *= (10 - 1)
        answers_randID.A_Score += 1

        scores = answers_randID['A_Score'].tolist()
        print("spacy")
        for answer in enumerate(anslist):
            doc1 = nlp(answer[1])
            doc2 = nlp(user_input[0])
            print("calculating similarity")
            if doc1.similarity(doc2) > glv_score:
                score = doc1.similarity(doc2)
                glv_position = answer[0]
            glv_marks = score * glv_position
            print(glv_marks)

        return math.ceil(glv_marks)

