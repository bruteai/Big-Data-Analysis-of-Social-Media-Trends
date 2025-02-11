from fastapi import FastAPI

app = FastAPI()

@app.get("/trends/")
def get_trends():
    return {"top_trends": ["#AI", "#BigData", "#NLP"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
