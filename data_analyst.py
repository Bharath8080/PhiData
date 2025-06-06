import json
from phi.model.google import Gemini
from phi.agent.duckdb import DuckDbAgent
from dotenv import load_dotenv
load_dotenv()
data_analyst = DuckDbAgent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    semantic_model=json.dumps(
        {
            "tables": [
                {
                    "name": "movies",
                    "description": "Contains information about movies from IMDB.",
                    "path": "https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
                }
            ]
        }
    ),
    markdown=True,
)
data_analyst.print_response(
    "Show me a histogram of ratings. "
    "Choose an appropriate bucket size but share how you chose it. "
    "Show me the result as a pretty ascii diagram",
    stream=True,
)
