# AI Fake Medical Advice Detector

## Overview

AI Fake Medical Advice Detector is an NLP-based healthcare project that analyzes health-related text and determines whether the advice is **medically correct or misinformation**.

The system uses **medical entity recognition, transformer-based classification, and knowledge retrieval (RAG)** to evaluate health claims and provide explanations.

---

## Features

* Detects **medical misinformation**
* Extracts **medical entities** from text
* Uses **AI models for classification**
* Retrieves **relevant medical knowledge**
* Provides **AI-generated explanations**
* Detects **high-risk medical advice**
* Interactive **Gradio web interface**

---

## Technologies Used

* Python
* HuggingFace Transformers
* SciSpaCy
* Sentence Transformers
* FAISS (Vector Search)
* Gradio (UI)
* Google Colab

---

## Project Structure

```
ai-fake-medical-advice-detector
│
├── app
│   └── gradio_app.py
│
├── models
│   └── load_models.py
│
├── nlp
│   ├── preprocessing.py
│   └── entity_detection.py
│
├── rag
│   ├── knowledge_base.py
│   └── retrieval.py
│
├── utils
│   ├── classification.py
│   ├── severity_detection.py
│   └── explanation_generator.py
│
├── requirements.txt
└── README.md
```

---

## Installation

Install required packages:

```
pip install -r requirements.txt
```

Install SciSpaCy medical model:

```
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_sm-0.5.4.tar.gz
```

---

## Run the Application

Start the Gradio interface:

```
python app/gradio_app.py
```

The web interface will open in your browser.

---

## Example Input

```
Drinking lemon water cures cancer completely
```

### Output

* Classification: **Misinformation**
* Confidence Score
* Risk Level
* Retrieved Medical Knowledge
* AI Explanation

---

## Future Improvements

* Use advanced medical models (BioBERT / MedGemma)
* Expand medical knowledge base
* Improve severity detection
* Deploy as a public web application

---

## License

This project is for educational and research purposes.
