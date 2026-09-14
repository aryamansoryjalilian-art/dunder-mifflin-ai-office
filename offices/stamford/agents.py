"""Stamford Office agents - Analytical, systematic, data-driven."""

import random
from typing import List, Dict, Any
from datetime import datetime
from models.agent import Agent, AgentRole, Finding
from models.response_templates import ResponseTemplates
from models.llm_simulator import LLMSimulator, LLMType


class JoshPorter:
    """Josh Porter - Stamford Manager & Analyzer"""
    
    def __init__(self):
        self.agent = Agent(
            name="Josh Porter",
            role=AgentRole.INVESTIGATOR,
            office="stamford",
            personality="Analytical, Strategic, Competitive",
            expertise=["Infrastructure Analysis", "System Design", "Performance Metrics"],
            llm_type="gpt"
        )
        self.llm = LLMSimulator(LLMType.GPT)
    
    def analyze_infrastructure(self, task_description: str) -> Finding:
        """Analyze infrastructure implications of the task."""
        self.agent.status = "analyzing"
        
        findings_list = [
            "Database query optimization required",
            "Load balancer configuration needs adjustment",
            "Cache invalidation strategy missing",
            "API rate limiting not properly configured",
            "Monitoring alerts not comprehensive"
        ]
        
        finding_text = random.choice(findings_list)
        metrics = random.choice(["10% performance degradation", "15% CPU spike", "Memory leak detected"])
        
        response = ResponseTemplates.get_stamford_response(
            "analysis",
            finding=finding_text,
            metrics=metrics,
            solution="Scale horizontally or optimize queries"
        )
        
        finding = Finding(
            timestamp=datetime.now(),
            agent_name="Josh Porter",
            agent_role=AgentRole.INVESTIGATOR,
            office="stamford",
            title=f"Infrastructure: {finding_text}",
            description=response,
            severity="warning",
            evidence=[f"Metrics: {metrics}", f"Task: {task_description}"],
            requires_validation=False
        )
        
        self.agent.add_finding(finding)
        self.agent.status = "idle"
        return finding


class KarenFilippelli:
    """Karen Filippelli - Stamford Performance Validator"""
    
    def __init__(self):
        self.agent = Agent(
            name="Karen Filippelli",
            role=AgentRole.VALIDATOR,
            office="stamford",
            personality="Precise, Detail-Focused, Professional",
            expertise=["Performance Testing", "Load Testing", "Benchmarking"],
            llm_type="gpt"
        )
        self.llm = LLMSimulator(LLMType.GPT)
    
    def validate_performance(self, finding: Finding) -> Finding:
        """Validate performance metrics and thresholds."""
        self.agent.status = "validating"
        
        test_results = [
            "Load test passed: 1000 concurrent users",
            "Response time: 250ms (SLA: 500ms) ✓",
            "Database connection pool optimized",
            "Cache hit ratio: 87% (Target: 80%+)",
        ]
        
        evidence = random.sample(test_results, 2)
        
        response = ResponseTemplates.get_stamford_response(
            "technical",
            verdict="Performance validation passed with flying colors",
            resources="CPU: 45%, Memory: 62%, Disk: 38%",
            scalability="System can handle 10x current load"
        )
        
        validation = Finding(
            timestamp=datetime.now(),
            agent_name="Karen Filippelli",
            agent_role=AgentRole.VALIDATOR,
            office="stamford",
            title=f"Performance Validated: {finding.title}",
            description=response,
            severity="info",
            evidence=evidence,
            recommendation="Approved for production deployment"
        )
        
        self.agent.add_finding(validation)
        self.agent.status = "idle"
        return validation


