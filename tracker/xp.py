"""XP and leveling system for AI learning."""

from .habits import HabitTracker


class XPSystem:
    """Manage XP calculations and levels."""

    # XP rewards by activity type
    XP_VALUES = {
        "blog": 25,
        "paper": 50,
        "video": 30,
        "exercise": 75,
        "project": 100,
    }

    # Level thresholds and names
    LEVELS = [
        (0, "Novice"),
        (250, "Apprentice"),
        (750, "Practitioner"),
        (1500, "Specialist"),
        (3000, "Prompt Engineer"),
        (5000, "Agent Architect"),
        (8000, "LLM Whisperer"),
        (12000, "AI Engineer"),
        (18000, "Frontier Explorer"),
        (25000, "Master"),
    ]

    def __init__(self, tracker: HabitTracker):
        self.tracker = tracker

    def calculate_xp(self, activity_type: str) -> int:
        """Calculate XP for an activity type."""
        base_xp = self.XP_VALUES.get(activity_type, 25)

        # Streak bonus
        streak = self.tracker.get_streak()
        streak_multiplier = 1.0

        if streak >= 30:
            streak_multiplier = 1.5
        elif streak >= 14:
            streak_multiplier = 1.3
        elif streak >= 7:
            streak_multiplier = 1.2
        elif streak >= 3:
            streak_multiplier = 1.1

        return int(base_xp * streak_multiplier)

    def get_level_name(self, level: int) -> str:
        """Get the name for a level."""
        if level < 1:
            return "Unknown"
        if level > len(self.LEVELS):
            return "Master"
        return self.LEVELS[level - 1][1]

    def get_xp_for_level(self, level: int) -> int | None:
        """Get the XP threshold for a level."""
        if level < 1 or level > len(self.LEVELS):
            return None
        return self.LEVELS[level - 1][0]

    def get_progress_to_next_level(self) -> tuple[int, int, float]:
        """Get progress to next level: (current_in_level, needed_for_level, percentage)."""
        level, total_xp = self.tracker.get_level_info()

        current_threshold = self.get_xp_for_level(level) or 0
        next_threshold = self.get_xp_for_level(level + 1)

        if next_threshold is None:
            # Max level
            return 0, 0, 100.0

        xp_in_level = total_xp - current_threshold
        xp_needed = next_threshold - current_threshold
        percentage = (xp_in_level / xp_needed) * 100 if xp_needed > 0 else 100

        return xp_in_level, xp_needed, percentage
