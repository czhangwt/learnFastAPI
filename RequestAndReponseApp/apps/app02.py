from fastapi import APIRouter
from typing import Union, Optional
app02 = APIRouter()

# route parameter example with query parameters
# the query parameters are optional and can be used to filter results
# different from path parameters, query parameters are not part of the URL path
@app02.get("/jobs/{position}")
async def get_job(position, salary:Union[str, None]=None, education=None, experience:Optional[int]=None): 
    # None is the default value for optional query parameters
    # Union[str, None] means the parameter can be a string or None, set it = None to make it optional
    # Optional[int] means the parameter can be an int or None, set it = None to make it optional
    return {
        "position": position,
        "salary": salary,
        "education": education,
        "experience": experience
    }