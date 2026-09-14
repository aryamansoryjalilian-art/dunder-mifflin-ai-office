"""Main application - System orchestration and workflow."""

from typing import Dict, Any
from datetime import datetime
from offices.scranton.agents import ScantonOffice
from offices.stamford.agents import StamfordOffice
from offices.corporate.agents import CorporateOffice
from intelligence.hub import CollectiveIntelligenceHub
from dashboard.cli import Dashboard, InteractiveMenu


class DunderMifflinAIOfficeSystem:
    """Main system orchestrator for Dunder Mifflin AI Office."""
    
    def __init__(self):
        self.name = "Dunder Mifflin AI Office System"
        self.version = "1.0.0"
        self.start_time = datetime.now()
        
        # Initialize offices
        self.scranton = ScantonOffice()
        self.stamford = StamfordOffice()
        self.corporate = CorporateOffice()
        
        # Initialize collective intelligence hub
        self.intelligence_hub = CollectiveIntelligenceHub()
        
        # Initialize dashboard
        self.dashboard = Dashboard()
        
        self.system_log = []
        self.operational = True
    
    def process_task(self, task_description: str) -> Dict[str, Any]:
        """Process a task through the entire system."""
        
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "task": task_description,
            "stages": {}
        }
        
        print(f"\n🚀 Starting task processing: {task_description}")
        
        # Stage 1: Scranton Office Processing
        print("\n📍 Stage 1: Scranton Office (UI Testing)")
        scranton_result = self.scranton.process_task(task_description)
        scranton_findings = scranton_result["findings"]
        log_entry["stages"]["scranton"] = scranton_result
        print(f"   ✓ Found {len(scranton_findings)} issues")
        
        # Stage 2: Stamford Office Processing
        print("\n📍 Stage 2: Stamford Office (Infrastructure)")
        stamford_result = self.stamford.process_task(task_description)
        stamford_findings = stamford_result["findings"]
        log_entry["stages"]["stamford"] = stamford_result
        print(f"   ✓ Analyzed {len(stamford_findings)} infrastructure aspects")
        
        # Stage 3: Corporate Office Processing
        print("\n📍 Stage 3: Corporate Office (Strategy)")
        corporate_result = self.corporate.process_findings(
            scranton_findings,
            stamford_findings
        )
        corporate_findings = corporate_result["findings"]
        log_entry["stages"]["corporate"] = corporate_result
        print(f"   ✓ Reviewed {len(corporate_findings)} strategic aspects")
        
        # Stage 4: Collective Intelligence Hub
        print("\n📍 Stage 4: Collective Intelligence Hub")
        intelligence_result = self.intelligence_hub.process_all_findings(
            scranton_findings,
            stamford_findings,
            corporate_findings
        )
        log_entry["stages"]["intelligence_hub"] = intelligence_result
        print(f"   ✓ Aggregated findings: {intelligence_result['stage_1_aggregation']['total_findings']}")
        print(f"   ✓ Consensus score: {intelligence_result['stage_2_consensus']['consensus_score']}/100")
        print(f"   ✓ Final decision: {intelligence_result['final_decision']}")
        
        self.system_log.append(log_entry)
        
        return {
            "task": task_description,
            "completion_time": datetime.now().isoformat(),
            "scranton": scranton_result,
            "stamford": stamford_result,
            "corporate": corporate_result,
            "intelligence_hub": intelligence_result,
            "status": "COMPLETED"
        }
    
    def display_full_report(self, result: Dict[str, Any]):
        """Display complete system report using dashboard."""
        scranton_data = {"office_status": self.scranton.get_status()}
        stamford_data = {"office_status": self.stamford.get_status()}
        corporate_data = {"office_status": self.corporate.get_status()}
        
        aggregated = result["intelligence_hub"]["stage_1_aggregation"]
        consensus = result["intelligence_hub"]["stage_2_consensus"]
        roundtable = result["intelligence_hub"]["stage_3_roundtable"]
        
        self.dashboard.display_full_report(
            scranton_data,
            stamford_data,
            corporate_data,
            aggregated,
            consensus,
            roundtable
        )
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get complete system status."""
        uptime = (datetime.now() - self.start_time).total_seconds()
        
        return {
            "system_name": self.name,
            "version": self.version,
            "operational": self.operational,
            "uptime_seconds": uptime,
            "offices": {
                "scranton": self.scranton.get_status(),
                "stamford": self.stamford.get_status(),
                "corporate": self.corporate.get_status()
            },
            "intelligence_hub": self.intelligence_hub.get_status(),
            "tasks_processed": len(self.system_log),
            "total_findings": sum(
                sum(len(agent.findings) for agent in office.agents)
                for office in [self.scranton, self.stamford, self.corporate]
            )
        }
    
    def shutdown(self):
        """Shutdown the system gracefully."""
        print("\n🛑 Shutting down Dunder Mifflin AI Office System...")
        self.operational = False
        print("✓ System shutdown complete")
        print(f"  Total tasks processed: {len(self.system_log)}")
        print(f"  Uptime: {(datetime.now() - self.start_time).total_seconds():.2f} seconds")


def demonstrate_system():
    """Demonstrate the complete system with example scenarios."""
    
    print("\n" + "="*80)
    print("🎬 DUNDER MIFFLIN AI OFFICE SYSTEM - LIVE DEMONSTRATION")
    print("="*80)
    
    # Initialize system
    system = DunderMifflinAIOfficeSystem()
    
    # Display system status
    print("\n📊 System Status:")
    status = system.get_system_status()
    print(f"  System: {status['system_name']} v{status['version']}")
    print(f"  Status: {'🟢 OPERATIONAL' if status['operational'] else '🔴 DOWN'}")
    print(f"  Offices: {len(status['offices'])}")
    print(f"  Agents: 15")
    print(f"  C-Suite Members: 5")
    
    # Example task 1
    print("\n" + "-"*80)
    task_1 = "Implement new API authentication mechanism with JWT tokens"
    result_1 = system.process_task(task_1)
    system.display_full_report(result_1)
    
    # Example task 2
    print("\n" + "-"*80)
    task_2 = "Redesign user dashboard with improved performance metrics"
    result_2 = system.process_task(task_2)
    system.display_full_report(result_2)
    
    # Final system status
    print("\n" + "="*80)
    print("📋 FINAL SYSTEM STATUS")
    print("="*80)
    final_status = system.get_system_status()
    print(f"  Tasks Processed: {final_status['tasks_processed']}")
    print(f"  Total Findings: {final_status['total_findings']}")
    print(f"  System Operational: {'✓ Yes' if final_status['operational'] else '✗ No'}")
    
    # Shutdown
    system.shutdown()


if __name__ == "__main__":
    demonstrate_system()
