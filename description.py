#!/usr/bin/env python
# coding: utf-8

#importing necessary libraries
from transformers import GPT2Tokenizer,TFGPT2LMHeadModel

#enter directory where model and tokenizer are saved
output_dir='saved_model/'

#load the saved tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained(output_dir)
model = TFGPT2LMHeadModel.from_pretrained(output_dir)


#function to generate medicine description	
def generate_text(input_text):
    # encoding the input text
    input_ids = tokenizer.encode(input_text, return_tensors='tf')


    #getting out output ids with use of sampling techniques
    output = model.generate(
    input_ids,do_sample=True,
      temperature=0.7,
      top_p = 0.85,
      max_length=500,
      top_k = 50)
    #decoding the generated ids into text to produce result
    result=tokenizer.decode(output[0],skip_special_tokens=True)
    return result


#importing the gradio library for deployment
import gradio as gr
#deploying the model in interface generated by gradio
#on entering input and clicking submit the model will generate description
output_text = gr.outputs.Textbox()
gr.Interface(generate_text,"textbox", output_text, title="Medicine Description System",
             description="It generates short description about any medicine by use of OpenAI's GPT-2 \
              when any input in form of medicine name or medicine details given to it.",allow_flagging=False).launch()

