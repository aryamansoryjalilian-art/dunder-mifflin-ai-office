"""Scranton Office agents - Creative, detailed, community-oriented."""

import random
from typing import List, Dict, Any
from datetime import datetime
from models.agent import Agent, AgentRole, Finding
from models.response_templates import ResponseTemplates
from models.llm_simulator import LLMSimulator, LLMType


class JimHalpert:
    """Jim Halpert - Scranton Manager & Discoverer"""
    
    def __init__(self):
        self.agent = Agent(
            name="Jim Halpert",
            role=AgentRole.DISCOVERER,
            office="scranton",
            personality="Charming, Insightful, Practical",
            expertise=["UI Testing", "User Flow Analysis", "Experience Design"],
            llm_type="claude"
        )
        self.llm = LLMSimulator(LLMType.CLAUDE)
    
    def discover_issue(self, task_description: str) -> Finding:
        """Discover potential issues in the task."""
        self.agent.status = "working"
        
        issues = [
            "UI button missing hover state",
            "Form validation not triggering on blur",
            "Mobile responsiveness issue on smaller screens",
            "Accessibility: missing alt text on images",
            "User flow breaks at checkout"
        ]
        
        issue = random.choice(issues)
        reason = "improper event listener" if "blur" in issue else "CSS media query missing"
        
        response = ResponseTemplates.get_scranton_response(
            "discovery",
            issue=issue,
            reason=reason
        )
        
        finding = Finding(
            timestamp=datetime.now(),
            agent_name="Jim Halpert",
            agent_role=AgentRole.DISCOVERER,
            office="scranton",
            title=f"Discovered: {issue}",
            description=response,
            severity="warning",
            evidence=[f"Issue found during {task_description}"],
            requires_validation=True
        )
        
        self.agent.add_finding(finding)
        self.agent.status = "idle"
        return finding


class PamBeesly:
    """Pam Beesly - Scranton API Investigator"""
    
    def __init__(self):
        self.agent = Agent(
            name="Pam Beesly",
            role=AgentRole.INVESTIGATOR,
            office="scranton",
            personality="Thoughtful, Detail-Oriented, Empathetic",
            expertise=["API Testing", "Data Validation", "Integration Testing"],
            llm_type="claude"
        )
        self.llm = LLMSimulator(LLMType.CLAUDE)
    
    def investigate_finding(self, finding: Finding) -> Finding:
        """Deep dive investigation of a finding."""
        self.agent.status = "investigating"
        
        investigations = [
            "API endpoint returns 200 but data structure is malformed",
            "Response time exceeds SLA by 40%",
            "Backend not handling concurrent requests properly",
            "Database query is missing index, causing slowdown",
        ]
        
        investigation = random.choice(investigations)
        evidence = [
            "API logs show 15 failed requests in last hour",
            "Response time average: 2500ms (SLA: 1500ms)",
            "Database query time: 800ms"
        ]
        
        response = ResponseTemplates.get_scranton_response(
            "investigation",
            finding=investigation,
            evidence="\n  - ".join(evidence)
        )
        
        investigation_finding = Finding(
            timestamp=datetime.now(),
            agent_name="Pam Beesly",
            agent_role=AgentRole.INVESTIGATOR,
            office="scranton",
            title=f"Investigation: {finding.title}",
            description=response,
            severity="warning",
            evidence=evidence,
            recommendation="Further testing required at backend",
            requires_validation=True
        )
        
        self.agent.add_finding(investigation_finding)
        self.agent.status = "idle"
        return investigation_finding


class DwightSchrute:
    """Dwight Schrute - Scranton Automation Expert"""
    
    def __init__(self):
        self.agent = Agent(
            name="Dwight Schrute",
            role=AgentRole.AUTOMATOR,
            office="scranton",
            personality="Intense, Disciplined, Competitive",
            expertise=["Test Automation", "Framework Design", "Regression Testing"],
            llm_type="claude"
        )
        self.llm = LLMSimulator(LLMType.CLAUDE)
    
    def create_automation(self, finding: Finding) -> Finding:
        """Create automated test for the finding."""
        self.agent.status = "automating"
        
        automation_types = [
            "Selenium test for UI validation",
            "Pytest unit test for API contract",
            "Performance test using Locust",
            "Accessibility audit using axe-core",
        ]
        
        automation = random.choice(automation_types)
        
        finding_auto = Finding(
            timestamp=datetime.now(),
            agent_name="Dwight Schrute",
            agent_role=AgentRole.AUTOMATOR,
            office="scranton",
            title=f"Automated: {finding.title}",
            description=f"Created {automation} to prevent regression. Test will run on every commit.",
            severity="info",
            evidence=[automation, "Test coverage: 95%"],
            recommendation="Add to CI/CD pipeline"
        )
        
        self.agent.add_finding(finding_auto)
        self.agent.status = "idle"
        return finding_auto


class RyanHoward:
    """Ryan Howard - Scranton Documentation Expert"""
    
    def __init__(self):
        self.agent = Agent(
            name="Ryan Howard",
            role=AgentRole.REPORTER,
            office="scranton",
            personality="Ambitious, Tech-Savvy, Opinionated",
            expertise=["Documentation", "Technical Writing", "Reporting"],
            llm_type="claude"
        )
        self.llm = LLMSimulator(LLMType.CLAUDE)
    
    def document_findings(self, findings: List[Finding]) -> Dict[str, Any]:
        """Document all findings in a comprehensive report."""
        self.agent.status = "documenting"
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "office": "Scranton",
            "findings_count": len(findings),
            "critical_issues": len([f for f in findings if f.severity == "critical"]),
            "warnings": len([f for f in findings if f.severity == "warning"]),
            "infos": len([f for f in findings if f.severity == "info"]),
            "summary": f"Scranton office discovered {len(findings)} findings requiring attention.",
            "findings": [f.to_dict() for f in findings],
            "generated_by": "Ryan Howard"
        }
        
        self.agent.status = "idle"
        return report


class ScantonOffice:
    """Scranton Office - Functional Testing Hub"""
    
    def __init__(self):
        self.name = "Scranton Branch"
        self.location = "Scranton, Pennsylvania"
        self.manager = "Jim Halpert"
        self.llm_type = "Claude-like"
        
        self.jim = JimHalpert()
        self.pam = PamBeesly()
        self.dwight = DwightSchrute()
        self.ryan = RyanHoward()
        
        self.agents = [self.jim.agent, self.pam.agent, self.dwight.agent, self.ryan.agent]
    
    def process_task(self, task_description: str) -> Dict[str, Any]:
        """Process a task through the Scranton office workflow."""
        findings = []
        
        # Discovery phase
        finding1 = self.jim.discover_issue(task_description)
        findings.append(finding1)
        
        # Investigation phase
        finding2 = self.pam.investigate_finding(finding1)
        findings.append(finding2)
        
        # Automation phase
        finding3 = self.dwight.create_automation(finding1)
        findings.append(finding3)
        
        # Documentation phase
        report = self.ryan.document_findings(findings)
        
        return {
            "office": self.name,
            "manager": self.manager,
            "llm_type": self.llm_type,
            "findings": findings,
            "report": report
        }
    
    def get_status(self) -> Dict[str, Any]:
        """Get current status of the office."""
        return {
            "name": self.name,
            "location": self.location,
            "manager": self.manager,
            "agents": [str(agent) for agent in self.agents],
            "total_findings": sum(len(agent.findings) for agent in self.agents)
        }
