from typing import TypedDict

class State(TypedDict):
    repo_path:str
    bug_description:str
    discovered_file:str
    diagnosis:str
    test_result:str

