from transformers import pipeline

# Zero-shot classification

classifier = pipeline("zero-shot-classification")
result_c = classifier(
    "This is a course about the Transformers library",
    candidate_labels=["education", "politics", "business"],
)

print(result_c)