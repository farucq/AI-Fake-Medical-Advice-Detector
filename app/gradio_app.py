import gradio as gr

from utils.classification import classify_advice
from utils.severity_detection import detect_severity
from rag.retrieval import retrieve_medical_knowledge
from utils.explanation_generator import generate_explanation

def gradio_interface(text):

    classification, confidence = classify_advice(text)
    severity = detect_severity(text)
    knowledge = retrieve_medical_knowledge(text)
    explanation = generate_explanation(text, knowledge)

    confidence_percent = f"{confidence*100:.2f}%"

    knowledge_text = "\n".join([f"• {k}" for k in knowledge])

    return (
        classification,
        confidence_percent,
        severity,
        knowledge_text,
        explanation
    )

with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("# AI Fake Medical Advice Detector")

    input_text = gr.Textbox(
        label="Enter Medical Advice",
        placeholder="Example: Drinking lemon water cures cancer"
    )

    analyze_btn = gr.Button("Analyze Advice")

    with gr.Row():
        classification_output = gr.Textbox(label="Classification")
        confidence_output = gr.Textbox(label="Confidence Score")
        severity_output = gr.Textbox(label="Risk Level")

    knowledge_output = gr.Textbox(label="Retrieved Knowledge")
    explanation_output = gr.Textbox(label="Explanation")

    analyze_btn.click(
        fn=gradio_interface,
        inputs=input_text,
        outputs=[
            classification_output,
            confidence_output,
            severity_output,
            knowledge_output,
            explanation_output
        ]
    )

demo.launch()
