from langchain.agents import AgentType, initialize_agent
from langchain.agents.tools import BaseTool
from langchain.llms import OpenAI

from domains.hr.api_resolver import HRAPIResolverTool


class HRExecutorTool(BaseTool):
    name = "HRExecutor"
    description = """This is a tool dedicated to a company's HR. 
    This tool can do the things like get the list of employees in the company, list of employees under a person X, number of groups in the company, compensation of a person X, etc 
    Input to this tool should be a string which describes what you want to do. 
    For example, if you want to get the number of employees under a person X, say "Number of employees under X"  
    If you want to get list of people under X, say "List of employees under X"
    If you want to get the compensation of a person X, say "Compensation of X" and so on.
    Make sure your string contains all the information that is needed to get the result.
    """

    def _run(self, query: str) -> str:
        print("\n Query to HR Domain Executor - ", query)
        tools = [HRAPIResolverTool()]
        llm = OpenAI(temperature=0)
        agent = initialize_agent(
            tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
        )
        return agent.run(query)

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("Does not support async")
