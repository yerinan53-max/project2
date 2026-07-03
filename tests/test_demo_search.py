import sys
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
for module_name in list(sys.modules):
    if module_name == "src" or module_name.startswith("src."):
        del sys.modules[module_name]

from src.config import SAMPLE_DATA_PATH
from src.data import load_cases
from src.search import expand_legal_query, semantic_search


class FakeEmbedder:
    def encode(self, texts):
        return np.array([[1.0]], dtype="float32")


def test_sample_cases_are_public_demo_data():
    cases = load_cases(SAMPLE_DATA_PATH)
    assert len(cases) >= 50
    assert "지나가는 행인 폭행 상해 사건" in set(cases["case_name"])


def test_assault_query_expands_to_relevant_terms():
    expanded = expand_legal_query("지나가는 행인을 폭행함")
    assert "행인 폭행" in expanded
    assert "상해" in expanded


def test_semantic_search_returns_dataframe():
    cases = pd.DataFrame(
        [
            {
                "case_name": "지나가는 행인 폭행 상해 사건",
                "issues": "행인 폭행과 상해 고의",
                "summary": "행인을 폭행하여 상해를 입힌 사례",
            }
        ]
    )
    embeddings = np.array([[1.0]], dtype="float32")
    results = semantic_search("지나가는 행인을 폭행함", cases, embeddings, FakeEmbedder())
    assert results.iloc[0]["case_name"] == "지나가는 행인 폭행 상해 사건"
