

#Dynamic model

#Dynamic models are selected at runtime based on the current state and context. 
# This enables sophisticated routing logic and cost optimization.

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse


basic_model = ChatOpenAI(model="gpt-4.1-mini")
advanced_model = ChatOpenAI(model="gpt-4.1")

@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    """Choose model based on conversation complexity."""
    message_count = len(request.state["messages"])

    if message_count > 2:
        # Use an advanced model for longer conversations
        model = advanced_model
        print("🔁 Switching to ADVANCED model")
    else:
        model = basic_model
        print("⚡ Using BASIC model")


    return handler(request.override(model=model))

agent = create_agent(
    model=basic_model,  # Default model
    middleware=[dynamic_model_selection]
)

response = agent.invoke({
    "messages": [
        {"role": "user", "content": "Hi"}
    ]
})

response = agent.invoke({
    "messages": [
        {"role": "user", "content": "Hi"},
        {"role": "assistant", "content": "Hello!"},
        {"role": "user", "content": "Explain quantum mechanics"}
    ]
})

#Decorators

# @before_agent
# @before_model
# @after_model
# @after_agent
# @wrap_model_call
# @wrap_tool_call
# @dynamic_prompt