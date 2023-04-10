# File containing the APIs that we wrote in addition to merge.dev apis

from domains.hr.apis.api_registry import register_hr_api

@register_hr_api
def get_employees_under_manager(manager_first_name, manager_last_name):
    """
    Returns the list of employees under the manager

    Args:
        manager_first_name (str): First name of the manager
        manager_last_name (str): Last name of the manager

    Returns:
        List[str]: List of employees in the format "First Name, Last Name"
    """
    if manager_first_name == "Sashank" and manager_last_name == "Gondala":
        return [
            "Alfred, Hitchcock", 
            "Steven, Spielberg", 
            "James, Cameron", 
            "Christopher, Nolan", 
            "Quentin, Tarantino"
        ]
    else:
        assert False, "Manager not found"
