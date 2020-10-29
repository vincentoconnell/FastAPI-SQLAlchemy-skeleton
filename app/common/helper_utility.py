import datetime


def validate_date(str_date_time) -> bool:
    try:

        date_time_obj = datetime.datetime.strptime(str_date_time, '%Y-%m-%d %H:%M:%S')

        if date_time_obj != datetime.datetime.strptime(str_date_time, '%Y-%m-%d %H:%M:%S'):
            raise ValueError
        return True
    except ValueError:
        return False
