from datetime import datetime





def get_earliest_v_2_0(date_string_1, date_string_2):
    date_1 = datetime.strptime(date_string_1, '%m/%d/%y')
    date_2 = datetime.strptime(date_string_2, '%m/%d/%y')
    if date_1 >= date_2:
        return date_string_1
    else:
        return date_string_2


def get_earliest_v_3_0(*dates_strings):
    def get_earliest_v_1_0(date_1, date_2):
        mm_1, dd_1, yyyy_1 = date_1.split('/')
        mm_2, dd_2, yyyy_2 = date_2.split('/')
        if (yyyy_1,mm_1,dd_1) < (yyyy_2,mm_2,dd_2):
            return date_1
        else:
            return date_2

    i_earliest = 0
    for i_new_date_sring, new_date_string in enumerate(dates_strings[1:]):
        print(str(i_new_date_sring)+") Comparo(" + str(dates_strings[i_earliest]) + ", " + str(new_date_string) + ")")
        if get_earliest_v_1_0(dates_strings[i_earliest], new_date_string) == new_date_string:
            print("\tMenor: "+str(new_date_string)+" Cambio el minimo por:" +str(dates_strings[i_new_date_sring+1]))
            i_earliest = i_new_date_sring+1
        else:
            print("\tMenor: " + str(dates_strings[i_earliest]))

    return dates_strings[i_earliest]


def get_earliest(*dates_strings):
    def get_earliest_v_1_0(date_1, date_2):
        mm_1, dd_1, yyyy_1 = date_1.split('/')
        mm_2, dd_2, yyyy_2 = date_2.split('/')
        if (yyyy_1,mm_1,dd_1) < (yyyy_2,mm_2,dd_2):
            return date_1
        else:
            return date_2

    i_earliest = 0
    for i_new_date_sring, new_date_string in enumerate(dates_strings[1:]):
        if get_earliest_v_1_0(dates_strings[i_earliest], new_date_string) == new_date_string:
            i_earliest = i_new_date_sring+1

    return dates_strings[i_earliest]
