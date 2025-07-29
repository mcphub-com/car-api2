import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/carapi/api/car-api2'

mcp = FastMCP('car-api2')

@mcp.tool()
def vindecoder(vin: Annotated[str, Field(description='')]) -> dict: 
    '''Decodes Vehicle Identification Numbers. The result will include a list of specifications in the specs property and a list of all possible trims matching the VIN in the trims property. For non-paying users, all VINs for 2015-2020 models (e.g. 1GTG6CEN0L1139305) will be returned, otherwise data is hidden. Paying users have full data access.'''
    url = 'https://car-api2.p.rapidapi.com/api/vin/1GTG6CEN0L1139305'
    headers = {'x-rapidapi-host': 'car-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'vin': vin,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def years(model: Annotated[Union[str, None], Field(description='')] = None,
          make_id: Annotated[Union[str, None], Field(description='')] = None,
          trim: Annotated[Union[str, None], Field(description='')] = None,
          year: Annotated[Union[str, None], Field(description='')] = None,
          make: Annotated[Union[str, None], Field(description='')] = None,
          make_model_id: Annotated[Union[str, None], Field(description='')] = None,
          json: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''For complex queries you may use the json field to send an array of URL encoded JSON conditions, example: `[{"field": "make", "op": "in", "val": ["Scion", "Tesla"]}]` Allowed operators are: `>`, `<`, `>=`, `<=`, `in`, `not in`, `like`, `not like`, `is null` and `not null`. Allowed search fields are: `year`, `make`, `model`, `trim`, `make_id`, and `make_model_id`.'''
    url = 'https://car-api2.p.rapidapi.com/api/years'
    headers = {'x-rapidapi-host': 'car-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'model': model,
        'make_id': make_id,
        'trim': trim,
        'year': year,
        'make': make,
        'make_model_id': make_model_id,
        'json': json,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def makes(limit: Annotated[Union[int, float, None], Field(description='')] = None,
          page: Annotated[Union[int, float, None], Field(description='')] = None,
          direction: Annotated[Union[str, None], Field(description='')] = None,
          sort: Annotated[Union[str, None], Field(description='')] = None,
          make: Annotated[Union[str, None], Field(description='')] = None,
          year: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Search makes by name and year.'''
    url = 'https://car-api2.p.rapidapi.com/api/makes'
    headers = {'x-rapidapi-host': 'car-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'page': page,
        'direction': direction,
        'sort': sort,
        'make': make,
        'year': year,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def models(make: Annotated[Union[str, None], Field(description='')] = None,
           limit: Annotated[Union[int, float, None], Field(description='')] = None,
           model: Annotated[Union[str, None], Field(description='')] = None,
           sort: Annotated[Union[str, None], Field(description='')] = None,
           page: Annotated[Union[int, float, None], Field(description='')] = None,
           direction: Annotated[Union[str, None], Field(description='')] = None,
           year: Annotated[Union[str, None], Field(description='')] = None,
           verbose: Annotated[Union[str, None], Field(description='Includes make, model and trim')] = None,
           make_id: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Search models by year, make, model, trim or make_id. To include the models make in the description request with the query parameter as `verbose=yes`. For complex queries you may use the json field to send an array of URL encoded JSON conditions, example: `[{"field": "make", "op": "in", "val": ["Ford", "Acura"]}, {"field": "year", "op": ">=", "val": 2010}] Allowed json operators are: =, !=, >, <, >=, <=, in, not in, like, not like, not null, and is null. Allowed json search fields are: year, make, model, make_id, created, and modified.'''
    url = 'https://car-api2.p.rapidapi.com/api/models'
    headers = {'x-rapidapi-host': 'car-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'make': make,
        'limit': limit,
        'model': model,
        'sort': sort,
        'page': page,
        'direction': direction,
        'year': year,
        'verbose': verbose,
        'make_id': make_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def trims(limit: Annotated[Union[int, float, None], Field(description='')] = None,
          direction: Annotated[Union[str, None], Field(description='')] = None,
          sort: Annotated[Union[str, None], Field(description='')] = None,
          year: Annotated[Union[str, None], Field(description='')] = None,
          model: Annotated[Union[str, None], Field(description='')] = None,
          page: Annotated[Union[int, float, None], Field(description='')] = None,
          trim: Annotated[Union[str, None], Field(description='')] = None,
          make_model_id: Annotated[Union[str, None], Field(description='')] = None,
          verbose: Annotated[Union[str, None], Field(description='Includes make, model and trim')] = None,
          make_id: Annotated[Union[str, None], Field(description='')] = None,
          make: Annotated[Union[str, None], Field(description='')] = None,
          json: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''To include additional information about the returned body (such as year, make, model and trim) request with the query parameter as verbose=yes. For complex queries you may use the json field to send an array of URL encoded JSON conditions, example: `[{"field": "year", "op": ">=", "val": 2010}, {"field": "year", "op": "<=", "val": 2020}]` Allowed operators are: `>`, `<`, `>=`, `<=`, `in`, `not in`, `like`, `not like`, `is null` and `not null`. Allowed json search fields are: year, make, model, trim, bodies.type, engines.cam_type, engines.cylinders, engines.drive_type, engines.engine_type, engines.fuel_type, engines.transmission, engines.valve_timing, engines.valves, make_id, make_model_id, make_model_trim_id, created, and modified.'''
    url = 'https://car-api2.p.rapidapi.com/api/trims'
    headers = {'x-rapidapi-host': 'car-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'direction': direction,
        'sort': sort,
        'year': year,
        'model': model,
        'page': page,
        'trim': trim,
        'make_model_id': make_model_id,
        'verbose': verbose,
        'make_id': make_id,
        'make': make,
        'json': json,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def trim_view(id: Annotated[Union[int, float], Field(description='Minimum: -9223372036854776000 Maximum: 9223372036854776000')]) -> dict: 
    '''Returns all data associated with the vehicle trim.'''
    url = 'https://car-api2.p.rapidapi.com/api/trims/%7Bid%7D'
    headers = {'x-rapidapi-host': 'car-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bodies(make_id: Annotated[Union[str, None], Field(description='')] = None,
           trim: Annotated[Union[str, None], Field(description='')] = None,
           json: Annotated[Union[str, None], Field(description='')] = None,
           sort: Annotated[Union[str, None], Field(description='')] = None,
           make_model_trim_id: Annotated[Union[str, None], Field(description='')] = None,
           make_model_id: Annotated[Union[str, None], Field(description='')] = None,
           model: Annotated[Union[str, None], Field(description='')] = None,
           verbose: Annotated[Union[str, None], Field(description='Includes make, model and trim')] = None,
           direction: Annotated[Union[str, None], Field(description='')] = None,
           make: Annotated[Union[str, None], Field(description='')] = None,
           year: Annotated[Union[str, None], Field(description='')] = None,
           type: Annotated[Union[str, None], Field(description='')] = None,
           limit: Annotated[Union[int, float, None], Field(description='')] = None,
           page: Annotated[Union[int, float, None], Field(description='')] = None,
           doors: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''To include additional information about the returned body (such as year, make, model and trim) request with the query parameter as verbose=yes. For complex queries you may use the json field to send an array of URL encoded JSON conditions, example: `[{"field": "doors", "op": ">=", "val": 4}, {"field": "type", "op": "in", "val": ["SUV","Van"]}]` See /api/vehicle-attributes for a complete list of vehicle attributes. Allowed operators are: `>`, `<`, `>=`, `<=`, `in`, `not in`, `like`, `not like`, `is null` and `not null`. Allowed json search fields are: year, make, model, trim, type, doors, make_id, make_model_id, and make_model_trim_id.'''
    url = 'https://car-api2.p.rapidapi.com/api/bodies'
    headers = {'x-rapidapi-host': 'car-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'make_id': make_id,
        'trim': trim,
        'json': json,
        'sort': sort,
        'make_model_trim_id': make_model_trim_id,
        'make_model_id': make_model_id,
        'model': model,
        'verbose': verbose,
        'direction': direction,
        'make': make,
        'year': year,
        'type': type,
        'limit': limit,
        'page': page,
        'doors': doors,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def engines(make: Annotated[Union[str, None], Field(description='')] = None,
            make_model_id: Annotated[Union[str, None], Field(description='')] = None,
            trim: Annotated[Union[str, None], Field(description='')] = None,
            cam_type: Annotated[Union[str, None], Field(description='')] = None,
            engine_type: Annotated[Union[str, None], Field(description='')] = None,
            make_model_trim_id: Annotated[Union[str, None], Field(description='')] = None,
            model: Annotated[Union[str, None], Field(description='')] = None,
            json: Annotated[Union[str, None], Field(description='')] = None,
            fuel_type: Annotated[Union[str, None], Field(description='')] = None,
            limit: Annotated[Union[int, float, None], Field(description='')] = None,
            drive_type: Annotated[Union[str, None], Field(description='')] = None,
            verbose: Annotated[Union[str, None], Field(description='Includes make, model and trim')] = None,
            make_id: Annotated[Union[str, None], Field(description='')] = None,
            year: Annotated[Union[str, None], Field(description='')] = None,
            cylinders: Annotated[Union[str, None], Field(description='')] = None,
            page: Annotated[Union[int, float, None], Field(description='')] = None,
            direction: Annotated[Union[str, None], Field(description='')] = None,
            sort: Annotated[Union[str, None], Field(description='')] = None,
            valve_timing: Annotated[Union[str, None], Field(description='')] = None,
            valves: Annotated[Union[str, None], Field(description='')] = None,
            size: Annotated[Union[str, None], Field(description='')] = None,
            horsepower_hp: Annotated[Union[str, None], Field(description='')] = None,
            transmission: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''To include additional information about the returned body (such as year, make, model and trim) request with the query parameter as verbose=yes. For complex queries you may use the json field to send an array of URL encoded JSON conditions, example: `[{"field": "horsepower_hp", "op": ">=", "val": 100}, {"field": "horsepower_hp", "op": "<=", "val": 300}]` See /api/vehicle-attributes for a complete list of vehicle attributes. Allowed operators are: `>`, `<`, `>=`, `<=`, `in`, `not in`, `like`, `not like`, `is null` and `not null`. Allowed json search fields are: year, make, model, trim, fuel_type, engine_type, transmission, drive_type, cam_type, valve_timing, valves, horsepower_hp, size, cylinders, make_id, make_model_id, and make_model_trim_id.'''
    url = 'https://car-api2.p.rapidapi.com/api/engines'
    headers = {'x-rapidapi-host': 'car-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'make': make,
        'make_model_id': make_model_id,
        'trim': trim,
        'cam_type': cam_type,
        'engine_type': engine_type,
        'make_model_trim_id': make_model_trim_id,
        'model': model,
        'json': json,
        'fuel_type': fuel_type,
        'limit': limit,
        'drive_type': drive_type,
        'verbose': verbose,
        'make_id': make_id,
        'year': year,
        'cylinders': cylinders,
        'page': page,
        'direction': direction,
        'sort': sort,
        'valve_timing': valve_timing,
        'valves': valves,
        'size': size,
        'horsepower_hp': horsepower_hp,
        'transmission': transmission,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def exterior_colors(name: Annotated[Union[str, None], Field(description='')] = None,
                    make_id: Annotated[Union[str, None], Field(description='')] = None,
                    make: Annotated[Union[str, None], Field(description='')] = None,
                    direction: Annotated[Union[str, None], Field(description='')] = None,
                    year: Annotated[Union[str, None], Field(description='')] = None,
                    model: Annotated[Union[str, None], Field(description='')] = None,
                    trim: Annotated[Union[str, None], Field(description='')] = None,
                    make_model_trim_id: Annotated[Union[str, None], Field(description='')] = None,
                    make_model_id: Annotated[Union[str, None], Field(description='')] = None,
                    page: Annotated[Union[int, float, None], Field(description='')] = None,
                    sort: Annotated[Union[str, None], Field(description='')] = None,
                    verbose: Annotated[Union[str, None], Field(description='Includes make, model and trim')] = None,
                    limit: Annotated[Union[int, float, None], Field(description='')] = None,
                    rgb: Annotated[Union[str, None], Field(description='')] = None,
                    json: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''To include additional information about the returned body (such as year, make, model and trim) request with the query parameter as verbose=yes. For complex queries you may use the json field to send an array of URL encoded JSON conditions, example: [{"field": "name", "op": "in", "val": ["red", "blue"]}] Allowed operators are: `>`, `<`, `>=`, `<=`, `in`, `not in`, `like`, `not like`, `is null` and `not null`. Allowed json search fields are: year, make, model, trim, name, rgb, make_id, make_model_id, and make_model_trim_i'''
    url = 'https://car-api2.p.rapidapi.com/api/exterior-colors'
    headers = {'x-rapidapi-host': 'car-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'name': name,
        'make_id': make_id,
        'make': make,
        'direction': direction,
        'year': year,
        'model': model,
        'trim': trim,
        'make_model_trim_id': make_model_trim_id,
        'make_model_id': make_model_id,
        'page': page,
        'sort': sort,
        'verbose': verbose,
        'limit': limit,
        'rgb': rgb,
        'json': json,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def interior_colors(direction: Annotated[Union[str, None], Field(description='')] = None,
                    limit: Annotated[Union[int, float, None], Field(description='')] = None,
                    make_model_trim_id: Annotated[Union[str, None], Field(description='')] = None,
                    year: Annotated[Union[str, None], Field(description='')] = None,
                    rgb: Annotated[Union[str, None], Field(description='')] = None,
                    page: Annotated[Union[int, float, None], Field(description='')] = None,
                    sort: Annotated[Union[str, None], Field(description='')] = None,
                    name: Annotated[Union[str, None], Field(description='')] = None,
                    trim: Annotated[Union[str, None], Field(description='')] = None,
                    verbose: Annotated[Union[str, None], Field(description='Includes make, model and trim')] = None,
                    json: Annotated[Union[str, None], Field(description='')] = None,
                    make_id: Annotated[Union[str, None], Field(description='')] = None,
                    model: Annotated[Union[str, None], Field(description='')] = None,
                    make: Annotated[Union[str, None], Field(description='')] = None,
                    make_model_id: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''To include additional information about the returned body (such as year, make, model and trim) request with the query parameter as verbose=yes. For complex queries you may use the json field to send an array of URL encoded JSON conditions, example: [{"field": "name", "op": "in", "val": ["red", "blue"]}] Allowed operators are: `>`, `<`, `>=`, `<=`, `in`, `not in`, `like`, `not like`, `is null` and `not null`. Allowed json search fields are: year, make, model, trim, name, rgb, make_id, make_model_id, and make_model_trim_i'''
    url = 'https://car-api2.p.rapidapi.com/api/interior-colors'
    headers = {'x-rapidapi-host': 'car-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'direction': direction,
        'limit': limit,
        'make_model_trim_id': make_model_trim_id,
        'year': year,
        'rgb': rgb,
        'page': page,
        'sort': sort,
        'name': name,
        'trim': trim,
        'verbose': verbose,
        'json': json,
        'make_id': make_id,
        'model': model,
        'make': make,
        'make_model_id': make_model_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def vehicle_attributes(attribute: Annotated[Union[str, None], Field(description='The attribute options to be returned')] = None) -> dict: 
    '''Returns all options for given attribute.'''
    url = 'https://car-api2.p.rapidapi.com/api/vehicle-attributes'
    headers = {'x-rapidapi-host': 'car-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'attribute': attribute,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def mileages(direction: Annotated[Union[str, None], Field(description='')] = None,
             range_city: Annotated[Union[str, None], Field(description='')] = None,
             page: Annotated[Union[int, float, None], Field(description='')] = None,
             combined_mpg: Annotated[Union[str, None], Field(description='')] = None,
             verbose: Annotated[Union[str, None], Field(description='Includes make, model and trim')] = None,
             epa_highway_mpg: Annotated[Union[str, None], Field(description='')] = None,
             limit: Annotated[Union[int, float, None], Field(description='')] = None,
             make_model_trim_id: Annotated[Union[str, None], Field(description='')] = None,
             sort: Annotated[Union[str, None], Field(description='')] = None,
             epa_city_mpg: Annotated[Union[str, None], Field(description='')] = None,
             model: Annotated[Union[str, None], Field(description='')] = None,
             trim: Annotated[Union[str, None], Field(description='')] = None,
             json: Annotated[Union[str, None], Field(description='')] = None,
             year: Annotated[Union[str, None], Field(description='')] = None,
             range_highway: Annotated[Union[str, None], Field(description='')] = None,
             make_model_id: Annotated[Union[str, None], Field(description='')] = None,
             make_id: Annotated[Union[str, None], Field(description='')] = None,
             make: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''To include additional information about the returned body (such as year, make, model and trim) request with the query parameter as verbose=yes. For complex queries you may use the json field to send an array of URL encoded JSON conditions, example: [{"field": "combined_mpg", "op": ">=", "val": 20}, {"field": "combined_mpg", "op": "<=", "val": 30}] Allowed operators are: `>`, `<`, `>=`, `<=`, `in`, `not in`, `like`, `not like`, `is null` and `not null`. Allowed json search fields are: year, make, model, trim, combined_mpg, epa_city_mpg, epa_highway_mpg, range_city, range_highway, make_id, make_model_id, and make_model_trim_id.'''
    url = 'https://car-api2.p.rapidapi.com/api/mileages'
    headers = {'x-rapidapi-host': 'car-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'direction': direction,
        'range_city': range_city,
        'page': page,
        'combined_mpg': combined_mpg,
        'verbose': verbose,
        'epa_highway_mpg': epa_highway_mpg,
        'limit': limit,
        'make_model_trim_id': make_model_trim_id,
        'sort': sort,
        'epa_city_mpg': epa_city_mpg,
        'model': model,
        'trim': trim,
        'json': json,
        'year': year,
        'range_highway': range_highway,
        'make_model_id': make_model_id,
        'make_id': make_id,
        'make': make,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
