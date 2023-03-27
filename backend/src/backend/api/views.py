from django.http import JsonResponse
import json
from .utils import get_mock_data, save_mock_data, get_task_index
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_task(request, id):
    """
    Retrieve a record with the specified ID from the list of records.

    Args:
        id (int): The ID of the record to retrieve.
        records (list): A list of records to retrieve the record from.

    Returns:
        dict: A dictionary containing the record data, or None if the record is not found.
    """
    tasks = get_mock_data()['tasks']
    index = get_task_index(tasks, id)
    if index is not None:
        data = tasks[index]
        return JsonResponse(data, safe=False)
    return JsonResponse({"error": "Task not found"})

@csrf_exempt
def add_task(request):
    """
    This function creates a new record in the database using the `create` method
    provided by Django's object-relational mapper (ORM).

    Args:
        data (dict): A dictionary containing data for the new record.

    Returns:
        int: The ID of the newly created record.
    """
    data = json.loads(request.body)
    tasks = get_mock_data()['tasks']
    task = {"id": len(tasks)+1, **data}
    tasks.append(task)
    save_mock_data({"tasks": tasks})
    return JsonResponse(task)

@csrf_exempt
def delete_task(request, id):

    """
    Delete a record with the specified ID from the list of records.

    Args:
        id (int): The ID of the record to delete.
        records (list): A list of records to delete the record from.

    Returns:
        bool: Returns True if the deletion was successful, False otherwise.
    """
    
    tasks = get_mock_data()['tasks']
    index = get_task_index(tasks, id)
    if index is not None:
        tasks.pop(index)
        save_mock_data({"tasks": tasks})
        return JsonResponse({"success": True}, safe=False)
    return JsonResponse({"error": "Task not found","success":False})

@csrf_exempt
def update_task(request, id):
    
    """
    Update an existing record in the list of records.

    Args:
        id (int): The ID of the record to update.
        data (dict): A dictionary containing the updated data for the record.
        records (list): A list of records to update the record in.

    Returns:
         bool: Returns True if the deletion was successful, False otherwise.
    """
    
    data = json.loads(request.body)
    tasks = get_mock_data()['tasks']
    index = get_task_index(tasks, id)
    if index is not None:
        tasks[index].update(data)
        save_mock_data({"tasks": tasks})
        return JsonResponse({"success": True}, safe=False)
    return JsonResponse({"error": "Task not found","success":False}, safe=False)

def search_task(request, term):
    
    """
    Search a list of records for a given search term.

    Args:
        term (str): The term to search for. Case-insensitive.
        records (list): The list of records to search.

    Returns:
        list: A list of dictionaries containing the records that match the search term.
    """
    
    tasks = get_mock_data()['tasks']
    filtered_tasks = [task for task in tasks if term.lower() in task['title'].lower()]
    return JsonResponse({"tasks": filtered_tasks}, safe=False)


def get_all_tasks(request):
    """
    Retrieve all records from the list of records.

    Args:
        records (list): A list of records to retrieve all records from.

    Returns:
        list: A list of dictionaries containing the records data.
    """
    data =  get_mock_data()['tasks']
    return JsonResponse(data, safe=False)