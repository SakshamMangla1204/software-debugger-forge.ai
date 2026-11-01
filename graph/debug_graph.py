import sys
from pathlib import Path

# Make the project root importable so `state` can be found when this file
# is run directly (e.g. `python3 graph/debug_graph.py`).
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from langgraph.graph import StateGraph, START, END

from state import State


# ---------------------------------------------------------------------------
# Local agent stubs (kept in this file so debug_graph.py works on its own.
# The agent files under agents/ are intentionally left untouched per your
# request; replace these stubs with real implementations later.)
# ---------------------------------------------------------------------------
def triage_agent(state: State) -> dict:
    bug_description = state.get("bug_description", "")
    print(f"[Triage] Received bug: {bug_description}")
    return {"discovered_file": "src/main.py"}


def investigator_agent(state: State) -> dict:
    discovered_file = state.get("discovered_file", "")
    print(f"[Investigator] Investigating: {discovered_file}")
    return {"diagnosis": "Likely cause: missing error handling."}


def repair_planner_agent(state: State) -> dict:
    diagnosis = state.get("diagnosis", "")
    print(f"[Repair Planner] Diagnosis: {diagnosis}")
    return {"repair_plan": "Fix the faulty line and add tests."}


def patch_generator_agent(state: State) -> dict:
    repair_plan = state.get("repair_plan", "")
    print(f"[Patch Generator] Plan: {repair_plan}")
    return {"patch": "---diff\n- old_code()\n+ new_code_fixed()\n---"}


def verifier_agent(state: State) -> dict:
    patch = state.get("patch", "")
    print(f"[Verifier] Verifying patch...")
    return {"test_result": "PASSED (simulated)"}


def reporter_agent(state: State) -> dict:
    test_result = state.get("test_result", "")
    print(f"[Reporter] {test_result}")
    return {}


# ---------------------------------------------------------------------------
# Build the debug graph
# ---------------------------------------------------------------------------
builder = StateGraph(State)

builder.add_node("triage", triage_agent)
builder.add_node("investigator", investigator_agent)
builder.add_node("repair_planner", repair_planner_agent)
builder.add_node("patch_generator", patch_generator_agent)
builder.add_node("verifier", verifier_agent)
builder.add_node("reporter", reporter_agent)

builder.add_edge(START, "triage")
builder.add_edge("triage", "investigator")
builder.add_edge("investigator", "repair_planner")
builder.add_edge("repair_planner", "patch_generator")
builder.add_edge("patch_generator", "verifier")
builder.add_edge("verifier", "reporter")
builder.add_edge("reporter", END)

debug_graph = builder.compile()


if __name__ == "__main__":
    # Example run
    initial_state = {
        "repo_path": ".",
        "bug_description": "App crashes when saving a file.",
        "discovered_file": "",
        "diagnosis": "",
        "test_result": "",
    }
    result = debug_graph.invoke(initial_state)
    print("\n=== Final result ===")
    print(result)


