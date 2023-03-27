import json

mock_file = 'backend/api/mock_data.json'

def get_mock_data():
    """
    Load mock data from a JSON file.

    Returns:
        dict: A dictionary containing the mock data.
    """
    with open(mock_file, 'r') as file:
        data = json.load(file)
        return data

def save_mock_data(data):
    """
    Save mock data to a JSON file.

    Args:
        data (dict): A dictionary containing the data to save.
    """
    with open(mock_file, 'w') as file:
        json.dump(data, file)

def get_task_index(tasks, id):
    """
    Find the index of a task in a list of tasks with the given ID.

    Args:
        tasks (list): A list of dictionaries, where each dictionary represents a task.
        id (int): The ID of the task to find.

    Returns:
        int: The index of the task in the `tasks` list, or `None` if the task is not found.
    """
    for i, task in enumerate(tasks):
        if task['id'] == id:
            return i
   
