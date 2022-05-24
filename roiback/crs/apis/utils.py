import datetime


# def validate_date(date_text):
#     try:
#         datetime.datetime.strptime(date_text, '%Y-%m-%d')
#     except ValueError:
#         raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def validate_date(date_text):
    try:
        response = datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    return response


def check_type(variable):
    if type(variable) != int and type(variable) != float:
        raise ValueError("Incorrect data type")
