from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

from domains.hr.executor import HRExecutorTool
from domains.tickets.executor import TicketExecutorTool

# Loading env variables like OpenAI key, merge dev key, etc.
from dotenv import load_dotenv
load_dotenv()

tools = [HRExecutorTool(), TicketExecutorTool()]

llm = OpenAI(temperature=0)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

query = "How many tickets combined are assigned to all the employees under Sashank Gondala?"

print("Query - ", query)

agent.run(query)
