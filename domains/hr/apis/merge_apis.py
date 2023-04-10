# File containing all the APIs from merge.dev

from domains.hr.apis.api_registry import register_hr_api


@register_hr_api
def get_employee_list():
    """
    Returns the list of employees

    Returns:
        List[str]: List of employees in the format "First Name, Last Name"
    """
    return ""


@register_hr_api
def get_employee_compensation(employee_first_name, employee_last_name):
    """
    Returns the compensation of the employee

    Args:
        employee_first_name (str): First name of the employee
        employee_last_name (str): Last name of the employee

    Returns:
        str: Compensation of the employee
    """
    return ""
