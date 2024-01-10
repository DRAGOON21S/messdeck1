import json as json

def load_menu_data():
    with open('messdeck/mess menu/asdf.json') as f :
        data= json.load(f)
    from datetime import datetime
    from .models import Date, breakfast,lunch,dinner

    # for date, date_dict in data.items():
    #     breakfast_items = date_dict["BREAKFAST"]
    #     print(f"{date:}")
    #     for item in breakfast_items:
    #         print(f"{item}")




    for date_str, date_dict in data.items():
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        date_obj, created = Date.objects.get_or_create(date=date)

        breakfast_items = date_dict["BREAKFAST"]
        for item in breakfast_items:
            breakfast.objects.get_or_create(date=date_obj, name=item)

        lunch_items = date_dict["LUNCH"]
        for item in lunch_items:
            lunch.objects.get_or_create(date=date_obj, name=item)

        dinner_items = date_dict["DINNER"]
        for item in dinner_items:
            dinner.objects.get_or_create(date=date_obj, name=item)