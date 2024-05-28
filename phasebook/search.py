import re
from flask import Blueprint, request
from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    print(request.args.to_dict())
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
    for user in USERS:
        for key, value in args.items():
            if type(user[key]) == str:
                regexFormat = f"({value.lower()})"
                result = re.findall(regexFormat, user[key].lower())
                if len(result) > 0:
                    results.append(user)
            if type(user[key]) == int and user[key] == int(value):
                results.append(user)

    return results
