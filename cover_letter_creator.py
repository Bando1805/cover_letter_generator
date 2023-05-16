# main.py
from tools.job_offer_linkedin import LinkedInDriver
from tools.gpt import gpt_create, gpt_modify
from tools.pdf_extractor import extract_text_from_pdf
from tools.pdf_creator import create_pdf_from_text

linkedin_driver = LinkedInDriver()

def generate_cover_letter(CV_file_path, job_url, job_description,user_requests):
    CV_text = extract_text_from_pdf(CV_file_path)
    
    if job_description != '':
        job_text = job_description
    else:
        job_text = linkedin_driver.get_job_description(job_url)

    if job_text.startswith('An error occurred'):
        return None, None
    
    else:
        cover_letter = gpt_create(CV_text, job_text, user_requests)
        cover_letter_filename = f'cover_letter.pdf'
        create_pdf_from_text(cover_letter, cover_letter_filename)
        
        return cover_letter, cover_letter_filename


