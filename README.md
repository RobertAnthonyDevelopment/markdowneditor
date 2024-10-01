# Markdown Reader/Editor

## Overview

This is a simple graphical Markdown Reader/Editor built using Python's `tkinter` library. The application allows users to write Markdown, convert it into HTML, and view the rendered HTML in real-time.

## Features

- **Markdown Editor**: A text area where users can write or edit Markdown text.
- **HTML Preview**: A side-by-side HTML output area to view the rendered HTML from Markdown in real-time.
- **File Operations**: Options to **View** and **Edit** (not **Open**) Markdown files and **Save** the HTML output.
- **User-friendly Interface**: The interface uses scrollable text areas and buttons for easy Markdown editing and previewing.

## Requirements

- Python 3.10 or Higher
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
    - **Open File**: Ignore this function. Copy and paste existing MD documents into the left pane.

## Optional: How to Create an Executable (.exe)

If you're working on macOS and want to create an executable, you can use `PyInstaller`. This step is optional and not required for running the application on your system.

### Steps to Create an Executable:

1. Install `PyInstaller`:
    ```bash
    pip install pyinstaller
    ```

2. Open your terminal and navigate to the project directory:
    ```bash
    cd markdowneditor
    ```

3. Run the following command to create a standalone executable:
    ```bash
    pyinstaller --onefile markdown_editor.py
    ```

    - The `--onefile` option ensures that all required files are bundled into a single executable.

4. After the process completes, the executable will be located in the `dist` directory:
    - On macOS, the app will be inside this `dist` folder. You can run it by navigating to the folder and opening the executable file.

5. **Run the Executable**: 
   - Navigate to the `dist` directory and double-click the generated executable file to launch the app.

### Note:
- This step is entirely optional. You can run the application using Python without creating an executable.

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