class ValCummings:
    """Val Cummings - Stamford Security Expert"""
    
    def __init__(self):
        self.agent = Agent(
            name="Val Cummings",
            role=AgentRole.VALIDATOR,
            office="stamford",
            personality="Vigilant, Security-Minded, Thorough",
            expertise=["Security Testing", "Vulnerability Assessment", "Compliance"],
            llm_type="gpt"
        )
        self.llm = LLMSimulator(LLMType.GPT)
    
    def security_audit(self, finding: Finding) -> Finding:
        """Perform security audit on findings."""
        self.agent.status = "auditing"
        
        security_checks = [
            "SQL injection prevention verified",
            "XSS protection enabled",
            "CSRF tokens properly implemented",
            "Authentication flow secure",
            "Data encryption in transit and at rest",
        ]
        
        checks_passed = random.sample(security_checks, 3)
        potential_issue = random.choice([
            "Session timeout needs adjustment",
            "API keys should be rotated",
            "SSL/TLS certificate expiring in 60 days"
        ])
        
        response = ResponseTemplates.get_stamford_response(
            "analysis",
            finding="Security audit completed with recommendations",
            metrics="OWASP Top 10: Compliant",
            solution="Address identified issues before production"
        )
        
        security = Finding(
            timestamp=datetime.now(),
            agent_name="Val Cummings",
            agent_role=AgentRole.VALIDATOR,
            office="stamford",
            title=f"Security Audit: {finding.title}",
            description=response,
            severity="warning",
            evidence=checks_passed + [potential_issue],
            recommendation="Fix security issues before deployment"
        )
        
        self.agent.add_finding(security)
        self.agent.status = "idle"
        return security


class HidetoshiHasagawa:
    """Hidetoshi Hasagawa - Stamford DevOps Expert"""
    
    def __init__(self):
        self.agent = Agent(
            name="Hidetoshi Hasagawa",
            role=AgentRole.AUTOMATOR,
            office="stamford",
            personality="Meticulous, Innovative, Process-Driven",
            expertise=["DevOps", "CI/CD Pipeline", "Infrastructure Automation"],
            llm_type="gpt"
        )
        self.llm = LLMSimulator(LLMType.GPT)
    
    def automate_deployment(self, findings: List[Finding]) -> Finding:
        """Create automated deployment pipeline."""
        self.agent.status = "automating"
        
        pipeline_steps = [
            "GitHub Actions workflow created",
            "Docker container optimized",
            "Terraform infrastructure-as-code generated",
            "Kubernetes deployment manifests prepared",
            "Health checks and monitoring configured",
        ]
        
        response = ResponseTemplates.get_stamford_response(
            "technical",
            verdict="Deployment automation complete",
            resources="Pipeline execution time: 5 minutes",
            scalability="Auto-scaling configured for peak load"
        )
        
        automation = Finding(
            timestamp=datetime.now(),
            agent_name="Hidetoshi Hasagawa",
            agent_role=AgentRole.AUTOMATOR,
            office="stamford",
            title="DevOps Pipeline Automated",
            description=response,
            severity="info",
            evidence=pipeline_steps,
            recommendation="Ready for continuous deployment"
        )
        
        self.agent.add_finding(automation)
        self.agent.status = "idle"
        return automation


class StamfordOffice:
    """Stamford Office - Infrastructure & Backend Hub"""
    
    def __init__(self):
        self.name = "Stamford Branch"
        self.location = "Stamford, Connecticut"
        self.manager = "Josh Porter"
        self.llm_type = "GPT-like"
        
        self.josh = JoshPorter()
        self.karen = KarenFilippelli()
        self.val = ValCummings()
        self.hidetoshi = HidetoshiHasagawa()
        
        self.agents = [self.josh.agent, self.karen.agent, self.val.agent, self.hidetoshi.agent]
    
    def process_task(self, task_description: str) -> Dict[str, Any]:
        """Process a task through the Stamford office workflow."""
        findings = []
        
        # Analysis phase
        finding1 = self.josh.analyze_infrastructure(task_description)
        findings.append(finding1)
        
        # Performance validation
        finding2 = self.karen.validate_performance(finding1)
        findings.append(finding2)
        
        # Security audit
        finding3 = self.val.security_audit(finding1)
        findings.append(finding3)
        
        # DevOps automation
        finding4 = self.hidetoshi.automate_deployment(findings)
        findings.append(finding4)
        
        return {
            "office": self.name,
            "manager": self.manager,
            "llm_type": self.llm_type,
            "findings": findings,
            "total_findings": len(findings)
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
