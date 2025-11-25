import chainlit as cl
from chainlit.types import AskFileResponse
from agent import agent
from utils import extract_text_from_pdf
from agents import Runner, Agent
from openai.types.responses import ResponseTextDeltaEvent

@cl.on_chat_start
async def start():
    """
    Initializes the chat interface and sends a welcome message.
    Prompts the user to upload a PDF file.
    """
    await cl.Message(
        content="Hello! Upload a PDF to get started. I will summarize it for you."
    ).send()

    files = None
    while files is None:
        files = await cl.AskFileMessage(
            content="Please upload a PDF file to begin!",
            accept=["application/pdf"],
            max_size_mb=20,
            timeout=180,
        ).send()

    pdf_file = files[0]
    
    # Store the file path in the user session
    cl.user_session.set("pdf_file_path", pdf_file.path)

    await cl.Message(
        content=f"Processing `{pdf_file.name}`..."
    ).send()

    # Extract text and store in session
    pdf_text = extract_text_from_pdf(pdf_file.path)
    cl.user_session.set("original_pdf_text", pdf_text)

    # Indicate processing and start streaming the summary
    response_message = cl.Message(content="📄 Analyzing your PDF...\n\n**Summary:**\n", author="PDF Assistant")
    await response_message.send()

   
    result = Runner.run_streamed(agent, input=f"Summarize the following PDF text: {pdf_text}")

    final_answer = ""
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            token = event.data.delta
            if token:
                await response_message.stream_token(token)
                final_answer += token
        elif event.type == "run_item_stream_event":
            if event.item.type == "tool_call_item":
                              pass
            elif event.item.type == "tool_call_output_item":
       
                pass
    
    await response_message.update()
    
    # After summary, ask about quiz
    await cl.Message(
        content="Would you like me to create a quiz from this content? Type 'Create Quiz' or click the button below.",
        actions=[
            cl.Action(name="create_quiz_button", label="Create Quiz", on_action=handle_quiz_request)
        ]
    ).send()


@cl.on_message
async def main(message: cl.Message):
    """
    Handles incoming messages from the user.
    Recognizes "Create Quiz" to generate a quiz.
    """
    if message.content.lower().strip() == "create quiz":
        await handle_quiz_request()
    else:
        await cl.Message(content="Please upload a PDF or type 'Create Quiz' to get questions from the last PDF.").send()


@cl.action_callback("create_quiz_button")
async def handle_quiz_request(action: cl.Action = None):
    """
    Handles the request to create a quiz.
    """
    original_pdf_text = cl.user_session.get("original_pdf_text")
    if not original_pdf_text:
        await cl.Message(content="Please upload a PDF first to generate a quiz.").send()
        return

    await cl.Message(content="📝 Generating quiz questions...", author="PDF Assistant").send()

    
    quiz_message = cl.Message(content="**Quiz:**\n", author="PDF Assistant")
    await quiz_message.send()

   
    result = Runner.run_streamed(agent, input=f"Generate a multiple choice quiz with at least 5 questions, each with 4 options (A, B, C, D), and clearly mark the correct answer. Use the following text: {original_pdf_text}")
    
    final_quiz = ""
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            token = event.data.delta
            if token:
                await quiz_message.stream_token(token)
                final_quiz += token
        elif event.type == "run_item_stream_event":
            if event.item.type == "tool_call_item":
        
                pass
            elif event.item.type == "tool_call_output_item":
                pass
    
    await quiz_message.update()

    await cl.Message(content="Quiz generated!").send()
