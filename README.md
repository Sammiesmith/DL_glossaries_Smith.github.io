# Automatic Glossary for CS182 Fall 2025 content
This pipeline prompts an LLM agent to identify key words in lecture, generate plain enlish definitions, and generate descriptions of how the terms are used in ML/DL. 

Website: https://sammiesmith.github.io/DL_glossaries_Smith.github.io/

## Instructions for running the pipeline
 Run build.py on a txt file of lecture transcript and a txt file of prerequisite material 

### Inputs to prompt 

 Lecture transcript txt, prerequiste material txt 

 Current version uses lecture 1 transcript and full eecs 127 reader

### Prompt
 
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

### Output
Output a csv with columns Term,Plain-English Explanation,Prerequisite Material Location,How Used in ML & Deep Learning

### Evaluation

#### Hallucinations
Seem to be few hallucinations in definitions and how the keyword is used in ML. The page numbers given for Prerequisite Material Location tab are sometimes hallucinated however-- which is a less destructive for student learning than halluciantion within definitions.


#### Issues

Prerequisite txt is too long to fit into a prompt. Have to use a truncated version (hence the 'Not explicitly in TOC' label under the 'Prerequisite Material Location' tab). Currently this is done naively (first x chars), not related to topics taught in the prerequisite material. Implication: generated description is derived more from the LLM's knowledge than from information in the prerequisite material.

* Feature/Bug: definitions/descriptions use technical vocabulary themselves, so the glossary itself requires a good amount of prerequisite knowledge. 

* Feature/Bug: definitions of mathematical objects do not explain their properties but might reference the usefulness of those properties. 

    For example the definition of a symmetric matrix is: A square matrix that is equal to its own transpose, meaning the elements across the main diagonal are identical. 

    The description of how symmetric matricies are used in ML/DL is: Symmetric matrices appear in various contexts in deep learning, particularly in covariance matrices (e.g., in Gaussian models), Hessian matrices (for second-order optimization), and kernel matrices. Their special properties (e.g., real eigenvalues, orthogonal eigenvectors) simplify mathematical analysis and can lead to more efficient computational algorithms. Understanding symmetric matrices is important for analyzing the curvature of loss landscapes and the stability of optimization processes.

    The description references useful properties of symmetric matricies (ex real eigenvalues) but does not explain what that means. 'Real eigenvalues' is not a keyword in the glossary since it was not mentioned in lecture because it is a prerequisite.
    
    The glossary itself does not have a prerequisite rubric; real eigenvalues are not explained but vectors are (a much more elementary concept). 





### Ideas for improvement

1) Automatically segment prerequisite material via Knowledge Componment (KC) using a) an LLM agent or b) naively using keywords in subheaders. This list can be either manually compiled or automatically compiled using the list of keywords gathered from lecture transcript. Then we can do a simple search over prerequisite material sections matching KC of section to keyword in lecture. I have poster describing accuracy of this pipline currently under review at SICSE TS 2026 conference. 


2) Use Retreival-Augmented-Generation (RAG) to inform generated description of keywords. In my experience while building my pipeline for SIGCSE, matching textsections to KCs via embeddings performs pooly. So this probably shouldn't be done via embedding match of keyword and textbook section. Using embeddings of the sentence per which the keyword was used might better match embeddings of textbook sections. A limitation of this however, is that the same keyword can be used in many different contexts. For example, I want to match the keyword 'affine transformation' to a prerequisite textbook section contaning the definition of affine transformations. But if my sentence is talking about affine transformations in neural networks, my embeddings might better match a section on neural networks that does not mention affine transformations at all.

## Ideas for additional features

Could be cool to have vocab quizes built into the platform. This could be implemented either as
 a) flashcards for more superficial learning or 
 b) follow up MCQs testing students' understanding of description of keywords. You could have a 'quiz me' button under each keyword that the user can click on and interact with. Can have one quiz question, multiple questions increasing in difficulty, or even questions that adapt to student mistakes (either naively in a role-player-journey flow chart structure or using llm teaching agents).

