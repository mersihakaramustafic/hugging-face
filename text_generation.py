from transformers import pipeline

# Text generation

generator = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-360M")
result_g = generator(
    "In this course, we will teach you how to",
    max_new_tokens=30,
    num_return_sequences=2,
    truncation=True
)

print(result_g)