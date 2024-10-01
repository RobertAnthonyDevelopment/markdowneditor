import tkinter as tk
from tkinter import scrolledtext, messagebox
import markdown

class MarkdownEditor:
    def __init__(self, master):
        self.master = master
        master.title("Markdown Reader/Editor")
        master.geometry("800x600")

        # Create the text area for editing Markdown
        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=20)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a button to render the Markdown
        self.render_button = tk.Button(master, text="Render", command=self.render_markdown)
        self.render_button.pack(side=tk.BOTTOM)

        # Create a text area for displaying rendered HTML
        self.output_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=20)
        self.output_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Menu Bar
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

    def render_markdown(self):
        # Get the text from the Markdown editor
        markdown_text = self.text_area.get("1.0", tk.END)

        # Convert Markdown to HTML
        html = markdown.markdown(markdown_text)

        # Clear the output area and insert the rendered HTML
        self.output_area.delete("1.0", tk.END)
        self.output_area.insert(tk.END, html)

    def save_file(self):
        try:
            with open("output.html", "w") as f:
                f.write(self.output_area.get("1.0", tk.END))
            messagebox.showinfo("Info", "File saved as output.html")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def open_file(self):
        try:
            with open("example.md", "r") as f:
                content = f.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    editor = MarkdownEditor(root)
    root.mainloop()
