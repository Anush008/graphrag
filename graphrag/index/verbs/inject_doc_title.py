# Copyright (c) 2024 Microsoft Corporation. All rights reserved.
"""A module containing 'hacked_verb' method definition."""

import logging
from typing import cast

import pandas as pd
from datashaper import TableContainer, VerbInput, verb

log = logging.getLogger(__name__)


@verb(name="inject_doc_title")
def inject_doc_title(input: VerbInput, **_kwargs) -> TableContainer:
    """Inject document titles into text chunks."""
    text_units_table = cast(pd.DataFrame, input.get_input())
    num_rows = len(text_units_table)
    docs_table = cast(pd.DataFrame, input.get_others()[0])[["id", "title"]].rename({"id": "document_id"}, axis=1)

    text_units_table["document_id"] = text_units_table["document_ids"].apply(lambda x: x[0])
    text_units_table = text_units_table.merge(
        docs_table, on="document_id", how="left"
    )
    text_units_table["chunk"] = (
        text_units_table["title"] + " " + text_units_table["chunk"]
    )
    num_updated_rows = len(text_units_table)

    log.info(
        "Injected document titles into %d/%d text units", num_updated_rows, num_rows
    )
    return TableContainer(table=text_units_table)
