
# ChatCat-GPT

This project is suppose to act like Chat-GPT. It will be targeting information retaining cats specifically.

I love cats and wanted to create or replicate something similar to Chat-GPT to further my understanding while gaining knowledge about Generative Pre-trained Transformers (GPT).

# Overview

ChatCat-GPT is an artificial intelligence program that generates dialogue. Created by open-AI, this highly capable chatbot uses machine learning algorithms to process and analyze large amounts of data. This data is then used to generate responses to the users’ inquiries. This language processing program can understand human language as it is spoken and written, allowing it to understand the information it is fed, and what to spit back out. Anyone can type out a question retaining to cats, and ChatCat-GPT spits back out an easily understandable answer – in a variety of formats with precise stipulations.
For example, you can ask the question, “Why does my cat want to scratch all of my furniture?”.

One of the key features of ChatCat-GPT is its ability to generate responses like humans in real-time, based on the user’s input. It can give natural answers to questions in a conversational tone and can generate any questions that is about cats.

# Outline

## I. Introduction

--- A. Brief explanation of AI and its applications in chatbots.

--- B. Introduction to Chat-GPT and its capabilities.

--- C. Importance of creating an AI like Chat-GPT from scratch.

## II. Understanding the Basics of Natural Language Processing (NLP)

--- A. Explanation of NLP and its role in chatbot development.

--- B. Overview of key NLP concepts such as tokenization, word embeddings, and language modeling.

--- C. Importance of data preprocessing and cleaning for NLP tasks.

## III. Building the Neural Network Architecture

--- A. Introduction to deep learning and neural networks.

--- B. Explanation of transformer-based architectures for language modeling.

--- C. Overview of the GPT (Generative Pre-trained Transformer) architecture.

--- D. Discussion on fine-tuning and transfer learning for chatbot development.

## IV. Training the AI Model

--- A. Gathering and preprocessing training data.

--- B. Explanation of pre-training and fine-tuning stages.

--- C. Overview of training techniques such as unsupervised learning and reinforcement learning.

--- D. Importance of iterative training and model evaluation.

## V. Deploying and Improving the Chatbot

--- A. Discussion on deployment options for the AI chatbot.

--- B. Importance of continuous improvement through user feedback and iteration.

--- C. Overview of techniques for handling user queries and generating appropriate responses.

--- D. Ethical considerations and guidelines for responsible AI chatbot development.

## VI. Conclusion

--- A. Emphasizing the potential of creating an AI like Chat-GPT from scratch.

--- B. Encouragement for readers to explore and contribute to the field of AI chatbot development.

----------------------------------------------------------------

## Current progress update - 04/08/2024

CatChat-GPT-2 Training a GPT2 model using google colab. This was the only way I can accomplish a working model of
medium sized without having to spend money. This is ideal when thinking about success rate.

<https://colab.research.google.com/drive/1qRIMC8DTDykc_BXSnSDvtZrLM5kxG-zn?usp=sharing>

I also am working on my own .txt file which may sound like it would be easy. It is easy but very time consuming. You
need a large amount of data to have a valid working GPT. When I say valid I mean easy to follow responses from the GPT. 

----------------------------------------------------------------

## Current progress update - 04/02/2024

Will be on the look for a GPT-2 sized model using PyTorch!

----------------------------------------------------------------

## Milestone 3 - 03/29/2024

This is the link to my 5 minute milestone 3 video

<https://www.youtube.com/watch?v=Q3HmhYu4dtE&ab_channel=IIRII>

----------------------------------------------------------------

## Current progress update - 03/27/2024

I am trying to decide if I should revert to a smaller model so I can have a working final project. I believe there is to much debugging to accomplish a large model with my OWN implemented code.

I will still be working on a LLM until the 31st before I make my decision on reverting to a smaller model or continuing to attempt the large model (LLM).

----------------------------------------------------------------

## Current progress update - 03/26/2024

ran into many issues when trying to put everything together the training code using Pytorch Lightning.

Will have to create my own training code from scratch it seems. I will explain thoroughly in my upcoming 5 minute milestone 3 video.

----------------------------------------------------------------

## Current progress update - 03/21/2024

Added the offocial Pytorch Lightning code.

<https://github.com/Lightning-AI>

----------------------------------------------------------------

## Current progress update - 03/20/2024

Adding a DeepSpeed try out GPT sample. It is not visible unless you download the code. They have it set up within the github page for DeepSpeed and anyone can try and set up the sample on their own computer.

Turns out I was right about $$$ money becoming an issue. As of right now I would have to pay to train my AI if I were to use DeepSpeed. I would have to look to see if their is any free LLM (Might be SOL)

