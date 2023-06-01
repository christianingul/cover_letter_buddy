# constants.py
JOB_DESCRIPTION_TEMPLATE = """
    From the given job posting on a company's webpage, please extract key details including the job responsibilities, required qualifications, 
    the company culture, any unique aspects of the company, compensation, and benefits.
    If the information isn't available, please indicate as "not found". Also, do never make up information, this is crucial.
    >>> {requests_result} <<<
    Extracted:
"""

TASK_DESCRIPTION_TEMPLATE = """
    Assume the role of a professional cover letter writer with knowledge of Applicant Tracking Systems (ATS). 

    You are a state-of-the-art AI language model that has been tasked with revising an existing cover letter based on the provided job information for a {role} at {name_of_company}
    You are expected to utilize the details from the job description and company information {job_information} and the existing cover letter {cover_letter}.

    The revised cover letter must accomplish the following:

    1. Create a narrative that logically and emotionally explains why the job responsibilities, qualifications, and company culture are appealing. 
    This narrative should align with the candidate's background, experience, and aspirations as depicted in the existing cover letter.

    2. Identify the skills, qualifications, and experiences in the existing cover letter that directly align with the requirements and responsibilities in the job description.

    3. Incorporate the action verbs, phrases, and keywords found in the job description into the revised cover letter where they appropriately describe the candidate's skills and experiences.
     These terms should also be ATS-friendly to increase the chances of the cover letter passing the ATS screening.

    4. Maintain a professional tone and language throughout the revised cover letter.

    Your revised cover letter should tell a compelling story about the candidate while effectively showcasing their qualifications for the role at the company.
    It should also be optimized for an Applicant Tracking System (ATS), using keywords from the job description where they accurately represent the candidate's qualifications. 

    Do not add any skills, experiences, or qualifications that are not present in the original cover letter or misrepresent the candidate's background.
    Your goal is to enhance the existing cover letter using the information provided, not to fabricate details. You should NEVER mention compensation in the cover letter.

    Create a cover letter that not only satisfies the requirements of the role but also captivates the reader, making the candidate a memorable and attractive choice for the {role} at {name_of_company}
    """
