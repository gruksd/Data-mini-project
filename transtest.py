from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-fi-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-fi-en")

# Input text in Finnish
text_to_translate = "Tämä on esimerkki suomenkielisestä tekstistä."

# Tokenize the input text
input_ids = tokenizer.encode(text_to_translate, return_tensors="pt", max_length=512, truncation=True)

# Perform translation
translated_ids = model.generate(input_ids, max_length=512, num_beams=4, length_penalty=0.6, early_stopping=True)

# Decode and print the translation
translated_text = tokenizer.decode(translated_ids[0], skip_special_tokens=True)

print("Finnish Input: ", text_to_translate)
print("English Translation: ", translated_text)
