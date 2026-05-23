def load_prompt(file_name):
    """
    Load prompt text from prompts/ folder.
    """

    with open(f"prompts/{file_name}", "r", encoding="utf-8") as file:
        return file.read()