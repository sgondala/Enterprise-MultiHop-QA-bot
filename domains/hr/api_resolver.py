from langchain.agents.tools import BaseTool
from domains.hr.apis.api_registry import HR_FUNCTION_REGISTRY

from domains.hr.apis import custom_apis, merge_apis

class HRAPIResolverTool(BaseTool):
    name = "HRAPIResolver"
    description = """This tool is used to call different HR related APIs. The APIs and their descriptions are defined as follows:

    {}

    Input should be the function name, followed by ';', followed by arguments separated by commas. 
    For example, if you want to get the number of employees under a person first_name last_name, say "get_employees_under_manager; first_name, last_name"
    If you want to get employee list, say "get_employee_list" as it doesn't have any arguments.

    Make sure your string contains all the information that is needed by the function in the right format.
    """ 

    def fill_description(self) -> None:
        """
        Fills description based on the HR_FUNCTION_REGISTRY
        """
        description_of_all_functions = ""

        for key in HR_FUNCTION_REGISTRY:
            function_name = key
            docstring = HR_FUNCTION_REGISTRY[key]['docstring']
            description_of_all_functions += "Function Name: " + function_name + "\n"
            description_of_all_functions += "Docstring: " + docstring + "\n\n"
        
        self.description = self.description.format(description_of_all_functions)

    def __init__(self) -> None:
        super().__init__()
        self.fill_description()
        
    def _run(self, query: str) -> str:
        # get_employees_under_manager; Sashank, Gondala
        print("\n Query to HR API resolver - ", query)
        query = query.split(";")
        function_name = query[0].strip()

        if function_name in HR_FUNCTION_REGISTRY:
            function = HR_FUNCTION_REGISTRY[function_name]['function']
            # module = HR_FUNCTION_REGISTRY[function_name]['module']
            args = query[1].strip().split(",")
            args = [arg.strip() for arg in args]
            # print("Calling function ", function_name, " with args ", args)
            return function(*args)

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("Does not support async")
    
if __name__ == '__main__':
    tool = HRAPIResolverTool()
    print(tool.description)