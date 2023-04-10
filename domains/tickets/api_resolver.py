from langchain.agents.tools import BaseTool
from domains.tickets.apis.api_registry import TICKET_FUNCTION_REGISTRY
from domains.tickets.apis import merge_apis # Need this import to register functions

class TicketAPIResolverTool(BaseTool):
    name = "TicketAPIResolverTool"
    description = """This tool is used to call different Ticketing related APIs. The APIs and their descriptions are defined as follows:

    {}

    Input should be the function name, followed by ';', followed by arguments separated by commas. 
    For example, if you want to get the number of comments per ticket, say "get_number_of_comments_per_ticket; <ticket_id>"

    Make sure your string contains all the information that is needed by the function in the right format.
    """ 

    def fill_description(self) -> None:
        """
        Fills description based on the TICKET_FUNCTION_REGISTRY
        """
        description_of_all_functions = ""

        for key in TICKET_FUNCTION_REGISTRY:
            function_name = key
            docstring = TICKET_FUNCTION_REGISTRY[key]['docstring']
            description_of_all_functions += "Function Name: " + function_name + "\n"
            description_of_all_functions += "Docstring: " + docstring + "\n\n"
        
        self.description = self.description.format(description_of_all_functions)

    def __init__(self) -> None:
        super().__init__()
        self.fill_description()
        
    def _run(self, query: str) -> str:
        print("\n Query to Ticket API resolver - ", query)
        query = query.split(";")
        function_name = query[0].strip()

        if function_name in TICKET_FUNCTION_REGISTRY:
            function = TICKET_FUNCTION_REGISTRY[function_name]['function']
            args = query[1].strip().split(",")
            args = [arg.strip() for arg in args]
            return function(*args)        

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("Does not support async")
    
if __name__ == '__main__':
    tool = TicketAPIResolverTool()
    print(tool.description)