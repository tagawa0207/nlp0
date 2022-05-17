from django.shortcuts import render
from .models import OriginalText, SummaryText
from .forms import LangForm
from transformers import AutoModelWithLMHead, AutoTokenizer, AutoModelForSeq2SeqLM
import spacy

def deldup_jp(text):
    ginza = spacy.load("ja_ginza")
    sents = [sent.text for sent in ginza(text).sents]
    sents = list(dict.fromkeys(sents))
    return "".join(sents)

def index(request):

    original_text = ""
    summary_text = ""

    if request.POST:

        if "original_text" in request.POST:
            original_text = request.POST["original_text"]
            lang_form = LangForm(request.POST)
            if lang_form.is_valid():
                which_lang = request.POST["which_lang"]

            fine_tuned_model = "./run_summarization_saved" if which_lang == "japanese" else "t5-base"

            tokenizer = AutoTokenizer.from_pretrained(fine_tuned_model)
            model = AutoModelForSeq2SeqLM.from_pretrained(fine_tuned_model)

            inputs = tokenizer.encode("summarize:" + original_text, return_tensors="pt", truncation=False)
            summary_ids = model.generate(inputs, max_length=2048, num_beams=20, early_stopping=False)
            generate_text = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]
            
            summary_text = deldup_jp(generate_text[0]) if which_lang == "japanese" else generate_text[0]
        else:
            summary_text = original_text
        
        return render(request, 'nlp0/index.html', {'original_text':original_text, 'summary_text':summary_text, 'lang_form': lang_form})

    return render(request, 'nlp0/index.html', {'original_text':original_text, 'summary_text':summary_text, 'lang_form': LangForm()})
