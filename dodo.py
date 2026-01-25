"""dodo.py for catalog - builds the unified chartbook site."""

import chartbook

BASE_DIR = chartbook.env.get_project_root()


def task_build_catalog():
    """Build the chartbook catalog site."""
    return {
        "actions": ["chartbook build -f"],
        "file_dep": ["chartbook.toml"],
        "targets": [BASE_DIR / "docs" / "index.html"],
        "verbosity": 2,
    }
