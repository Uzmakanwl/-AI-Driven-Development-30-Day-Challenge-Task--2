# GEMINI.md - Build Study Notes Summarizer & Quiz Generator Agent

## 🎯 Mission
You are tasked with building a **PDF Summarizer & Quiz Generator Agent** using:
- **OpenAgents SDK** with Gemini 2.5 Flash model
- **Chainlit** for the web interface
- **PyPDF** for PDF text extraction

---

## 📋 Pre-Flight Checklist

Before writing ANY code, complete these steps:

### 1. Research Phase (Use Context7 MCP Tools)
```
Search and understand:
- OpenAgents SDK documentation (initialization, tool binding, streaming)
- Chainlit documentation (file upload, message handlers, streaming responses)
- PyPDF usage for text extraction
- Best practices for Gemini model prompting
- How to structure agent tools properly
```


### 2. Environment Setup
```
Check if these packages exist:
- chainlit
- openai-agents (OpenAgents SDK)
- pypdf
- python-dotenv

Only install missing packages using: uv add <package-name>
```

---

## 🏗️ Implementation Instructions

### Phase 1: Project Structure
Create this exact file structure:
```
project/
├── .env                 # API keys (GEMINI_API_KEY)
├── agent.py            # Agent configuration & tool setup
├── utils.py            # PDF text extraction helper
├── app.py              # Chainlit UI and event handlers
├── pyproject.toml      # Dependencies
└── README.md           # Usage instructions
```

---

### Phase 2: Build Core Components

#### A. PDF Text Extraction (`utils.py`)
```python
# Create a simple, robust PDF text extractor
# Requirements:
# - Function name: extract_text_from_pdf(file_path)
# - Use PyPDF's PdfReader
# - Return full text as string
# - Handle empty pages gracefully
# - No unnecessary error handling
```

#### B. Agent Configuration (`agent.py`)
```python
# Research using Context7 MCP, then implement:
# 1. Initialize Gemini client with gemini-2.5-flash model
# 2. Load API key from .env
# 3. Create two agent tools:
#    - SummarizerTool: Takes PDF text, returns structured summary
#    - QuizGeneratorTool: Takes PDF text, generates MCQs
# 4. Set system prompt:
"""
You are an AI study assistant that helps students learn.

When a user uploads a PDF:
1. Extract and summarize the content in clear, structured format
2. Wait for user to request a quiz
3. Generate quiz questions from the ORIGINAL PDF text (not the summary)
4. Create MCQs with 4 options each, clearly mark correct answers
5. Stream all responses progressively
"""
```

#### C. Chainlit UI (`app.py`)
```python
# Implement these exact handlers:

@cl.on_chat_start
# Send welcome message: "Hello! Upload a PDF to get started."

@cl.on_message
# Handle two scenarios:
# 1. PDF Upload Detected:
#    - Call extract_text_from_pdf()
#    - Pass text to SummarizerTool
#    - Stream summary back to UI
#    - Show "Create Quiz" button/prompt
# 
# 2. "Create Quiz" Request:
#    - Retrieve original PDF text (store in session)
#    - Call QuizGeneratorTool with ORIGINAL text
#    - Stream quiz questions to UI
#    - Format questions clearly (numbering, options A-D)
```

---

### Phase 3: Configuration Files

#### `.env`
```
GEMINI_API_KEY=your_actual_api_key_here
```

#### `pyproject.toml`
```toml
[project]
name = "pdf-quiz-agent"
version = "0.1.0"
requires-python = ">=3.11"

dependencies = [
    "chainlit",
    "openai-agents",
    "pypdf",
    "python-dotenv"
]
```

---

## 🎯 Critical Requirements

### Zero-Bloat Protocol
- **ONLY** implement: PDF summarization and quiz generation
- **NO** extra features like:
  - Multiple file formats
  - User authentication
  - Database storage
  - Advanced error handling beyond basic checks

### MCP Research Mandate
Before implementing ANY feature:
1. Use Context7 MCP to search official documentation
2. Verify syntax and method signatures
3. Check for best practices
4. Confirm the feature is actually supported

### Tool Implementation Rules
- SummarizerTool: Generates concise, structured summary (use headings, bullet points)
- QuizGeneratorTool: 
  - Minimum 5 MCQs
  - 4 options per question (A, B, C, D)
  - Clearly indicate correct answer
  - Questions cover different sections of PDF

### Streaming Requirements
- All agent responses MUST stream progressively to Chainlit UI
- Use Chainlit's `cl.Message(content="...").send()` pattern
- Show typing indicators where appropriate

---

## 🧪 Testing Checklist

After implementation, verify:
1. ✅ PDF uploads successfully
2. ✅ Summary appears within 10 seconds
3. ✅ Summary is well-structured (not a wall of text)
4. ✅ "Create Quiz" functionality works
5. ✅ Quiz has 5+ questions with proper formatting
6. ✅ Quiz is based on ORIGINAL PDF (not the summary)
7. ✅ Responses stream progressively
8. ✅ No crashes on empty or malformed PDFs

---

## 🚀 Execution Flow

```
Step 1: Research ALL components using Context7 MCP
        ↓
Step 2: Create file structure
        ↓
Step 3: Implement utils.py (PDF extraction)
        ↓
Step 4: Implement agent.py (Gemini + tools)
        ↓
Step 5: Implement app.py (Chainlit handlers)
        ↓
Step 6: Configure .env and pyproject.toml
        ↓
Step 7: Test with sample PDF
        ↓
Step 8: Iterate based on test results
```

---

## 📝 Example Interaction Flow

```
User: *uploads research_paper.pdf*

Agent: "📄 Analyzing your PDF..."
       [Streams summary progressively]
       
       "**Summary:**
       
       **Introduction**
       - Key point 1
       - Key point 2
       
       **Methods**
       - Approach used
       - Data sources
       
       **Results**
       - Finding 1
       - Finding 2
       
       Would you like me to create a quiz from this content?"

User: "Yes, create a quiz"

Agent: "📝 Generating quiz questions..."
       
       "**Quiz: Research Paper**
       
       **Question 1:** What was the primary research method used?
       A) Survey analysis
       B) Experimental design
       C) Case study
       D) Meta-analysis
       
       ✅ Correct Answer: B
       
       **Question 2:** ..."
```

---

## ⚠️ Common Pitfalls to Avoid

1. ❌ Generating quiz from summary instead of original PDF
2. ❌ Not streaming responses (showing all at once)
3. ❌ Hardcoding API keys in code
4. ❌ Adding features not in requirements
5. ❌ Not using Context7 MCP for documentation research
6. ❌ Installing packages without checking if they exist

---

## 🎓 Success Criteria

Your agent is complete when:
- [ ] A non-technical user can upload a PDF and get a summary
- [ ] The quiz accurately reflects PDF content
- [ ] All responses stream smoothly
- [ ] Code follows the zero-bloat protocol
- [ ] Documentation research was thorough
- [ ] No unnecessary dependencies

---

**NOW BEGIN:** Start with Context7 MCP research on OpenAgents SDK (openai-agents) initialization. Do not write any code until you've researched all components.