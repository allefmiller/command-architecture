import schedule
import time
from database import execute_sql

def atualizar_produtos_dpa():
    execute_sql("EXEC sp_AtualizaDPA")

schedule.every().day.at("05:00").do(atualizar_produtos_dpa)

while True:
    schedule.run_pending()
    time.sleep(1)