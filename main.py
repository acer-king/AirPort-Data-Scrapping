from DataOutputMgr import DataOutputMgr as DOMgr
from DataSourceMgr import DataSourceMgr as DSMgr
from DataUtil import DataUtil as DUtil
from datetime import datetime
from sqlite3 import OperationalError
from time import sleep


def main():
    dsmgr = DSMgr()
    rows = dsmgr.getDatasFromTable()
    results = []
    for row in rows:
        date, time, city_name, _ = tuple(row)[0:4]
        if not time:
            continue
        datetimeobj = datetime.strptime(date + " " + time, '%d.%m.%Y %H:%M')
        temp = DUtil.get_temperature_from_city_name(city_name=city_name)
        note = DUtil.get_note_from_temperature(temp)
        results.append((city_name, datetimeobj, temp, note))
        if(temp is None):
            continue
    # update database with this results.
    domgr = DOMgr()
    for row in results:
        try:
            domgr.upsert(row)
            sleep(5)
        except OperationalError as err:
            print(err)
        except ValueError as err:
            print(err)
        finally:
            pass
    domgr.commit()


if __name__ == "__main__":
    main()
