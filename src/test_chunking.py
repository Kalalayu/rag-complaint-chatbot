from src.chunking import chunk_text

print("🚀 test_chunking started")

text = "This is a long complaint text. " * 50
chunks = chunk_text(text)

print("Number of chunks:", len(chunks))
print("First chunk:")
print(chunks[0])

print("✅ test_chunking finished")
