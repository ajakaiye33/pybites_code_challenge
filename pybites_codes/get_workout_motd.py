workout_schedule = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}


def get_workout_motd(day):
    """Title case passed in day argument (monday or MONDAY -> Monday)
       and check if it is in the given workout_schedule dict.

       If it is there retrieve the workout, if not raise a KeyError.

       Return the chill or go_train variable depending the retrieved
       workout value ('Rest' or workout bla)

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'"""
    day = day.title()
    rest, chill, go_train = 'Rest', 'Chill out!', 'Go train {}'.format(workout_schedule[day])
    day in workout_schedule.keys()
    v = workout_schedule[day]
    if v == rest:
        return chill
    else:
        return go_train


print(get_workout_motd('Sunday'))
