from typing import List

from fastapi import APIRouter, Path, Query

from .models import Stop, Route
from .repository import stops_repository, routes_repository

stops_router = APIRouter(prefix='/stop', tags=['Stop'])
routes_router = APIRouter(prefix='/route', tags=['Route'])


@stops_router.get('/by_code/{stop_code}', response_model=Stop)
async def find_stop_by_code(stop_code: int = Path(..., description='Stop code', example=5200)) -> Stop:
    return await stops_repository.find_stop_by_code(stop_code)


@stops_router.get('/near', response_model=List[Stop])
async def find_nearest_stops(
        lat: float = Query(..., description='Latitude', ge=-90, le=90),
        lng: float = Query(..., description='Longitude', ge=-180, le=180),
        radius: int = Query(100, description='Search radius', ge=0, le=5000),
) -> List[Stop]:
    return await stops_repository.find_stops_in_area(lat, lng, radius)


@routes_router.get('/{route_id}', response_model=Route)
async def find_route_by_id(route_id: str) -> Route:
    return routes_repository.find_route_by_id(route_id)
