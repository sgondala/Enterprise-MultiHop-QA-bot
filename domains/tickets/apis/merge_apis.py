# File containing all the APIs from merge.dev

from domains.tickets.apis.api_registry import register_ticket_api


@register_ticket_api
def get_number_of_tickets_per_employee(
    employee_first_name: str, employee_last_name: str
) -> int:
    """
    Returns the number of tickets per employee

    Args:
        employee_first_name (str): First name of the employee
        employee_last_name (str): Last name of the employee

    Returns:
        int: Number of tickets per employee
    """
    if employee_first_name == "Sashank" and employee_last_name == "Gondala":
        return 10
    elif employee_first_name == "Alfred" and employee_last_name == "Hitchcock":
        return 5
    elif employee_first_name == "Steven" and employee_last_name == "Spielberg":
        return 2
    elif employee_first_name == "James" and employee_last_name == "Cameron":
        return 3
    elif employee_first_name == "Christopher" and employee_last_name == "Nolan":
        return 1
    elif employee_first_name == "Quentin" and employee_last_name == "Tarantino":
        return 4
    else:
        assert False, "Employee not found"


@register_ticket_api
def get_number_of_comments_per_ticket(ticket_id: str) -> int:
    """
    Returns the number of comments per ticket

    Args:
        ticket_id (str): Ticket ID

    Returns:
        int: Number of comments per ticket
    """
    return 0
