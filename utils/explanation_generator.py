from models.load_models import generator

def generate_explanation(text, knowledge):

    prompt = f"""
    Health advice: {text}

    Medical references:
    {knowledge}

    Explain whether this advice is medically correct or misinformation.
    """

    response = generator(
        prompt,
        max_length=120,
        do_sample=False
    )

    return response[0]["generated_text"]
