import os
import openai

API_KEY = "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"

openai.api_key = API_KEY
def gpt_create(CV, job, user_requests):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= f"""You are a professionar cover letter consultant.
    You are given a CV and a job description.
    You are asked to write a user's cover letter for a specific job.
    Make sure to use the same wording of the job offer 
    and that you show that the worker shares the values of the job offer.
    Write 150 words. Use professional language.
    CV: {CV}
    Job description: {job}
    User requests: {user_requests}
    Cover letter: """,
    temperature=0.7,
    max_tokens= 1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,

    )
    text = response.choices[0].text
    return text
    

def gpt_modify(chat_input, cover_letter):
    response = openai.Completion.create(
    model="davinci",
    prompt= f"""You are a professionar cover letter consultant.
    You are given a cover letter and a chat input.
    You are asked to modify the cover letter based on the chat input.
    Make sure to use the same wording of the chat input.
    Use professional language.
    Chat input: {chat_input}
    Cover letter: {cover_letter}
    Modified cover letter: """,
    temperature=0.7,
    max_tokens= 1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,

    )
    text = response.choices[0].text
    return text