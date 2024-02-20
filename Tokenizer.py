# Tokenizer 

import torch
from torch.utils.data import DataLoader, Dataset
from transformers import GPT2Tokenizer

# Step 1: Read Text Data
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data

# Example: Read text data from a local file
text_data = read_text_file('names.txt')

# Step 2: Tokenize Text Data
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenized_data = [tokenizer.encode(text, add_special_tokens=True) for text in text_data]

# Step 3: Create Custom Dataset
class TextDataset(Dataset):
    def __init__(self, tokenized_data):
        self.tokenized_data = tokenized_data

    def __len__(self):
        return len(self.tokenized_data)

    def __getitem__(self, idx):
        return torch.tensor(self.tokenized_data[idx], dtype=torch.long)

# Initialize your dataset
dataset = TextDataset(tokenized_data)

# Step 4: Create Data Loader
batch_size = 4
data_loader = DataLoader(dataset, batch_size=16, shuffle=True)
