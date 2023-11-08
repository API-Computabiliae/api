# importando as bibliotecas que serão utilizadas
import openai
import PyPDF2
import os
from read_pdf.settings import SECRET_KEY

#essa função serve para dividirmos o nosso pdf, e ficar mais fácil de procurar as respostas 
def chunk_pdf(pdf_file, limit=4000, overlap=1):
    chunks = []
    chunk = ""
    with open(pdf_file, "rb") as f:
        pdf = PyPDF2.PdfReader(f)
        for page in pdf.pages:
            chunk += page.extract_text()
            while len(chunk) > limit:
                chunks.append(chunk[:limit])
                chunk = chunk[limit -overlap:]
    if len(chunk):
        chunks.append(chunk)

    return chunks

#essa função vai achar as palavras chaves nas chucks do pdf
def find_matches(chunks, keywords, padding=500):
    df = {}
    results = {}

    trimmed_chunks = []
    for i, chunk in enumerate(chunks):
        if i != 0:
            chunk = chunk[padding:]
        if i != len(chunks):
            chunk = chunk[:-padding]
        trimmed_chunks.append(chunk.lower())

    for chunk in trimmed_chunks:
        for keyword in keywords:
            occurences = chunk.count(keyword)
            if keyword not in df:
                df[keyword] = 0
            df[keyword] += occurences
    
    for chunk_id, chunk in enumerate(trimmed_chunks):
        points = 0
        for keyword in keywords:
            occurences = chunk.count(keyword)
            if occurences > 0:
                points += occurences / df[keyword]
        results[chunk_id] = points

    return dict(results.items(), key=lambda item: item[1], reverse=True)

#com as chunks necessárias, vamos obter as nossas repostas
def answer_question(chunk, question):
    openai.api_key = SECRET_KEY 

    prompt = f"""```
    {chunk}
    ```

    Baseado nas informações acima, qual é a resposta para essa questão?

    ```	
    {question}
    ```"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["choices"][0]["message"]["content"]
