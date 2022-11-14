from LAS import Converter
import json
from fastapi import APIRouter, FastAPI, File, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
las_data = './data/mockdata3.las'

router = APIRouter(prefix="/json", tags=['Convert_LAS'])

@router.get('/')
async def las_to_json (response: JSONResponse):
  # print("running")
  #  return {"message": "sent to the back"}
  c = Converter() # create converter object

  data = c.set_file(las_data) #return LogWrapper
  json_data = {"lasData": {"data" : data.data, "version" : data.version, "curve" : data.curve, "parameter": data.parameter, "well":data.well, "other":data.other }}
  # get section
  # data      = log.data
  # version   = log.version
  # curve     = log.curve
  # parameter = log.parameter
  # well      = log.well
  # other     = log.other
  # log = json.dumps(log)
  # log = data.get_json("json")
  return json_data
  # print(log.well)
  def is_json(data):
    try:
        json_object = json.loads(data)
    except ValueError as e:
        return False
    return True

  





