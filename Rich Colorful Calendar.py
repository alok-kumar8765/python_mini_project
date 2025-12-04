# Purpose: Generate and display a beautifully formatted, colorful calendar directly in the console using the 'rich' library.
# Dependencies:
# pip install rich
import calendar
from rich.console import Console
from rich.table import Table

# --- Configuration ---
TARGET_YEAR = 2026 # The year to generate the calendar for

# ---------------------

def colorful_calendar(year: int):
    """
    Generates a yearly calendar, formatting each month with rich text styling,
    and displays it in the console.

    Args:
        year (int): The calendar year to display.
    """
    print(f"--- Generating Calendar for {year} with Rich ---")
    
    # Initialize Console and Calendar module
    console = Console()
    cal = calendar.TextCalendar(calendar.SUNDAY) # Start week on Sunday (US standard)
    
    # Get all month data for the given year
    # calendar.monthcalendar(year, m) returns a list of lists (weeks)
    months_data = [cal.monthcalendar(year, m) for m in range(1, 13)]
    
    for month_index, month_weeks in enumerate(months_data):
        # Month name is 1-indexed (index + 1)
        month_name = calendar.month_name[month_index + 1]
        
        # 1. Create a rich Table object for the month
        table = Table(
            title=f"[bold cyan]{month_name} {year}[/bold cyan]",
            show_header=True,
            show_lines=True,
            title_style="bold cyan"
        )
        
        # 2. Define table columns with specific justification and style
        # Mon-Fri are green, Sat/Sun are red
        table.add_column("Mon", justify="center", style="green")
        table.add_column("Tue", justify="center", style="green")
        table.add_column("Wed", justify="center", style="green")
        table.add_column("Thu", justify="center", style="green")
        table.add_column("Fri", justify="center", style="green")
        table.add_column("Sat", justify="center", style="red")
        table.add_column("Sun", justify="center", style="red")
        
        # 3. Populate rows with day data
        for week in month_weeks:
            row_data = []
            for day in week:
                # 0 represents a day outside the current month (needs to be blank)
                # Convert the day integer to a string, or an empty string if it's 0
                day_str = str(day) if day != 0 else ""
                row_data.append(day_str)
            
            # Add the completed week as a row
            table.add_row(*row_data)
        
        # 4. Print the table to the console
        console.print(table)
        console.print("\n") # Add a newline spacer

# --- Execution ---
if __name__ == "__main__":
    colorful_calendar(TARGET_YEAR)

# Use Cases:
# 1. CLI Tools: Enhancing command-line application output with color and formatting.
# 2. Productivity Scripts: Displaying a formatted calendar for date planning.
# 3. System Utility: Creating visually distinct output for scripts run in the terminal.