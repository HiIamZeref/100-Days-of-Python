from datetime import datetime, timedelta


today = datetime.today()

later = (today + timedelta(180)).strftime("%d/%m/%Y")

print(today.strftime("%d/%m/%Y"))
print(later)