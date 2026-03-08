import os
import sys

# Add project root to sys.path
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from scripts.database import db_manager
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def generate_dashboard():
    """Fetches analytics data from the database and displays it neatly."""
    console.print("\n[bold cyan]📊 Lead Tracking Analytics Dashboard[/bold cyan]")
    
    data = db_manager.get_analytics_data()
    
    # 1. Total summary
    total_leads = sum(data["status_counts"].values())
    
    summary_text = (
        f"[bold]Total Leads in System:[/bold] {total_leads}\n"
        f"[bold]Total Potential Deal Value:[/bold] ₹{data['total_deal_value']:,.2f}"
    )
    console.print(Panel(summary_text, title="Overview", border_style="blue"))
    
    # 2. Status Breakdown Table
    status_table = Table(title="Leads by Status", show_header=True, header_style="bold magenta")
    status_table.add_column("Status", style="cyan")
    status_table.add_column("Count", justify="right")
    
    for status, count in sorted(data["status_counts"].items(), key=lambda x: x[1], reverse=True):
        status_table.add_row(status, str(count))
        
    console.print(status_table)
    
    # 3. Location Breakdown Table
    loc_table = Table(title="Top Locations for Prospects", show_header=True, header_style="bold green")
    loc_table.add_column("Location/Address", style="yellow")
    loc_table.add_column("Lead Count", justify="right")
    
    # Show top 10 locations
    sorted_locs = sorted(data["location_counts"].items(), key=lambda x: x[1], reverse=True)
    for loc, count in sorted_locs[:10]:
        loc_table.add_row(str(loc)[:50] + "..." if len(str(loc)) > 50 else str(loc), str(count))
        
    console.print(loc_table)
    console.print("\n[italic dim]Run this dashboard anytime to see your updated calling progress.[/italic dim]\n")

if __name__ == "__main__":
    generate_dashboard()
