# Document Generator

## Purpose

The Document Generator is a Flask-based web application designed to help users generate structured document outlines and diagrams based on input text. It leverages Azure OpenAI for natural language processing to create structured outlines and diagrams automatically.

## Functionalities

1. **Outline Generation** - Users can input raw text, and the application processes it to generate a structured document outline.
2. **Diagram Generation** - Based on the generated outline, users can select a diagram type (flowchart, sequence diagram, class diagram, etc.) to visualize their content.
3. **Download Options** - Users can download the generated outline as a `.docx` Word document.

## Technologies Used

- **Flask** - Backend framework for handling API requests and rendering the frontend.
- **Azure OpenAI** - Utilized for processing and generating text-based outlines and diagrams.
- **Mermaid.js** - For rendering diagrams dynamically in the frontend.
- **HTML, CSS, JavaScript** - For the frontend interface.
- **Python & OpenAI API** - Backend logic and AI-powered responses.

## Installation & Setup

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- pip (Python package manager)
- A valid Azure OpenAI API Key
- Virtual environment (optional but recommended)

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd document-generator
   ```
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up Azure OpenAI configuration**
   - Create a `.env` file in the project root and add the following:
     ```ini
     AZURE_OPENAI_API_KEY=your-api-key
     AZURE_OPENAI_API_BASE=your-api-url
     AZURE_OPENAI_ENGINE=your-engine-name
     ```
5. **Run the Flask application**
   ```bash
   python app.py
   ```
6. **Access the application**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## API Endpoints

1. **Home Page**

   - `GET /`
   - Renders the `index.html` page.

2. **Generate Outline**

   - `POST /outline`
   - Input: `{ "outline": "User input text" }`
   - Output: `{ "result": "Generated structured outline" }`

3. **Generate Diagram**

   - `POST /generate-diagram`
   - Input: `{ "type": "flowchart", "instructions": "optional", "outline": "previously generated outline" }`
   - Output: `{ "result": "Mermaid.js formatted diagram" }`

4. **Download Outline as Word File**

   - `POST /download`
   - Input: `{ "content": "Markdown content" }`
   - Output: `.docx` file download

## Usage

1. **Enter text** - Input your content in the text area.
2. **Generate Outline** - Click the "Generate Outline" button.
3. **Generate Diagram** - Select a diagram type and generate.
4. **Download Outline** - Click "Download Outline" to save it as a Word file.

## Troubleshooting

- Ensure your `.env` file is correctly set up with the Azure OpenAI API key.
- If the application fails to start, check for missing dependencies and install them using `pip install -r requirements.txt`.
- Verify that the Flask application is running on the correct port.
