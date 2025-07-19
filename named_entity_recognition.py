from transformers import pipeline

# Named entity recognition

ner = pipeline("ner", grouped_entities=True)
result_ner = ner("My name is Sylvain and I work at Hugging Face in Brooklyn.")

print(result_ner)