from typer import Typer
from cover_letter.llm import create_cover_letter, read_resume
from cover_letter.settings import load_settings
import pyperclip
app = Typer()
@app.command()
def main():
    print("Copy the job description")
    job_desc = pyperclip.paste()
    input()
    settings = load_settings()
    print(create_cover_letter(job_desc, read_resume(settings.resume_path)))