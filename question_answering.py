from transformers import pipeline

# Question answering

question_answerer = pipeline("question-answering")
result_qa = question_answerer(
    question="Where do I work?",
    context="My name is Sylvain and I work at Hugging Face in Brooklyn",
)

print(result_qa)