from ollama import Client
from ollama import ChatResponse

client = Client(
  host='http://ollama:11434',
  #headers={'x-some-header': 'some-value'}
)

def check_application(application)->bool:
    print("checking an application")
    
    prompt = f"""
        {application}

        compare the application with the search criterions. could the application match?
        the tenant is searchning for an job:

        What I would prefer to do in my job:
            - Junior / ohne Berufserfahrung
            - Working with postgres, vue, node, c#
            - Working at an innovative company utilising AI
            - Working with three.js
            - Working as an automation engineer
            - Working with GEN AI
            - Programming related to manufacturing automation and AI
            - Working on AI in manufacturing automation
            - Engineering of mechatronic system, especially robots
            - CAD/Mechanical engineering of Robots for automation
            - Trainee at a company with reputaiton (mercedes, bosch, basf, abb, trumpf, ...)
            - Programming of robotic software for automation (Not what an technician would do, Not simply teach in)

        What I would accept:
            - erste Berufserfahrung

        What I dont want to do in my job:
            - work with ancient technologies (cobold, old c / c++ projects)
        What I dont want to do in my job:
            - job_descriptions that are for "Techniker"
        What I dont want to do in my job:
            - Werkstudent / Praktikum / Abschlussarbeit
        What I dont want to do in my job:
            - Work for a very small company
        
            
        Projects I did and had fun doing:
            - writing an computer vision algorithm to detect the positions of parts for pick and place in industrial automation
            - writing complex full-stack web-applications (vue, .net, postgres) with graphql to increase automation in the manufacturing space
            - writing algorithms to analyze 3D CAD geometries to automatically generate production plans using opencascade and custom step parsers
            - modifying wasm linker of LLVM to allow for dynamic linking of position dependent code of swift wasm
        
        Projects I would definetly like working on:
            - web based BIM software
            - reinforcement learning of pick an place software
            - AI in manufacturing
        
    """

    response: ChatResponse = client.chat(model='deepseek-r1:1.5b', messages=[
    {
        'role': 'user',
        'content': prompt,
    },
    ])

    print(response.message.content)


if __name__ == '__main__':
    check_application("engineer")