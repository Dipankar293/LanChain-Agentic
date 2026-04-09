
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI


# Basic agent creation
agent_basic = create_agent("openai:gpt-5")

basic_response = agent_basic.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in NE India"}]}
)

print("FULL RESPONSE:", basic_response)

#Customised agent creation (ChatAnthropic, ChatGoogleGenerativeAI)
model = ChatOpenAI(
    model="gpt-5",
    temperature=0.9,
    max_tokens=10000,
    timeout=30
)

agent_custom_model = create_agent(model)

response = agent_custom_model.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in NE India"}]}
)


#get the content of the last message in the response
print("FULL RESPONSE:", response["messages"][-1].content)

#get the token usage of the last message in the response
print("TOKEN USAGE:", response["messages"][-1].response_metadata["token_usage"])

#get the message id of the last message in the response
print("MESSAGE ID:", response["messages"][-1].response_metadata["id"])
