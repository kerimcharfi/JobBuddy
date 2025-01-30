#This script takes existing applications and creates and sorts chunks of reusable paragraphs

#import ollama
from utils import txt_file_iter

"""
    output format

    [
    {
        tags: ["software-basisc", "ci/cd"],
        paragraph: "
            
        "
    }   
    ]

"""

def process_file(file_content: str):
    print("---")
    print(file_content[0:150])
    print("---")


def execute():
    # iterate
    for file in txt_file_iter("C:/Users/Kerim/OneDrive/Dokumente Kerim/Bewerbung/Anschreiben/TextDatabase"):
        process_file(file)
    pass

if __name__ == '__main__':
    execute()