from datetime import date

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from fake_data_app import create_app

store_dict = create_app()
app = FastAPI()


@app.get("/")
def visit(
    store_name: str, year: int, month: int, day: int, sensor_id: int | None = None
):
    # If the store is not in the dictionary
    if not (store_name in store_dict.keys()):
        return JSONResponse(status_code=404, content="Store Not found")

    # Check the value of sensor_id
    if sensor_id and (sensor_id > 7 or sensor_id < 0):
        return JSONResponse(
            status_code=404, content="Sensor_id should be between 0 and 7"
        )

    # Check the year
    if year < 2019:
        return JSONResponse(status_code=404, content="No data before 2019")

    # Check the date
    try:
        date(year, month, day)
    except TypeError:
        return JSONResponse(status_code=404, content="Enter a valid date")

    # Check the date is in the past
    if date.today() < date(year, month, day):
        return JSONResponse(status_code=404, content="Choose a date in the past")

    # If no sensor choose return the visit for the whole store
    if sensor_id is None:
        visit_counts = store_dict[store_name].get_all_traffic(date(year, month, day))
    else:
        visit_counts = store_dict[store_name].get_sensor_traffic(
            sensor_id, date(year, month, day)
        )

    if visit_counts < 0:
        return JSONResponse(
            status_code=404, content="The store was closed try another date"
        )

    return JSONResponse(status_code=200, content=visit_counts)
