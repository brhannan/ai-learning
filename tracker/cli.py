#!/usr/bin/env python3
"""AI Learning CLI - Track your journey to becoming an AI engineer."""

import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich import box
from datetime import datetime, timedelta
from pathlib import Path
import json

from .habits import HabitTracker
from .xp import XPSystem
from .progress import ProgressVisualizer

app = typer.Typer(
    name="ai-learn",
    help="Track your AI learning journey. Become Anthropic-ready.",
    add_completion=False,
)
console = Console()

# Data file path
DATA_DIR = Path(__file__).parent / "data"
DATA_FILE = DATA_DIR / "log.json"


def get_tracker() -> HabitTracker:
    """Get or create the habit tracker."""
    DATA_DIR.mkdir(exist_ok=True)
    return HabitTracker(DATA_FILE)


@app.command()
def log(
    description: str = typer.Argument(..., help="What you read/completed"),
    reading_type: str = typer.Option(
        "paper", "--type", "-t", help="Type: paper, blog, video, exercise, project"
    ),
):
    """Log a completed reading or activity."""
    tracker = get_tracker()
    xp_system = XPSystem(tracker)

    # Log the activity
    entry = tracker.log_activity(description, reading_type)

    # Calculate XP
    xp_earned = xp_system.calculate_xp(reading_type)
    old_level, old_xp = tracker.get_level_info()
    tracker.add_xp(xp_earned)
    new_level, new_xp = tracker.get_level_info()

    # Show result
    console.print()
    console.print(f"[green]✓[/green] Logged: [bold]{description}[/bold]")
    console.print(f"  [yellow]+{xp_earned} XP[/yellow] earned!")

    # Check for level up
    if new_level > old_level:
        level_name = xp_system.get_level_name(new_level)
        console.print()
        console.print(Panel(
            f"[bold yellow]⭐ LEVEL UP! ⭐[/bold yellow]\n\n"
            f"You are now Level {new_level}: [bold cyan]{level_name}[/bold cyan]",
            title="Congratulations!",
            border_style="yellow",
        ))

    # Show streak
    streak = tracker.get_streak()
    if streak > 0:
        console.print(f"  [red]🔥 Streak: {streak} days[/red]")

    # Check achievements
    new_achievements = tracker.check_achievements()
    for achievement in new_achievements:
        console.print()
        console.print(f"  [bold magenta]🏆 Achievement Unlocked: {achievement}[/bold magenta]")


@app.command()
def streak():
    """Show your current streak and calendar."""
    tracker = get_tracker()
    visualizer = ProgressVisualizer(tracker)

    current_streak = tracker.get_streak()
    longest_streak = tracker.get_longest_streak()

    console.print()
    console.print(Panel(
        f"[bold red]🔥 Current Streak: {current_streak} days[/bold red]\n"
        f"[dim]Longest streak: {longest_streak} days[/dim]",
        title="Streak Status",
        border_style="red",
    ))

    # Show calendar
    console.print()
    visualizer.print_calendar()


@app.command()
def progress(
    module: str = typer.Argument(None, help="Module name for specific progress"),
):
    """Show your learning progress."""
    tracker = get_tracker()
    xp_system = XPSystem(tracker)
    visualizer = ProgressVisualizer(tracker)

    level, total_xp = tracker.get_level_info()
    level_name = xp_system.get_level_name(level)
    next_level_xp = xp_system.get_xp_for_level(level + 1)
    xp_to_next = next_level_xp - total_xp if next_level_xp else 0

    console.print()
    console.print(Panel(
        f"[bold cyan]📚 AI Learning Progress[/bold cyan]\n\n"
        f"[red]🔥 Streak: {tracker.get_streak()} days[/red]    "
        f"[yellow]⭐ Level {level}: {level_name}[/yellow]\n"
        f"[dim]💎 {total_xp:,} XP  ({xp_to_next:,} to Level {level + 1})[/dim]",
        border_style="cyan",
    ))

    # Show module progress
    console.print()
    visualizer.print_module_progress()

    # Show recent activity
    console.print()
    visualizer.print_recent_activity()


@app.command()
def stats():
    """Show detailed statistics."""
    tracker = get_tracker()

    stats_data = tracker.get_stats()

    table = Table(title="📊 Learning Statistics", box=box.ROUNDED)
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Total readings", str(stats_data["total_readings"]))
    table.add_row("Papers read", str(stats_data["papers"]))
    table.add_row("Blog posts", str(stats_data["blogs"]))
    table.add_row("Videos watched", str(stats_data["videos"]))
    table.add_row("Exercises completed", str(stats_data["exercises"]))
    table.add_row("Projects worked on", str(stats_data["projects"]))
    table.add_row("Total XP", f"{stats_data['total_xp']:,}")
    table.add_row("Current streak", f"{stats_data['streak']} days")
    table.add_row("Longest streak", f"{stats_data['longest_streak']} days")
    table.add_row("Days active", str(stats_data["days_active"]))

    console.print()
    console.print(table)


