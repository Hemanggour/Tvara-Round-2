from src.prompt import SYSTEM_PROMPT
from src.utils import read_page

def process_moderation(llm, filepath):
    raw_text = read_page(filepath)

    result = llm.invoke(SYSTEM_PROMPT.format(text=raw_text))

    return result
