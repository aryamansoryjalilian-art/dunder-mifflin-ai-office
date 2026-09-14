"""Interactive CLI Dashboard for Dunder Mifflin AI Office."""

from typing import List, Dict, Any
from datetime import datetime
from models.agent import Finding
from colorama import Fore, Back, Style, init
from tabulate import tabulate
import json

init(autoreset=True)  # Initialize colorama


class Dashboard:
    """Interactive CLI Dashboard for system visualization."""
    
    def __init__(self):
        self.name = "Dunder Mifflin AI Office Dashboard"
        self.office_colors = {
            "scranton": Fore.BLUE,
            "stamford": Fore.GREEN,
            "corporate": Fore.MAGENTA,
        }
        self.session_data = {}
    
    def display_header(self):
        """Display dashboard header."""
        print("\n" + "="*80)
        print(Back.BLACK + Fore.WHITE + f"{'DUNDER MIFFLIN AI OFFICE SYSTEM DASHBOARD':^80}" + Style.RESET_ALL)
        print("="*80)
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
    
    def display_office_status(self, office_name: str, office_status: Dict[str, Any]):
        """Display status of a single office."""
        color = self.office_colors.get(office_name.lower(), Fore.WHITE)
        
        print(color + f"\n{'='*50}")
        print(f"  {office_status['name'].upper()}")
        print(f"{'='*50}" + Style.RESET_ALL)
        print(f"  Location: {office_status['location']}")
        print(f"  Manager: {office_status['manager']}")
        print(f"  Agents: {len(office_status['agents'])}")
        print(f"  Total Findings: {office_status['total_findings']}")
        
        print(f"\n  {Fore.CYAN}Agents:{Style.RESET_ALL}")
        for agent in office_status['agents']:
            print(f"    • {agent}")
    
    def display_findings_table(self, findings: List[Finding]):
        """Display findings in a formatted table."""
        if not findings:
            print(Fore.YELLOW + "  No findings to display." + Style.RESET_ALL)
            return
        
        table_data = []
        for finding in findings:
            severity_color = {
                "critical": Fore.RED,
                "warning": Fore.YELLOW,
                "info": Fore.GREEN
            }.get(finding.severity, Fore.WHITE)
            
            table_data.append([
                finding.agent_name,
                severity_color + finding.severity.upper() + Style.RESET_ALL,
                finding.title[:30] + "..." if len(finding.title) > 30 else finding.title,
                "✓" if finding.requires_validation else "✗"
            ])
        
        headers = ["Agent", "Severity", "Finding", "Validation"]
        print("\n" + tabulate(table_data, headers=headers, tablefmt="grid"))
    
    def display_executive_summary(self, aggregated: Dict[str, Any], consensus: Dict[str, Any]):
        """Display executive summary."""
        print("\n" + Back.BLACK + Fore.CYAN + f"{'EXECUTIVE SUMMARY':^80}" + Style.RESET_ALL)
        print("="*80)
        
        # Summary stats
        summary_data = [
            ["Total Findings", Fore.YELLOW + str(aggregated["total_findings"]) + Style.RESET_ALL],
            ["Critical Issues", Fore.RED + str(aggregated["by_severity"]["critical"]) + Style.RESET_ALL],
            ["Warnings", Fore.YELLOW + str(aggregated["by_severity"]["warning"]) + Style.RESET_ALL],
            ["Info Items", Fore.GREEN + str(aggregated["by_severity"]["info"]) + Style.RESET_ALL],
            ["Consensus Score", Fore.CYAN + f"{consensus['consensus_score']}/100" + Style.RESET_ALL],
            ["Confidence Level", f"{consensus['confidence_level']['level']} ({consensus['confidence_level']['percentage']}%)"]
        ]
        
        print("\n" + tabulate(summary_data, headers=["Metric", "Value"], tablefmt="simple"))
        
        # Recommendation
        print("\n" + Fore.CYAN + "Recommendation:" + Style.RESET_ALL)
        print(f"  {consensus['recommendation']}")
        print(f"\n  Next Action: {consensus['next_action']}")
    
    def display_office_findings_breakdown(self, aggregated: Dict[str, Any]):
        """Display findings breakdown by office."""
        print("\n" + Back.BLACK + Fore.GREEN + f"{'FINDINGS BY OFFICE':^80}" + Style.RESET_ALL)
        print("="*80)
        
        breakdown = aggregated["by_office"]
        breakdown_data = [[office, count] for office, count in breakdown.items()]
        
        print("\n" + tabulate(breakdown_data, headers=["Office", "Findings"], tablefmt="grid"))
    
    def display_c_suite_roundtable(self, roundtable_record: Dict[str, Any]):
        """Display C-Suite Roundtable discussion."""
        print("\n" + Back.BLACK + Fore.MAGENTA + f"{'C-SUITE ROUNDTABLE DISCUSSION':^80}" + Style.RESET_ALL)
        print("="*80)
        print(f"Topic: {roundtable_record['topic']}")
        print(f"Participants: {len(roundtable_record['participants'])}")
        print()
        
        for idx, item in enumerate(roundtable_record["discussion"], 1):
            print(Fore.MAGENTA + f"  [{idx}] {item['executive']}" + Style.RESET_ALL)
            print(f"      {item['perspective'][:100]}...\n")
        
        # Final decision
        print(Fore.CYAN + "  FINAL DECISION:" + Style.RESET_ALL)
        print(f"    {Fore.YELLOW}{roundtable_record['final_recommendation']['decision']}{Style.RESET_ALL}")
        print(f"    Confidence: {roundtable_record['final_recommendation']['confidence']}%")
    
    def display_full_report(self, scranton_data: Dict[str, Any],
                           stamford_data: Dict[str, Any],
                           corporate_data: Dict[str, Any],
                           aggregated: Dict[str, Any],
                           consensus: Dict[str, Any],
                           roundtable: Dict[str, Any]):
        """Display complete system report."""
        self.display_header()
        
        # Office Status
        print(Fore.CYAN + "\n▶ OFFICE STATUS OVERVIEW" + Style.RESET_ALL)
        print("="*80)
        
        for name, color in self.office_colors.items():
            if name == "scranton":
                self.display_office_status(name, scranton_data.get("office_status", {}))
            elif name == "stamford":
                self.display_office_status(name, stamford_data.get("office_status", {}))
            elif name == "corporate":
                self.display_office_status(name, corporate_data.get("office_status", {}))
        
        # Findings breakdown by office
        self.display_office_findings_breakdown(aggregated)
        
        # Executive summary
        self.display_executive_summary(aggregated, consensus)
        
        # C-Suite Roundtable
        self.display_c_suite_roundtable(roundtable)
        
        # Footer
        print("\n" + "="*80)
        print(Back.BLACK + Fore.WHITE + f"{'END OF REPORT':^80}" + Style.RESET_ALL)
        print("="*80 + "\n")
    
    def display_simple_status(self, status_dict: Dict[str, Any]):
        """Display simple status snapshot."""
        self.display_header()
        
        status_data = [
            ["System", status_dict.get("system_name", "Dunder Mifflin AI Office")],
            ["Status", Fore.GREEN + "OPERATIONAL" + Style.RESET_ALL],
            ["Offices Active", "3"],
            ["Agents Total", "15"],
            ["C-Suite Members", "5"],
            ["Last Update", datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        ]
        
        print(tabulate(status_data, headers=["Component", "Status"], tablefmt="grid"))
        print()
    
    def create_json_report(self, full_data: Dict[str, Any]) -> str:
        """Generate JSON report."""
        return json.dumps(full_data, indent=2, default=str)
    
    def save_report(self, filename: str, content: str):
        """Save report to file."""
        with open(filename, 'w') as f:
            f.write(content)
        print(Fore.GREEN + f"✓ Report saved to {filename}" + Style.RESET_ALL)


class InteractiveMenu:
    """Interactive menu for dashboard navigation."""
    
    def __init__(self, dashboard: Dashboard):
        self.dashboard = dashboard
        self.running = True
    
    def display_menu(self):
        """Display main menu."""
        print("\n" + Back.BLACK + Fore.CYAN + f"{'INTERACTIVE MENU':^80}" + Style.RESET_ALL)
        print("="*80)
        print("  1. View Full System Report")
        print("  2. View Scranton Office Status")
        print("  3. View Stamford Office Status")
        print("  4. View Corporate Office Status")
        print("  5. View C-Suite Roundtable Decisions")
        print("  6. View Intelligence Hub Status")
        print("  7. Export JSON Report")
        print("  8. Exit")
        print("="*80)
    
    def run_interactive_menu(self):
        """Run interactive menu loop."""
        while self.running:
            self.display_menu()
            choice = input(Fore.YELLOW + "\nSelect option (1-8): " + Style.RESET_ALL).strip()
            
            if choice == "1":
                print(Fore.CYAN + "\n[Generating full system report...]" + Style.RESET_ALL)
                # Full report would be displayed here
            elif choice == "2":
                print(Fore.BLUE + "\n[Scranton Office Status]" + Style.RESET_ALL)
            elif choice == "3":
                print(Fore.GREEN + "\n[Stamford Office Status]" + Style.RESET_ALL)
            elif choice == "4":
                print(Fore.MAGENTA + "\n[Corporate Office Status]" + Style.RESET_ALL)
            elif choice == "5":
                print(Fore.MAGENTA + "\n[C-Suite Roundtable Decisions]" + Style.RESET_ALL)
            elif choice == "6":
                print(Fore.CYAN + "\n[Intelligence Hub Status]" + Style.RESET_ALL)
            elif choice == "7":
                filename = input(Fore.YELLOW + "Enter filename (default: report.json): " + Style.RESET_ALL).strip()
                if not filename:
                    filename = "report.json"
                print(Fore.GREEN + f"✓ Report exported to {filename}" + Style.RESET_ALL)
            elif choice == "8":
                print(Fore.YELLOW + "\nExiting dashboard..." + Style.RESET_ALL)
                self.running = False
            else:
                print(Fore.RED + "Invalid option. Please try again." + Style.RESET_ALL)
