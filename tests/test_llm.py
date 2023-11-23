import pytest
from cover_letter.llm import read_resume, create_cover_letter
from cover_letter.settings import load_settings
job_desc = """ 
Introduction:

FitnessMatrixInc is an unique approach to health and wellness that is based on the principle of bio-individuality. This means that we believe that everyone is different and has their own unique needs and challenges. We will work with you to understand your biochemistry and develop a personalized plan that is right for you.

Role Responsibilities:

Work in close collaboration with the Business Intelligence Lead, Federal Data Lead, and other Program teams 
Develop, maintain, and improve BI tools, build and enhance standard operating procedures (SOPs) 
Manage various data sets and active Google workbooks with adjacent contract teams, monitor and analyze financial health information at the project and program levels 
Communicate with client leadership to assess data needs and emerging requirements 
Work with large data sets, workbooks, and spreadsheets to manipulate and manage program-level information using macros, queries, scripts, etc. 
Gather requirements and lead the development of long-term data management tools, processes, and solutions based on organizational needs. 
Be comfortable working with collaboration tools such as; Google Suite, Microsoft Office 
Providing general support to the client including, but not limited to, analysis, data calls, financial management, risk management, audits, and project management-related tasks. 

Qualifications:

Bachelor's Degree in business, business intelligence, data or information management, or similar. 
Proficient in Google Scripts 
Minimum 1 year of data or information management and/or data analysis experience. 
Experience using Microsoft Excel and Google Sheets (macros, imports, query functions). 
Experience with developing in Google App Script is a plus. 
Experience using SQL Developer is a plus. 
Excellent written and verbal communication skills. 
Willing to work in an administratively manual environment while working towards automation of processes in the future. 

Why should we work with FitnessMatrixInc?

FitnessMatrixInc is the leading provider of holistic and multidimensional health and wellness services. We offer a comprehensive approach to health and wellness. We take into account all aspects of your life, from your physical fitness and nutrition to your mental, emotional, and spiritual well-being. We use the latest science and technology to develop our programs and services. We are constantly innovating and finding new ways to help our clients achieve their goals. 
We offer a variety of programs and services to meet your needs and budget."""


def test_load_resume():
    """
    Test case to verify the loading of a resume.

    It loads the settings and asserts that the name "SWARNASHRUTI JUPUDI" is present in the loaded resume.

    """
    settings = load_settings()
    assert "SWARNASHRUTI JUPUDI" in read_resume(settings.resume_path)

def test_create_cover_letter():
    """
    Test case for the create_cover_letter function.

    This test verifies that the generated cover letter contains the expected content,
    such as the company name and the applicant's name.

    It assumes that the `load_settings` function has been implemented and returns the
    necessary settings, and that the `read_resume` function has been implemented and
    correctly reads the resume from the specified path.

    Raises:
        AssertionError: If the expected content is not found in the generated cover letter.
    """
    settings = load_settings()
    cover_letter_content = create_cover_letter(job_desc, read_resume(settings.resume_path))
    assert "FitnessMatrixInc" in cover_letter_content
    assert "swarnashruti jupudi" in cover_letter_content.lower()

def open_ai_set():
    """
    This function sets up the OpenAI API by loading the settings and asserting that the OpenAI API key is not empty.

    Raises:
        AssertionError: If the OpenAI API key is empty in the settings.

    """
    settings = load_settings()
    assert len(settings.openai_api_key) > 0  in settings