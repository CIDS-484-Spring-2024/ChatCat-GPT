# Tokenizer 

from transformers import GPT2Tokenizer

# Initialize the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Tokenize the input text
text = "Hello, how are you?"
input_ids = tokenizer.encode(text, add_special_tokens=True)