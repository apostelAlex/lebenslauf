from openai import OpenAI
APIKEY = "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"





def ask_gpt(prompt, model_name):
    
    client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=APIKEY,
)   
    
    chat_completion = client.chat.completions.create(
        messages = [
        {"role": "system", "content": "You are a job consultant. You will be given a resume and you have to give a list of jobs that fit that resume. Don't write anything else."},
        {"role": "user","content": prompt},
        ],
        model="gpt-4",
    )

    result = chat_completion.choices[0].message.content.strip()
    # pyperclip.copy(summary)
    return result


if __name__ == "__main__":

    prompt = ""
    with open("/Users/a2/code/transcription/results/1697299777123103000/1697299777123103000.txt",  "r") as f:
        prompt = f.read()
    model_name = "gpt-3.5-turbo-16k-0613"
    print(ask_gpt(prompt, model_name))
