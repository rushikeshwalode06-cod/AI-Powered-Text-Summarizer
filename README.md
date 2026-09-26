# 🤖 AI-Powered Text Summarizer

An **AI-powered text summarization application** that automatically converts long text into concise and meaningful summaries using a fine-tuned **T5-Small Transformer model**.

---

## 🚀 Project Overview

The **AI-Powered Text Summarizer** uses Natural Language Processing (NLP) and Transformer-based deep learning to understand lengthy text and generate a shorter summary while preserving the important information.

The model is trained using the **BillSum dataset** and the **Google T5-Small** pretrained model.

---

## ✨ Features

* 📝 Long text summarization
* 🤖 AI-powered automatic summarization
* ⚡ Fast summary generation
* 🧠 Transformer-based NLP model
* 📚 BillSum dataset
* 📊 ROUGE-based evaluation
* 🤗 Hugging Face integration
* 🎯 Concise and meaningful summaries
* 🎨 User-friendly interface

---

## 🛠️ Technologies Used

* 🐍 Python
* 🤗 Hugging Face Transformers
* 🧠 T5-Small
* 📚 Hugging Face Datasets
* 📊 ROUGE Score
* 🔥 PyTorch
* 🎨 Streamlit
* 🔧 Accelerate
* 🔢 NumPy

---

## 🧠 Model

### T5-Small

This project uses the pretrained **Google T5-Small** Transformer model.

T5 (Text-to-Text Transfer Transformer) treats NLP tasks as text-to-text problems. For summarization, the input text is provided with the prefix:

```text
summarize:
```

The model then generates a concise summary of the input text.

---

## 📚 Dataset

### BillSum Dataset

The model is trained using the **BillSum dataset**, which contains U.S. Congressional and California state bills along with their summaries.

Dataset:

```text
dany0407/billsum
```

The California test split was used and divided into training and testing portions.

---

## 🔄 Project Workflow

```text
Dataset Collection
       ↓
Data Preprocessing
       ↓
Text Tokenization
       ↓
T5-Small Model
       ↓
Model Training
       ↓
ROUGE Evaluation
       ↓
Model Testing
       ↓
Hugging Face Model
       ↓
Generate Summary
```

---

## ⚙️ Data Preprocessing

The input documents are prepared using the T5 tokenizer.

The model input follows the format:

```text
summarize: <input text>
```

The tokenizer processes:

* Input documents
* Target summaries
* Maximum input length
* Maximum summary length
* Truncation

The input sequence length is limited to **1024 tokens**, while generated labels are limited to **128 tokens**.

---

## 🏋️ Model Training

The T5-Small model is fine-tuned using the Hugging Face `Seq2SeqTrainer`.

### Training Configuration

| Parameter             | Value       |
| --------------------- | ----------- |
| Model                 | T5-Small    |
| Learning Rate         | 2e-5        |
| Train Batch Size      | 16          |
| Evaluation Batch Size | 16          |
| Weight Decay          | 0.01        |
| Epochs                | 10          |
| Evaluation            | Every Epoch |
| Precision             | FP16        |
| Generation            | Enabled     |

---

## 📊 Model Evaluation

The model performance is evaluated using **ROUGE (Recall-Oriented Understudy for Gisting Evaluation)**.

Evaluation metrics include:

* ROUGE-1
* ROUGE-2
* ROUGE-L
* Generated Length

ROUGE compares the generated summary with the reference summary to evaluate how well the model captures important information.

---

## 🤗 Hugging Face Model

After training, the model was uploaded to Hugging Face for easy access and reuse.

**Model:** `rushikeshwalode/summarization_model`

---

## 🎯 Applications

This AI summarization system can be useful for:

* 📰 News summarization
* 📄 Document summarization
* 📚 Research paper summarization
* 🏛️ Legal document summarization
* 📑 Report summarization
* 📧 Long email summarization
* 📖 Educational content summarization

---

## 🔮 Future Improvements

* 🚀 Improve summarization quality with larger Transformer models
* 📄 Add PDF document summarization
* 📑 Add DOCX file summarization
* 🌍 Support multiple languages
* ⚡ Optimize inference speed
* 🎨 Improve Streamlit UI
* 📊 Add summary length controls
* 🔊 Add text-to-speech for generated summaries
* ☁️ Deploy the application online

---

## 🧠 Skills Demonstrated

* Python Programming
* Natural Language Processing
* Deep Learning
* Transformer Models
* Text Summarization
* T5 Fine-Tuning
* Tokenization
* Hugging Face Transformers
* Hugging Face Datasets
* Model Evaluation
* ROUGE Score
* Streamlit
* Model Deployment

---

## 🏆 Conclusion

The **AI-Powered Text Summarizer** demonstrates how Transformer-based NLP models can be used to automatically summarize long-form text.

By combining **T5-Small, BillSum, Hugging Face Transformers, ROUGE evaluation, and Streamlit**, this project provides an end-to-end AI text summarization solution.
