import os

INPUT_DIR = "data/cleaned_docs"
OUTPUT_DIR = "data/chunks"
# make output folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 150 words per chunk - smaller version for the chunk size
CHUNK_SIZE = 150  
# go through each cleaned doc and split into chunks
for file_name in os.listdir(INPUT_DIR):
    # skip anything that's not a txt file 
    if not file_name.endswith(".txt"):
        continue

    # read the file and split into words
    
    with open(os.path.join(INPUT_DIR, file_name), "r", encoding="utf-8") as f:
        words = f.read().split()

    chunk_count = 0

    for i in range(0, len(words), CHUNK_SIZE):
        chunk_words = words[i:i + CHUNK_SIZE]
        chunk_text = " ".join(chunk_words)
        # name format: OriginalDoc.txt_chunk_0.txt, _chunk_1.txt, etc.
        chunk_file = f"{file_name}_chunk_{chunk_count}.txt"
        chunk_path = os.path.join(OUTPUT_DIR, chunk_file)

        with open(chunk_path, "w", encoding="utf-8") as f:
            f.write(chunk_text)

        chunk_count += 1

print("150-word chunking complete.")
