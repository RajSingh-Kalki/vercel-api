from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load the student marks data
with open("q-vercel-python.json") as f:
    student_marks = {student["name"]: student["marks"] for student in json.load(f)}

@app.get("/api")
def get_marks(name: str):
    names = name.split(",")
    marks = []
    for n in names:
        if n in student_marks:
            marks.append(student_marks[n])
        else:
            raise HTTPException(status_code=404, detail=f"Student {n} not found")
    return {"marks": marks}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
