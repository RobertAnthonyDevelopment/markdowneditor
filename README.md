# Markdown Reader/Editor

## Overview

This is a simple graphical Markdown Reader/Editor built using Python's `tkinter` library. The application allows users to write Markdown, convert it into HTML, and view the rendered HTML in real-time. Users can also open and save files, making this a useful tool for Markdown-based content creation. 


## Features

- **Markdown Editor**: A text area where users can write or edit Markdown text.
- **HTML Preview**: A side-by-side HTML output area to view the rendered HTML from Markdown in real-time.
- **File Operations**: Options to **View** and **Edit** (not **Open**) Markdown files and **Save** the HTML output.
- **User-friendly Interface**: The interface uses scrollable text areas and buttons for easy Markdown editing and previewing.

## Requirements

- Python 3.x
- `tkinter` (usually pre-installed with Python)
- `markdown` module

To install the `markdown` module, run:
```bash
pip install markdown
```

## Installation and Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/RobertAnthonyDevelopment/markdowneditor.git
    ```

2. Install the dependencies:
    ```bash
    pip install markdown
    ```

3. Run the application:
    ```bash
    python markdown_editor.py
    ```

## How to Use

1. **Writing Markdown**: On the left side, you can write Markdown syntax in the text area.
2. **Rendering HTML**: Click the "Render" button to convert the Markdown into HTML. The rendered HTML will appear in the right-side text area.
3. **File Menu**: 
    - **Save File**: Save the HTML output to an HTML file.
    - **Open File**: Ignore this Function Copy and Paste existing MD documents into Left Pane
## Example

1. Write this Markdown in the left text area:
   ```
   # Welcome
   This is an **example** of a Markdown document.
   ```
   
2. Click "Render" and the HTML output will be:
   ```html
   <h1>Welcome</h1>
   <p>This is an <strong>example</strong> of a Markdown document.</p>
   ```

3. You can save this HTML output using the "Save" option from the file menu.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
