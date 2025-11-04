-> uv Keys
        cd ai_trip_planner
        uv python list
        uv python install cpython-3.12.12-windows-x86_64-none
        uv python list
        uv venv env --python cpython-3.11.9-windows-x86_64-none
        .\env\Scripts\activate
        uv pip list
        uv pip install langchain
        uv pip list
        doskey/history