### 
import os
import datetime

def synthesise_application(job_description, application_chunks):
    f"""
        the task is to synthesise an job application from the given input chunks
        wrap the your result in asterics ***. 
        the resulting application should have between 450-550 words.
        given the follwoing chunks

        given the following job description:

        {job_description}


    
    """

def pick_chunks(job_description, application_chunks):
    pass

def refiner():
    pass

def main():
    chunk_selection = pick_chunks(job_description, all_chunks)
    job_application = synthesise_application(job_application, chunk_selection)

    # write job application to file
    file_name = datetime.datetime.now
    with os.open(file_name) as f:
        f.write(job_application)