@app.command()
def next():
    """Suggest what to read next."""
    tracker = get_tracker()

    # Get current phase based on XP
    level, xp = tracker.get_level_info()

    suggestions = {
        1: ("Phase 1: Foundations", [
            "The Illustrated Transformer (blog)",
            "Attention Is All You Need (paper)",
            "3Blue1Brown attention video",
        ]),
        2: ("Phase 1: Foundations", [
            "Continue transformer readings",
            "Start Project 1: Transformer from scratch",
        ]),
        3: ("Phase 2: LLM Engineering", [
            "GPT-2 paper",
            "LLaMA paper series",
        ]),
        4: ("Phase 2: LLM Engineering", [
            "FlashAttention paper",
            "vLLM documentation",
        ]),
        5: ("Phase 3: Alignment", [
            "Constitutional AI paper (MUST READ)",
            "InstructGPT paper",
        ]),
        6: ("Phase 3: Alignment", [
            "Scaling Monosemanticity (Anthropic)",
            "Start Project 2: Mini-RLHF",
        ]),
        7: ("Phase 4: Agents", [
            "ReAct paper",
            "Chain-of-Thought paper",
        ]),
        8: ("Phase 4: Agents", [
            "SWE-Agent paper",
            "Start Project 4: Agent Framework",
        ]),
        9: ("Phase 5: Mastery", [
            "System design practice",
            "Work on capstone project",
        ]),
        10: ("Complete!", [
            "Polish portfolio",
            "Practice interviews",
            "Apply to Anthropic!",
        ]),
    }

    phase, items = suggestions.get(level, suggestions[1])

    console.print()
    console.print(Panel(
        f"[bold cyan]{phase}[/bold cyan]\n\n" +
        "\n".join(f"  → {item}" for item in items),
        title="📖 Suggested Next Steps",
        border_style="blue",
    ))


@app.command()
def achievements():
    """Show all achievements."""
    tracker = get_tracker()
    unlocked = tracker.get_achievements()

    all_achievements = {
        "🔥 Week Warrior": "7 day streak",
        "🌟 Month Master": "30 day streak",
        "📚 Deep Diver": "5 readings in one module",
        "🎯 Focused": "Complete a module",
        "🚀 Speed Reader": "3 readings in one day",
        "🧠 Polymath": "Read from 5 different modules",
        "💪 Consistent": "Log activity 3 days in a row",
        "📖 First Steps": "Log your first reading",
        "⭐ Level 5": "Reach Prompt Engineer level",
        "🏆 Level 10": "Reach Master level",
    }

    console.print()
    table = Table(title="🏆 Achievements", box=box.ROUNDED)
    table.add_column("Badge", style="yellow")
    table.add_column("Achievement", style="cyan")
    table.add_column("Status", style="green")

    for badge, desc in all_achievements.items():
        status = "[green]✓ Unlocked[/green]" if badge in unlocked else "[dim]Locked[/dim]"
        table.add_row(badge.split()[0], f"{badge.split(' ', 1)[1]}: {desc}", status)

    console.print(table)


@app.command()
def quote():
    """Show a motivational quote."""
    import random

    quotes = [
        ("The secret of getting ahead is getting started.", "Mark Twain"),
        ("You do not rise to the level of your goals. You fall to the level of your systems.", "James Clear"),
        ("Every expert was once a beginner.", "Helen Hayes"),
        ("The best time to plant a tree was 20 years ago. The second best time is now.", "Chinese Proverb"),
        ("Small daily improvements are the key to staggering long-term results.", "Robin Sharma"),
        ("Don't break the chain.", "Jerry Seinfeld"),
        ("We are what we repeatedly do. Excellence is not an act, but a habit.", "Aristotle"),
        ("The only way to do great work is to love what you do.", "Steve Jobs"),
        ("Learning never exhausts the mind.", "Leonardo da Vinci"),
        ("An investment in knowledge pays the best interest.", "Benjamin Franklin"),
    ]

    quote, author = random.choice(quotes)

    console.print()
    console.print(Panel(
        f"[italic]{quote}[/italic]\n\n— {author}",
        border_style="blue",
    ))


@app.command()
def reset(
    confirm: bool = typer.Option(False, "--yes", "-y", help="Confirm reset"),
):
    """Reset all progress (use with caution!)."""
    if not confirm:
        console.print("[yellow]Are you sure? Use --yes to confirm.[/yellow]")
        return

    tracker = get_tracker()
    tracker.reset()
    console.print("[green]Progress reset.[/green]")


if __name__ == "__main__":
    app()
