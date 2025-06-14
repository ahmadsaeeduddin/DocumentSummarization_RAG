from transformers import pipeline

# This downloads the model on first run (cached afterward)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(context_chunks):
    # Combine all chunks into one string
    combined_text = "\n\n".join(context_chunks)

    # Limit the input length (model has max token limit)
    if len(combined_text) > 3000:
        combined_text = combined_text[:3000]

    summary = summarizer("Summarize the following Text: " + combined_text, max_length=300, min_length=50, do_sample=False)
    return summary[0]['summary_text']
