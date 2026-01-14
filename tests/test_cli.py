"""Tests for the CLI."""

import json
import tempfile
from pathlib import Path

from tracker.habits import HabitTracker
from tracker.cli import get_uncompleted_suggestions


def test_get_uncompleted_suggestions_filters_completed_items():
    """Suggestions should not include items that have been completed."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        # Simulate a user who has completed some items
        data = {
            "activities": [
                {"description": "The Illustrated Transformer", "type": "blog", "date": "2026-01-13", "timestamp": "2026-01-13T00:00:00"},
                {"description": "Attention Is All You Need", "type": "paper", "date": "2026-01-14", "timestamp": "2026-01-14T00:00:00"},
            ],
            "xp": 75,
            "achievements": [],
            "streak_data": {"current": 2, "longest": 2, "last_activity_date": "2026-01-14"},
        }
        json.dump(data, f)
        f.flush()

        tracker = HabitTracker(Path(f.name))

        suggestions = [
            "The Illustrated Transformer (blog)",
            "Attention Is All You Need (paper)",
            "3Blue1Brown attention video",
        ]

        uncompleted = get_uncompleted_suggestions(tracker, suggestions)

        # Should only have the video left
        assert len(uncompleted) == 1
        assert "3Blue1Brown" in uncompleted[0]


def test_get_uncompleted_suggestions_returns_all_when_none_completed():
    """When nothing is completed, all suggestions should be returned."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        data = {
            "activities": [],
            "xp": 0,
            "achievements": [],
            "streak_data": {"current": 0, "longest": 0, "last_activity_date": None},
        }
        json.dump(data, f)
        f.flush()

        tracker = HabitTracker(Path(f.name))

        suggestions = [
            "The Illustrated Transformer (blog)",
            "Attention Is All You Need (paper)",
        ]

        uncompleted = get_uncompleted_suggestions(tracker, suggestions)

        assert len(uncompleted) == 2
