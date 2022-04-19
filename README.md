# FastAPI
Building API using  fastapi 



#code

```


from fastapi import FastAPI
# from core.config import settings
from typing import Optional
from pydantic import BaseModel
from mangum import Mangum


class query(BaseModel):
    name: str
    age: Optional[int] = None
    profession: str
    interest: Optional[str] = None
    query: str



app = FastAPI()

@app.get("/")
async def welcome():
    return {"Greeting":"Hello World"}


@app.get("/intro")
async def my_intro():
    return {"Name":"Ajit kumar", "Age":21, "Country":"India", "Profession":"Software Engineer", "Languages":"Python, C++, C#", "Interests":"Football, Movies, Music", "Hobbies":"Coding, Reading, Travelling"}


@app.post("/query")
async def your_query(query: query):
    return {"Query":query.query, "Name":query.name, "Age":query.age, "Profession":query.profession}


handler = Mangum(app)


```
