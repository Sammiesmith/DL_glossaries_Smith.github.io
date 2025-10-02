import os
import pandas as pd
from clients.google_gemini import get_llm_response
from code.data_reader import read_txt

lecture_transcript_path = "./data/lecture1_transcript.txt"
lecture_text = read_txt(lecture_transcript_path)

prereq_path = "./data/machlearn_text.txt"
prereq_text = read_txt(prereq_path)


# Build prompt
prompt = f'''
You are an expert teaching assistant. I will provide you with (a) a lecture transcript and (b) prerequisite course materials.
Your task is to build a full glossary of all technical terms used in the lecture. For each term you must:

1. Write the term exactly as it appears in the lecture.
2. Give a 1–2 sentence plain-English explanation (no math symbols).
3. Provide the exact location in the prerequisite materials (page number and section).
4. Add a detailed but beginner-friendly explanation of how the term is used in machine learning and deep learning — technical yet interpretable, including typical roles in architectures, training, optimization, or evaluation.

Return the result as a CSV with these columns:
Term | Plain-English Explanation | Prerequisite Material Location | How Used in ML & Deep Learning.

Please do not use commas such that it interferes with the csv format. You must return a valid csv with exactly and only the specified columns

Lecture Transcript:
{lecture_text}

Prerequisite Materials:
{prereq_text} 
'''

# 5. Send to Gemini (Flash 2.5)
response = get_llm_response(prompt, "")

# 6. Print response
print(response)

############################################

csv_output_path = './outputs/Lecture1_Glossary.csv'
with open(csv_output_path, 'w', encoding='utf-8') as f:
    f.write(response)

print("Saved CSV to", csv_output_path)

