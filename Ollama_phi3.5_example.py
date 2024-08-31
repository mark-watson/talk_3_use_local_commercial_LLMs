import ollama

def query_file(query, file_path, model='llama3.1'):
  print(f"\nquery: {query}\tfile_path: {file_path}\tmodel: {model}")
  text = open(file_path, 'r').read()
  prompt = f"Answer this question:\n\n{query}\n\ngiven this text:\n\n{text}\n\nAnswer:"

  response = ollama.chat(
    model=model,
    messages=[{'role': 'user', 'content': prompt }],)
  r = response['message']['content'] 
  return r

print(f"\n{query_file('Who says that economics is bullshit?',
                      'economics.txt',
                      model='phi3.5')}")
# note: phi3.5activate has a 128K context window