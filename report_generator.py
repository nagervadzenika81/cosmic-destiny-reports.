import openai

def generate_cosmic_report(name, birthdate, location):
    prompt = f"Generate a personalized cosmic destiny report for {name}, born on {birthdate} in {location}. Include numerology, astral alignment, and mythology."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