----------------------------------------------------------------

## Current progress update - 03/17/2024

Successfully downloaded DeepSpeed using WSL(Ubunutu) in Visual Studio Code. Finally got around the biggest issue I have ran into so far in my project! Hopefully I can start moving at "Lightning" speed now!

![DeepSpeed Successful](https://github.com/CIDS-484-Spring-2024/ChatCat-GPT/assets/117781469/25736c5f-712f-4916-b286-7e21d3d0d71e)

I wanted to point out the DeepSpeed (<https://github.com/microsoft/DeepSpeed>) is programmed by Microsoft but not support by Windows OS. I am unsure why they don't have support for their code on their own systems (Unless it is a marketing thing . . . That would be my only logical assumption).

----------------------------------------------------------------

## Current progress update - 03/16/2024

Looks like I have found the work around for the issue that I ran into with DeepSpeed! You install something called WSL which is short for "Windows Subsystem for Linux". DeepSpeed has zero support and can not run on Windows as of right now unfortunately.

here is the windows offocial website where you can learn more - <https://learn.microsoft.com/en-us/windows/wsl/install>

I am currently in progress of implementing the work around. Will update later or next update if it was successful.

----------------------------------------------------------------

## Current progress update - 03/12/2024

DeepSpeed was added THIS IS AN INVISIBLE FILE. You must download the code in order to access the DeepSpeed folder.

Even better. Just go to this Github page and see it for yourself - <https://github.com/microsoft/DeepSpeed>

Currently working to resolve this issue.
(Windows 11 has an issue with newer version of python and a package. Many many many blogs about this issue which is directly connected to Pytorch Lightning and installing the DeepSpeed package)

I am going to attempt a LLM/NN "Large Language Model" which was suggested in a peer review from milestone 1.

I will be using to learn about LLM using PyTorch Lightning.

Tons of code high level code is introduced and explained in the below links.

How to build a chatbot using open-source LLMs like Llama 2 and Falcon
<https://lightning.ai/pages/community/tutorial/how-to-build-a-chatbot-using-open-source-llms-like-llama-2-and-falcon/>

Scaling Large (Language) Models with PyTorch Lightning - Lightning AI
<https://lightning.ai/blog/scaling-large-language-models-with-pytorch-lightning/>

Using Lightning with DeepSpeed - (<https://github.com/microsoft/DeepSpeed>)

<https://lightning.ai/docs/pytorch/stable/advanced/model_parallel.html#deepspeed>

Here is the offocial site!
<https://www.deepspeed.ai/>

----------------------------------------------------------------

## Milestone 2 - 03/01/2024

This is the link to my 5 minute milestone 2 video - <https://www.youtube.com/watch?v=0rmQ_D9AQlY&ab_channel=IIRII>

----------------------------------------------------------------

## Current progress update - 02/26/2024

A big part of GPTs is Neural Networks and what you use to train those Neural Networks. Python has a training library of it's own called and known as "Lightning"
which is something created in "PyTorch" so it got the name "PyTorch Lightning".
Following is one of a few videos I am watching about this specific part of my project (Neural Network)

Word Embedding in PyTorch + Lightning for the python language.
<https://youtu.be/Qf06XDYXCXI>

----------------------------------------------------------------

## Current progress update - 02/24/2024

Currently learning exactly how the "Transformer" neural network works.
Python for example has something called "Lightning" or Pytorch Lightning.
Once I completely understand this part I will find out if I can create a functioning Transformer neural network without having to spend $

----------------------------------------------------------------

## Current progress update - 02/20/2024

added the GPTtrainingsample folder. This folder has python code (use kernel 3.12.1 to make it work when it asks which environment to use)
This code takes the input.txt file which is a list of cat names. It then creates its own
list of names that are unique and different from the 10000+ names on the input.txt file

You can do this on your own computer using VS code. (you can replace the input.txt file with your own.

----------------------------------------------------------------

## Current progress update - 02/17/2024

adding a tokenizer called tiktoken. I believe this is the best option for python based AIs. I still am learning all of the requirements to make an AI run so my first milestone video may not have been very clear. My outline was still accurate but it is a ton of learning and I am unsure if I will be able to complete the project by semesters end.

I do feel confident in having a working model of some sort accomplished. Hopefully before milestone 2

----------------------------------------------------------------
## Milestone 1

This is the link to my 5 minute milestone 1 video
<https://www.youtube.com/watch?v=ORlQ82_WnYo&ab_channel=IIRII>

----------------------------------------------------------------
