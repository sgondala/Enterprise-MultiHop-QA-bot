from langchain.agents.tools import BaseTool
from domains.tickets.api_resolver import TicketAPIResolverTool
from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain.agents import initialize_agent

class TicketExecutorTool(BaseTool):
    name = "TicketExecutor"
    description = """This is a tool dedicated to answering questions about a company's ticketing system
    This tool can do the things like the number of open tickets in the company, the number of tickets assigned to a person X, number of projects within a company, etc
    Input to this tool should be a string which describes what you want to do.
    For example, if you want to get the number of open tickets in the company, say "Number of open tickets"
    If you want to get the number of tickets assigned to a person X, say "Number of tickets assigned to X" and so on
    Make sure your string contains all the information that is needed to get the result.
    """
    
    def _run(self, query: str) -> str:
        print("\n Query to Ticket Domain executor - ", query)
        tools = [TicketAPIResolverTool()]
        llm = OpenAI(temperature=0)
        agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
        return agent.run(query)

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("Does not support async")
