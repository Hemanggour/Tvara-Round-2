from langchain_openai import ChatOpenAI
from pydantic import BaseModel


class OutputSchema(BaseModel):
    """Schema for response."""
    allowed: bool
    flag: str


def get_openai(*args, **kwargs):
    
    llm = ChatOpenAI(
        model="gpt-5-nano",
        temperature=0.2,
        max_retries=2,
    )

    structured_llm = llm.with_structured_output(OutputSchema, method="json_schema")

    return structured_llm
