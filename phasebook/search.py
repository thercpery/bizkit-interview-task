import re
from flask import Blueprint, request
from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    
    results = []
    parameters = ['id', 'name', 'age', 'occupation']
    for parameter in parameters:
        if parameter in args:
            for user in USERS:
                if user not in results:
                    if type(user[parameter]) == str:
                        regexFormat = f"({args[parameter].lower()})"
                        result = re.findall(regexFormat, user[parameter].lower())
                        if len(result) > 0:
                            results.append(user)
                    if type(user[parameter]) == int:
                        if user[parameter] == int(args[parameter]) or user[parameter] == int(args[parameter]) + 1 or user[parameter] == int(args[parameter]) - 1: 
                            results.append(user)

    return results
