#open ai connection
from cover_letter.settings import load_settings
import PyPDF2

from openai import OpenAI

def read_resume(resume_path: str) -> str:
  pdfFileObj = open(resume_path, 'rb')
  reader = PyPDF2.PdfReader(pdfFileObj)
  return reader.pages[0].extract_text()



def create_cover_letter(job_desc:str, resume:str)-> str:
  settings = load_settings()
  client = OpenAI(
      api_key=settings.openai_api_key
  )

  system_prompt_content = f"You are a helpful assistant to a job seeker. You are helping them write a cover letter for a job posting. Here is the job posting:\n\n```\n{job_desc}\n```"
  system_prompt = {"role": "system", "content": system_prompt_content}
  resume_prompt_content = f"Here is the resume of the job seeker:\n\n```\n{resume}\n```"
  resume_prompt = {"role": "system", "content": resume_prompt_content}
  user_prompt_content = "Write a cover letter for the given job posting. Use the resume to match skills to the job posting. Use numbers to quantify your accomplishments. Just write the body of the cover letter and nothing else. If the job description contains skills outside of the resume, write about how I can learn those skills quickly."
  user_prompt = {"role": "user", "content": user_prompt_content}
  completion = client.chat.completions.create(
    model=settings.model,
    messages=[
      system_prompt,resume_prompt,
      user_prompt
    ]
  )    
  return completion.choices[0].message.content
    


