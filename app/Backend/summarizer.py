from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(context_chunks):
    combined_text = "\n\n".join(context_chunks)

    if len(combined_text) > 3000:
        combined_text = combined_text[:3000]

    summary = summarizer("Summarize the following Text: " + combined_text, max_length=300, min_length=50, do_sample=False)
    return summary[0]['summary_text']
