import tkinter as tk
from tkinter import messagebox
from app.ocr import capture_and_extract_text
from app.translator import translate_text
from app.tts import speak_text

def start_gui():
    root = tk.Tk()
    root.title("Screen Translator")
    root.geometry("400x300")

    def process():
        try:
            extracted_text = capture_and_extract_text(
                hide_window_callback=root.withdraw,
                show_window_callback=root.deiconify
            )
            translated = translate_text(extracted_text)
            speak_text(translated)
            output_box.delete(1.0, tk.END)
            output_box.insert(tk.END, translated)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            root.deiconify()  # fallback თუ exception მოხდა

    btn = tk.Button(root, text="Translate Screen Text", command=process)
    btn.pack(pady=20)

    output_box = tk.Text(root, wrap=tk.WORD, height=10)
    output_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    root.mainloop()
