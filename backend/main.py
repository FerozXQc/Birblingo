from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return 'hello world'

if __name__ == '__main__':
    app.run()