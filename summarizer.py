# from openai import OpenAI
# import os
# from dotenv import load_dotenv

# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def generate_summary(context_chunks, model="gpt-3.5-turbo"):
#     combined_text = "\n\n".join(context_chunks)

#     prompt = f"""
#     You are a helpful assistant. Summarize the following document as clearly and concisely as possible.

#     Document:
#     {combined_text}
#     """

#     response = client.chat.completions.create(
#         model=model,
#         messages=[
#             {"role": "system", "content": "You are an expert summarizer."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.3,
#         max_tokens=500
#     )

#     summary = response.choices[0].message.content.strip()
#     return summary


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
