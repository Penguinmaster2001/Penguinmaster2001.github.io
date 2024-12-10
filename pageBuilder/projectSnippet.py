
import json



def create_project_snippet(project_info: dict, project_snippet: str) -> str:

    for field_name in project_info.keys():

        field_info = project_info[field_name]

        if isinstance(field_info, list):
            tmp = field_info

            field_info = "<ul>\n"
            for li in tmp:
                field_info += f"<li>{li}</li>\n"
            field_info += "</ul>\n"

        project_snippet = project_snippet.replace(f"<!-- $${field_name}$$ -->", field_info)

    return project_snippet



def create_project_section_snippet(project_json_path: str) -> str:

    with open(project_json_path, 'r') as jsonFile:
        projects: list = json.load(jsonFile)

    with open("./pageParts/actions/resume-project.html", 'r') as f:
        project_snippet = f.read()

    projects_list = ""

    for project in projects:
        projects_list += create_project_snippet(project, project_snippet)

    with open("./pageParts/actions/resume-project-section.html", 'r') as f:
        projects_section_snippet = f.read()
    
    return projects_section_snippet.replace("<!-- $$resume-projects$$ -->", projects_list)
