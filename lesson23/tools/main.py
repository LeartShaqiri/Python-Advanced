from fastapi import FastAPI
from models import  Deverloper, Project

app = FastAPI()


@app.post("/developers")
def create_developer(developer: Deverloper):
    return {"message": "Developer creted", "developer": developer}


@app.post("/projects")
def create_project(project: Project):
    return {"message": "Project creted", "developer": project}


@app.get("/projects")
def get_projects():
    sample_project = Project(
        title= "TEST"
        description= "this is the test project"
        langauge= ["Python", "Java"]
        lead_developer=Deverloper(name="joe", experience=5)
    )