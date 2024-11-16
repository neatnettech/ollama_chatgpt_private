# Variables
PYTHON := python3  # Use the appropriate Python version
SCRIPTS_DIR := scripts
DATA_DIR := chatgpt_export
CONVERSATIONS_DIR := $(DATA_DIR)/conversations
PREPARED_DATA_DIR := $(DATA_DIR)/prepared_data

# Targets
.PHONY: all clean extract export

# Default target: Run both scripts
all: extract export

# Step 1: Extract prompts
extract:
	@echo "Running extract_prompts.py..."
	$(PYTHON) $(SCRIPTS_DIR)/extract_prompts.py --input $(DATA_DIR)/conversations.json --output $(PREPARED_DATA_DIR)/prompts.jsonl
	@echo "Prompts extracted to $(PREPARED_DATA_DIR)/prompts.jsonl."

# Step 2: Export to conversations
export:
	@echo "Running export_to_conversations.py..."
	$(PYTHON) $(SCRIPTS_DIR)/export_to_conversations.py --input $(PREPARED_DATA_DIR)/prompts.jsonl --output $(CONVERSATIONS_DIR)/formatted_conversations.jsonl
	@echo "Conversations exported to $(CONVERSATIONS_DIR)/formatted_conversations.jsonl."

# Clean up generated files
clean:
	@echo "Cleaning up generated files..."
	rm -rf $(PREPARED_DATA_DIR)/*.jsonl $(CONVERSATIONS_DIR)/formatted_conversations.jsonl
	@echo "Cleanup complete."