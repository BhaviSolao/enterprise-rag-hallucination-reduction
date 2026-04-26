import os

# paths
INPUT_DIR = "data/parsed_docs"
OUTPUT_DIR = "data/chunks"


CHUNK_SIZE = 300      # words
OVERLAP = 50          # words

os.makedirs(OUTPUT_DIR, exist_ok=True)

def chunk_text(text):
    # split into words
    words = text.split()
    chunks = []
    start = 0
    # sliding window with overlap
    while start < len(words):
        end = start + CHUNK_SIZE
        chunk = words[start:end]
        chunks.append(" ".join(chunk))
        start += CHUNK_SIZE - OVERLAP

    return chunks
# loop through cleaned docs
for file in os.listdir(INPUT_DIR):
    if file.endswith(".txt"):
        with open(os.path.join(INPUT_DIR, file), "r", encoding="utf-8") as f:
            text = f.read()

        chunks = chunk_text(text)
         # save each chunk
        for i, chunk in enumerate(chunks):
            out_file = f"{file.replace('.txt','')}_chunk_{i}.txt"
            with open(os.path.join(OUTPUT_DIR, out_file), "w", encoding="utf-8") as out:
                out.write(chunk)

print("Chunking complete.")
