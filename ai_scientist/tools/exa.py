import os
import requests
import time
import warnings
from typing import Dict, List, Optional, Union

import backoff

from ai_scientist.tools.base_tool import BaseTool


def on_backoff(details: Dict) -> None:
    print(
        f"Backing off {details['wait']:0.1f} seconds after {details['tries']} tries "
        f"calling function {details['target'].__name__} at {time.strftime('%X')}"
    )


class SemanticScholarSearchTool(BaseTool):
    def __init__(
        self,
        name: str = "SearchSemanticScholar",
        description: str = (
            "Search for relevant literature using Semantic Scholar. "
            "Provide a search query to find relevant papers."
        ),
        max_results: int = 10,
    ):
        parameters = [
            {
                "name": "query",
                "type": "str",
                "description": "The search query to find relevant papers.",
            }
        ]
        super().__init__(name, description, parameters)
        self.max_results = max_results
        self.EXA_API_KEY = os.getenv("EXA_API_KEY")
        if not self.EXA_API_KEY:
            warnings.warn(
                "No Exa API key found. Requests will be subject to stricter rate limits. "
                "Set the EXA_API_KEY environment variable for higher limits."
            )

    def use_tool(self, query: str) -> Optional[str]:
        papers = self.search_for_papers(query)
        if papers:
            return self.format_papers(papers)
        else:
            return "No papers found."

    @backoff.on_exception(
        backoff.expo,
        (requests.exceptions.HTTPError, requests.exceptions.ConnectionError),
        on_backoff=on_backoff,
    )
    def search_for_papers(self, query: str) -> Optional[List[Dict]]:
        if not query:
            return None
        
        headers = {
            "content-type": "application/json"
        }
        if self.EXA_API_KEY:
            headers["x-api-key"] = self.EXA_API_KEY
        
        data = {
            "query": query,
            "category": "research paper",
            "numResults": self.max_results,
            "contents": {
                "text": {
                    "maxCharacters": 512,
                }
            },
        }
        
        rsp = requests.post(
            "https://api.exa.ai/search",
            headers=headers,
            json=data,
        )
        print(f"Response Status Code: {rsp.status_code}")
        print(f"Response Content: {rsp.text[:500]}")
        rsp.raise_for_status()
        results = rsp.json()

        papers = results.get("results", [])
        total = len(papers)
        print(f"Response Content: results total: {total}")
        if total == 0:
            return None
        # Sort papers by citationCount in descending order
        papers.sort(key=lambda x: x.get("score", 0), reverse=True)
        return papers

    def format_papers(self, papers: List[Dict]) -> str:
        paper_strings = []
        for i, paper in enumerate(papers):
            authors =  paper.get("authors", [])
            paper_strings.append(
                f"""{i + 1}: {paper.get("title", "Unknown Title")}. {authors}. {paper.get("publishedDate", "Unknown publishedDate")}.
score: {paper.get("score", "N/A")}
Abstract: {paper.get("text", "No text available.")}"""
            )
        return "\n\n".join(paper_strings)
