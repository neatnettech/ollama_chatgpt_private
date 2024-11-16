import json
import os

file_path = 'chatgpt_export/conversations.json'
output_dir = 'chatgpt_export/prepared_data'


os.makedirs(output_dir, exist_ok=True)


with open(file_path, 'r') as file:
    data = json.load(file)


prepared_data = []

for conversation in data:
    mapping = conversation.get("mapping", {})


    conversation_pairs = []
    for message_id, message_data in mapping.items():
        message = message_data.get("message")
        if message:
            role = message.get("author", {}).get("role", "unknown").capitalize()


            parts = message.get("content", {}).get("parts", [])
            content = " ".join(
                part["text"] if isinstance(part, dict) and "text" in part else str(part)
                for part in parts
            )

            conversation_pairs.append({"role": role, "content": content})


    for i in range(len(conversation_pairs) - 1):
        if conversation_pairs[i]["role"] == "User" and conversation_pairs[i + 1]["role"] == "Assistant":
            prompt = conversation_pairs[i]["content"]
            response = conversation_pairs[i + 1]["content"]
            prepared_data.append({"prompt": prompt, "response": response})


output_file = os.path.join(output_dir, 'fine_tuning_data.jsonl')
with open(output_file, 'w') as output:
    for item in prepared_data:
        output.write(json.dumps(item) + '\n')

print(f"Fine-tuning data saved to '{output_file}'")