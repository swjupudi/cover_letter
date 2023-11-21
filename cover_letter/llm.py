#open ai connection
from cover_letter.settings import load_settings


from openai import OpenAI

def create_cover_letter(job_desc:str)-> str:
  settings = load_settings()
  client = OpenAI(
      api_key=settings.openai_api_key
  )

  system_prompt_content = f"You are a helpful assistant to a job seeker. You are helping them write a cover letter for a job posting. Here is the job posting:\n\n```\n{job_desc}\n```"
  system_prompt = {"role": "system", "content": system_prompt_content}
  user_prompt_content = "Write a cover letter for the given job posting"
  user_prompt = {"role": "user", "content": user_prompt_content}
  completion = client.chat.completions.create(
    model=settings.model,
    messages=[
      system_prompt,
      user_prompt
    ]
  )    
  return completion.choices[0].message.content
    


