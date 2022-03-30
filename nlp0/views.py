from django.shortcuts import render
from .models import OriginalText, SummaryText
#from transformers import AutoModelWithLMHead, AutoTokenizer
import os
import sys


def index(request):

    original_text = ""
    summary_text = ""
    deb = "hello"

    if request.POST:
        deb = "hello"
        if "original_text" in requet.POST:
            original_text = request.POST["original_text"]

            tokenizer = AutoTokenizer.from_pretrained("t5-base")
            model = AutoModelWithLMHead.from_pretrained("t5-base")
            inputs = tokenizer.encode("summarize:" + original_text, return_tensors="pt", truncation=True)
            summary_ids = model.generate(inputs, max_length=200, num_beams=4, early_stopping=True)
            generate_text = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]
            
            summary_text = generate_text[0]
        else:
            summary_text = original_text
        
        return render(request, 'nlp0/index.html', {'original_text':original_text, 'summary_text':summary_text, 'deb':deb})

    return render(request, 'nlp0/index.html', {'original_text':original_text, 'summary_text':summary_text, 'deb':deb})
    # original_text = OriginalText.objects.order_by('-date')[:5]
    # summary_text = SummaryText.objects.order_by('-date')[:5]
    # context = {'original_text': original_text, 'summary_text': summary_text}
    # return render(request, 'nlp0/index.html', context)

