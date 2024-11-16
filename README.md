
# ChatGPT Data Preparation and Fine-Tuning Pipeline

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow.svg)](https://huggingface.co/)

A project to extract, preprocess, and fine-tune datasets for large language models like CodeQwen using ChatGPT data.

---

## Project Structure

```plaintext
.
├── Makefile                       # Automates tasks like data extraction and export
├── README.md                      # Project documentation
├── chatgpt_export/                # Directory containing exported ChatGPT data
│   ├── conversations/             # Individual conversations in plain text
│   ├── conversations.json         # Exported conversations
│   ├── prepared_data/             # Processed data for fine-tuning
│   └── ...                        # Other exported metadata
├── notebooks/                     # Jupyter notebooks for fine-tuning
│   └── fine_tune_codeqwen.ipynb   # Notebook for fine-tuning CodeQwen
└── scripts/                       # Python scripts for data preparation
    ├── export_to_conversations.py # Converts extracted data into conversational format
    └── extract_prompts.py         # Extracts prompts from ChatGPT data
```

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Required Python packages (install via `requirements.txt`):
  ```bash
  pip install -r requirements.txt
  ```
- Exported data from ChatGPT, or any other training data

### How to Use

1. **Extract Prompts**:
   Run the `extract_prompts.py` script to extract prompts from ChatGPT-exported data:
   ```bash
   make extract
   ```

2. **Export to Conversations**:
   Format the extracted prompts into a conversational format:
   ```bash
   make export
   ```

3. **Fine-Tune**:
   Use the formatted data to fine-tune a large language model. Refer to `notebooks/fine_tune_codeqwen.ipynb` for detailed steps.

4. **Clean Up**:
   Remove intermediate and output files:
   ```bash
   make clean
   ```

---

## License

This project is licensed under the MIT License.

---

## Contributing

We welcome contributions! Feel free to open an issue or submit a pull request.


Once I get my GPU, this will accelerate !

---

## Acknowledgments

- [unsloth](https://github.com/unslothai/unsloth)
- [Unsloth notebook](https://colab.research.google.com/drive/1mvwsIQWDs2EdZxZQF9pRGnnOvE86MVvR?usp=sharing#scrollTo=MKX_XKs_BNZR)