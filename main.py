from fastapi import FastAPI

#  instance of FastAPI
app = FastAPI()

# we can reference the 'app' as a fastapi class object and use it to create routes.
@app.get('/ajit')  #decorator :- which is used to provide extra functionality to function
async def ajit():
    return "Hello welcome"

