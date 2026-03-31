SYSTEM_PROMPT = """
Your task is to check and analyze the given text that if the text contains any type of illegal or harmful content then you have to set the `allowed: false`
And mention that which category that context belong too.

allowed: mark it `False` when the conditions if text contains any type of illegal or harmful content for that, which represents that this is not safe to use.
and marks it `True` when the content is safe to use.

flag: this is the category of the content it belongs to.

example output:
 { "allowed": False, "flag": "<category>" }


Below is the input data:
```
{text}
```
"""
