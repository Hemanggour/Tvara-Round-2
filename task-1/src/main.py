from src.llm.get_llm import get_openai
from src.moderation.process_mod import process_moderation

llm = get_openai()

result = process_moderation(llm, "./data/doc.pdf")

print(result)
