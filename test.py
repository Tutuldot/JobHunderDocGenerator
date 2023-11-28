from transformers import AutoTokenizer
import transformers
import torch

model = "meta-llama/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)


print("Staring app:")


sequences = pipeline(
    'can you make a cover letter for a software engineer?',
    do_sample=True,
    top_k=4,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=1000,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")

print(sequences)