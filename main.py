#!/usr/bin/env python3
"""Main entry point for Dunder Mifflin AI Office System."""

import sys
from app.system import DunderMifflinAIOfficeSystem
from colorama import Fore, Back, Style, init

init(autoreset=True)


def print_welcome():
    """Print welcome message."""
    print("\n" + "="*80)
    print(Back.BLUE + Fore.WHITE + f"{'WELCOME TO DUNDER MIFFLIN AI OFFICE SYSTEM':^80}" + Style.RESET_ALL)
    print("="*80)
    print("\nA fictional AI office simulation inspired by The Office.")
    print("\n" + Fore.CYAN + "Features:" + Style.RESET_ALL)
    print("  • 3 Regional Offices with specialized AI agents")
    print("  • Collective Intelligence Hub for consensus building")
    print("  • C-Suite Roundtable for strategic decision-making")
    print("  • Interactive Dashboard with real-time reporting")
    print("\n" + Fore.YELLOW + "Offices:" + Style.RESET_ALL)
    print("  📍 Scranton (Claude-like) - UI Testing & Creative Analysis")
    print("  📍 Stamford (GPT-like) - Infrastructure & Systematic Analysis")
    print("  📍 Corporate (Gemini-like) - Strategy & Holistic Review")
    print("\n" + Fore.MAGENTA + "C-Suite Members:" + Style.RESET_ALL)
    print("  👩 Michael Scott (CEO) - Vision & Direction")
    print("  👨 Nellie Bertram (CTO) - Technical Authority")
    print("  👨 Oscar Martinez (CFO) - Financial & Resources")
    print("  👨 Deangelo Vickers (COO) - Operations")
    print("  👨 Gabe Lewis (Chief AI Officer) - Collective Intelligence")
    print("\n" + "="*80 + "\n")


def main():
    """Main entry point."""
    print_welcome()
    
    # Initialize system
    print(Fore.CYAN + "🚀 Initializing Dunder Mifflin AI Office System..." + Style.RESET_ALL)
    system = DunderMifflinAIOfficeSystem()
    print(Fore.GREEN + "✓ System initialized successfully" + Style.RESET_ALL)
    
    # Display system status
    status = system.get_system_status()
    print(f"\n{Fore.YELLOW}System Status:{Style.RESET_ALL}")
    print(f"  Name: {status['system_name']}")
    print(f"  Version: {status['version']}")
    print(f"  Status: {Fore.GREEN}✓ OPERATIONAL{Style.RESET_ALL}")
    print(f"  Offices: {len(status['offices'])}")
    print(f"  Total Agents: 15")
    print(f"  C-Suite Members: 5")
    
    # Interactive menu
    print("\n" + Fore.CYAN + "Available Options:" + Style.RESET_ALL)
    print("  1. Run demo with example tasks")
    print("  2. Process a custom task")
    print("  3. View system status")
    print("  4. Exit")
    
    while True:
        choice = input(f"\n{Fore.YELLOW}Select option (1-4): {Style.RESET_ALL}").strip()
        
        if choice == "1":
            print(f"\n{Fore.CYAN}🎬 Running demonstration...{Style.RESET_ALL}")
            from app.system import demonstrate_system
            demonstrate_system()
            break
        
        elif choice == "2":
            task = input(f"\n{Fore.YELLOW}Enter task description: {Style.RESET_ALL}").strip()
            if task:
                print(f"\n{Fore.CYAN}🚀 Processing task...{Style.RESET_ALL}")
                result = system.process_task(task)
                system.display_full_report(result)
            else:
                print(Fore.RED + "Task cannot be empty." + Style.RESET_ALL)
        
        elif choice == "3":
            status = system.get_system_status()
            print(f"\n{Fore.GREEN}📋 System Status Report{Style.RESET_ALL}")
            print(f"  Operational: {Fore.GREEN}✓{Style.RESET_ALL}")
            print(f"  Tasks Processed: {status['tasks_processed']}")
            print(f"  Total Findings: {status['total_findings']}")
            print(f"  Uptime: {status['uptime_seconds']:.2f} seconds")
        
        elif choice == "4":
            print(f"\n{Fore.YELLOW}Exiting...{Style.RESET_ALL}")
            system.shutdown()
            break
        
        else:
            print(Fore.RED + "Invalid option. Please try again." + Style.RESET_ALL)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}\n🛑 System interrupted by user{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)
