from openai import OpenAI
import json
import os 
from dotenv import load_dotenv

load_dotenv()

OPEN_AI_KEY = os.environ['OPEN_AI_KEY']

gpt_api_key=OPEN_AI_KEY

client=OpenAI(api_key=gpt_api_key)

schema = {
    "type": "object",
    "properties": {
        "logs": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "timestamp": {
                        "type": "string",
                        "description": "The timestamp when the log entry was generated"
                    },
                    "logLevel": {
                        "type": "string",
                        "description": "The severity level of the log entry"
                    },
                    "message": {
                        "type": "string",
                        "description": "The content of the log message"
                    },
                    "source": {
                        "type": "string",
                        "description": "The source of the log entry (if available)"
                    },
                    "logStream": {
                        "type": "string",
                        "description": "Indicates whether the log message originated from stdout or stderr"
                    }
                },
                "required": ["timestamp", "logLevel", "message"]
            }
        },
        "id": {
            "type": "string",
            "description": "The ID of the Docker container"
        },
        "name": {
            "type": "string",
            "description": "The name of the Docker container"
        },
        "status": {
            "type": "string",
            "description": "The status of the Docker container"
        },
        "overall_health": {
            "type": "string",
            "description": "This gives the overall overview on the health of the container by analysing the logs. This should be atleast 50 words long."
        },
        "suggestions": {
            "type": "string",
            "description": "This suggests what should be done right now to make either the docker container running or to optimise the current state of the container. This should be pointwise with each point on a new line"
        }
    },
    "required": ["logs", "id", "name", "status", "overall_health", "suggestions"],
    "description": "Schema for representing a report generated from Docker logs"
}


def reportGeneration(obj):

    logs = obj['logs']
    id = obj['id']
    name = obj['name']
    status = obj['status']
    
    prompt_template = f"""
        Read the following prompt and specify each of its fields as mentioned below:

        1. Container ID
        Enter the ID of the Docker container: {id}

        2. Container Name
        Enter the name of the Docker container: {name}

        3. Container Status
        Enter the status of the Docker container: {status}

        4. Logs
        Analyze the provided container logs and generate a report based on the following questions:
        
        a. What is the severity level (log level) of each log entry?
        b. What is the content of each log message?
        c. (Optional) Is there any source mentioned for each log entry?
        d. Is each log entry from stdout or stderr?

        The provided logs are as follows:
        {logs}
    """

    gpt_prompt = prompt_template

    print(prompt_template)
    
    response=client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": gpt_prompt},
        ],
        functions=[{"name": "print", "parameters": schema}],
        function_call={"name": "print"},
    )

    print(response.choices[0].message.function_call.arguments)

    return json.loads(response.choices[0].message.function_call.arguments)


# print(reportGeneration({
#   "id": "4a1f80c09ef10accf103d6ea64d66f66955382a7a63930b5f4e6bc200233b64f",
#   "logs": [
#     "Using sqlite database at /etc/todos/todo.db",
#     "Listening on port 3000",
#     ""
#   ],
#   "name": "dockertest_container",
#   "status": "running"
# }))

generated_script = """FROM node:18-alpine
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000
EOF
"""