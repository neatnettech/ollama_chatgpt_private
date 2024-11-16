import json
import os

file_path = 'chatgpt_export/conversations.json'
output_dir = 'chatgpt_export/conversations'

os.makedirs(output_dir, exist_ok=True)

with open(file_path, 'r') as file:
    data = json.load(file)


for conversation in data:
    title = conversation.get("title", "Untitled").replace("/", "-").replace("\\", "-")
    mapping = conversation.get("mapping", {})
    messages = []

    for message_id, message_data in mapping.items():
        message = message_data.get("message")
        if message:
            role = message.get("author", {}).get("role", "unknown").capitalize()
            

            parts = message.get("content", {}).get("parts", [])
            content = " ".join(
                part["text"] if isinstance(part, dict) and "text" in part else str(part)
                for part in parts
            )
            
            messages.append(f"{role}:\n{content}\n")


    conversation_text = "\n".join(messages)


    output_file = os.path.join(output_dir, f"{title}.txt")
    with open(output_file, 'w') as output:
        output.write(conversation_text)

print(f"Conversations saved to '{output_dir}'")