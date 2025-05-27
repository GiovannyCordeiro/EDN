from datetime import datetime

# calculo da idade em dias
def age_cal(birth_date: str) -> int:
    birth_date_calendar = datetime.strptime(birth_date, '%d-%m-%Y').date()
    data_atual = datetime.now().date()
    age_days = (data_atual - birth_date_calendar).days
    return age_days

print(age_cal('08-01-2003'))
print(age_cal('03-05-2000'))