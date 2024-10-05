import gradio as gr

def calculate_height(width, aspect_ratio):
    ratio = float(aspect_ratio.split(':')[0]) / int(aspect_ratio.split(':')[1])
    height = round(width / ratio)
    return height

def main():
    interface = gr.Interface(
        fn=calculate_height,
        inputs=[gr.Number(label="Breite/Höhe"), gr.Textbox(label="Seitenverhältnis (z.B. 16:9, 9:16)")],
        outputs=gr.Number(label="Breite/Höhe"),
        title="Seitenverhältnis-Rechner",
        description="Geben Sie die Breite und das Seitenverhältnis ein, um die Breite/Höhe zu berechnen."
    )
    interface.launch()

if __name__ == "__main__":
    main()