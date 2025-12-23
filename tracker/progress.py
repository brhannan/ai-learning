"""Progress visualization for AI learning."""

from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn
from rich import box

from .habits import HabitTracker

console = Console()


class ProgressVisualizer:
    """Visualize learning progress."""

    # Curriculum modules with reading counts
    MODULES = {
        "01-ml-fundamentals": {"name": "ML Fundamentals", "readings": 8, "phase": 1},
        "02-transformers": {"name": "Transformers", "readings": 10, "phase": 1},
        "03-scaling-laws": {"name": "Scaling Laws", "readings": 5, "phase": 1},
        "04-llm-architectures": {"name": "LLM Architectures", "readings": 8, "phase": 2},
        "05-training-infra": {"name": "Training Infra", "readings": 6, "phase": 2},
        "06-inference": {"name": "Inference & Serving", "readings": 6, "phase": 2},
        "07-rlhf": {"name": "RLHF Fundamentals", "readings": 8, "phase": 3},
        "08-constitutional-ai": {"name": "Constitutional AI", "readings": 10, "phase": 3},
        "09-interpretability": {"name": "Interpretability", "readings": 12, "phase": 3},
        "10-alignment": {"name": "Alignment Research", "readings": 8, "phase": 3},
        "11-prompting": {"name": "Advanced Prompting", "readings": 8, "phase": 4},
        "12-rag": {"name": "RAG Systems", "readings": 8, "phase": 4},
        "13-agents": {"name": "Agents & Tool Use", "readings": 10, "phase": 4},
        "14-coding-agents": {"name": "Coding Agents", "readings": 6, "phase": 4},
        "15-system-design": {"name": "System Design", "readings": 6, "phase": 5},
        "16-evals": {"name": "Benchmarks & Evals", "readings": 6, "phase": 5},
        "17-multimodal": {"name": "Multimodal", "readings": 6, "phase": 5},
    }

    def __init__(self, tracker: HabitTracker):
        self.tracker = tracker

    def print_calendar(self, weeks: int = 4):
        """Print a calendar showing activity days."""
        activity_dates = self.tracker.get_activity_dates()
        today = datetime.now().date()

        console.print("[bold]Activity Calendar[/bold]")
        console.print()

        # Header
        console.print("    Mo Tu We Th Fr Sa Su")

        # Go back to start of the period
        start = today - timedelta(days=today.weekday() + (weeks - 1) * 7)

        for week in range(weeks):
            week_start = start + timedelta(weeks=week)
            row = f"W{week + 1}: "

            for day in range(7):
                current = week_start + timedelta(days=day)
                date_str = current.isoformat()

                if current > today:
                    row += "[dim]  [/dim] "
                elif date_str in activity_dates:
                    row += "[green]✓[/green]  "
                elif current == today:
                    row += "[yellow]○[/yellow]  "
                else:
                    row += "[dim]·[/dim]  "

            console.print(row)

    def print_module_progress(self):
        """Print progress for each module."""
        # For now, show placeholder progress based on XP
        # In a real implementation, this would track which readings were completed
        level, xp = self.tracker.get_level_info()

        table = Table(title="Module Progress", box=box.SIMPLE)
        table.add_column("Module", style="cyan")
        table.add_column("Progress", style="green", width=25)
        table.add_column("Phase")

        # Show modules with simulated progress based on level
        for module_id, info in self.MODULES.items():
            phase = info["phase"]
            name = info["name"]

            # Simulate progress based on level
            if level >= phase * 2:
                progress = 100
                bar = "████████████████████"
            elif level >= phase * 2 - 1:
                progress = 50
                bar = "██████████░░░░░░░░░░"
            elif level >= phase:
                progress = 20
                bar = "████░░░░░░░░░░░░░░░░"
            else:
                progress = 0
                bar = "░░░░░░░░░░░░░░░░░░░░"

            if progress == 100:
                status = f"[green]{bar}[/green] {progress}%"
            elif progress > 0:
                status = f"[yellow]{bar}[/yellow] {progress}%"
            else:
                status = f"[dim]{bar}[/dim] {progress}%"

            phase_label = f"Phase {phase}"
            if phase == 3:
                phase_label += " [bold magenta](Anthropic Core)[/bold magenta]"

            table.add_row(name, status, phase_label)

        console.print(table)

    def print_recent_activity(self, days: int = 7):
        """Print recent activity log."""
        activities = self.tracker.get_recent_activities(days)

        if not activities:
            console.print("[dim]No recent activity. Start with 'ai-learn log'![/dim]")
            return

        console.print("[bold]Recent Activity[/bold]")
        console.print()

        # Group by date
        by_date = {}
        for activity in activities:
            date = activity["date"]
            if date not in by_date:
                by_date[date] = []
            by_date[date].append(activity)

        for date in sorted(by_date.keys(), reverse=True)[:5]:
            console.print(f"[bold]{date}[/bold]")
            for activity in by_date[date]:
                icon = self._get_type_icon(activity["type"])
                console.print(f"  {icon} {activity['description']}")
            console.print()

    def _get_type_icon(self, activity_type: str) -> str:
        """Get icon for activity type."""
        icons = {
            "paper": "📄",
            "blog": "📝",
            "video": "🎥",
            "exercise": "💪",
            "project": "🔨",
        }
        return icons.get(activity_type, "📚")

    def print_phase_overview(self):
        """Print overview of all phases."""
        phases = {
            1: ("Foundations", ["ML Fundamentals", "Transformers", "Scaling Laws"]),
            2: ("LLM Engineering", ["Architectures", "Training", "Inference"]),
            3: ("Alignment & Safety", ["RLHF", "Constitutional AI", "Interpretability", "Alignment"]),
            4: ("Agents & Apps", ["Prompting", "RAG", "Agents", "Coding Agents"]),
            5: ("Mastery", ["System Design", "Evals", "Multimodal"]),
        }

        for phase_num, (name, modules) in phases.items():
            console.print(f"\n[bold]Phase {phase_num}: {name}[/bold]")
            for module in modules:
                console.print(f"  • {module}")
