#The simplest way to create a tool is with the @tool decorator. 
#By default, the function’s docstring becomes the tool’s description that helps the model understand when to use it:

from langchain.tools import tool

@tool
def search_database(query: str, limit: int = 10) -> str:
    """Search the customer database for records matching the query.

    Args:
        query: Search terms to look for
        limit: Maximum number of results to return
    """
    return f"Found {limit} results for '{query}'"


#Custom tool name
#Override the tool name when you need something more descriptive

@tool("web_search")  # Custom name
def search(query: str) -> str:
    """Search the web for information."""
    return f"Results for: {query}"

print(search.name)  # web_search

#Custom tool description
#Override the auto-generated tool description for clearer model guidance

@tool("calculator", description="Performs arithmetic calculations. Use this for any math problems.")
def calc(expression: str) -> str:
    """Evaluate mathematical expressions."""
    return str(eval(expression))