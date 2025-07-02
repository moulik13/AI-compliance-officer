from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Sample input text (can be longer for better summarization)
text = """
The European Union has announced a new policy focused on improving digital infrastructure across its member states.
The policy aims to enhance internet accessibility, reduce data costs, and support technological innovation. 
This initiative is part of a broader strategy to increase digital competitiveness in global markets.
"""

# Run the summarization
summary = summarizer(text, max_length=100, min_length=30, do_sample=False)

# Print output
print("Original Text:")
print(text)
print("\nGenerated Summary:")
print(summary[0]['summary_text'])
