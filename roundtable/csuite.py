"""C-Suite Roundtable - Collective Intelligence & Decision Making."""

import random
from typing import List, Dict, Any
from datetime import datetime
from models.agent import Finding
from models.response_templates import ResponseTemplates


class CSuiteExecutive:
    """Base class for C-Suite executives."""
    
    def __init__(self, name: str, role: str, focus: str):
        self.name = name
        self.role = role
        self.focus = focus
        self.position = f"{role} ({name})"
        self.opinions = []
    
    def provide_perspective(self, topic: str, findings: List[Finding]) -> str:
        """Provide perspective on a topic."""
        raise NotImplementedError


class MichaelScott(CSuiteExecutive):
    """Michael Scott - CEO (Vision & Direction)"""
    
    def __init__(self):
        super().__init__("Michael Scott", "CEO", "Vision & Direction")
    
    def provide_perspective(self, topic: str, findings: List[Finding]) -> str:
        """CEO provides visionary perspective."""
        perspectives = [
            f"Okay people, here's what I'm thinking - we need to make this *great*. {topic} is our moment. "
            f"Everyone's going to remember this. Let's be bold!",
            
            f"That's what she said! *laughs* But seriously, {topic}... This is exactly what we need to "
            f"take Dunder Mifflin to the next level. Vision accomplished!",
            
            f"You know what? The findings show we're on the right path with {topic}. "
            f"I'm going to make an executive decision here - let's do this with confidence!",
        ]
        return random.choice(perspectives)


class NellieBertram(CSuiteExecutive):
    """Nellie Bertram - CTO (Technical Authority)"""
    
    def __init__(self):
        super().__init__("Nellie Bertram", "CTO", "Technical Authority")
    
    def provide_perspective(self, topic: str, findings: List[Finding]) -> str:
        """CTO provides technical perspective."""
        perspectives = [
            f"From a technical standpoint, {topic} requires attention to {random.choice(['scalability', 'reliability', 'security'])}. "
            f"The architecture needs to support our growth trajectory. Implementation should follow best practices.",
            
            f"Technical requirements for {topic}: We need robust infrastructure, proper monitoring, "
            f"and failover mechanisms. Let's ensure we're building for the long term.",
            
            f"The technical implications of {topic} are significant. I recommend we prioritize "
            f"infrastructure improvements and establish clear technical standards.",
        ]
        return random.choice(perspectives)


class OscarMartinez(CSuiteExecutive):
    """Oscar Martinez - CFO (Financial & Resources)"""
    
    def __init__(self):
        super().__init__("Oscar Martinez", "CFO", "Financial & Resources")
    
    def provide_perspective(self, topic: str, findings: List[Finding]) -> str:
        """CFO provides financial perspective."""
        perspectives = [
            f"Let's look at the numbers for {topic}. Budget allocation: we need to be smart about resources. "
            f"ROI projection looks positive if we execute properly. Cost-benefit analysis is favorable.",
            
            f"From a financial perspective, {topic} offers good returns. We should allocate resources strategically "
            f"to maximize impact while maintaining fiscal responsibility.",
            
            f"The financial impact of {topic} depends on execution. We need to track costs carefully and "
            f"ensure we're optimizing resource utilization across all three offices.",
        ]
        return random.choice(perspectives)


class DeangeloVickers(CSuiteExecutive):
    """Deangelo Vickers - COO (Operations)"""
    
    def __init__(self):
        super().__init__("Deangelo Vickers", "COO", "Operations")
    
    def provide_perspective(self, topic: str, findings: List[Finding]) -> str:
        """COO provides operational perspective."""
        perspectives = [
            f"Operationally, {topic} requires coordination across all offices. Timeline and contingencies "
            f"must be established. We need to ensure smooth execution and risk mitigation.",
            
            f"The operational plan for {topic}: We'll need to synchronize efforts across Scranton, Stamford, "
            f"and Corporate. Process optimization and efficiency are key to success.",
            
            f"Let me break down the operations: {topic} needs clear milestones, assigned owners, and "
            f"contingency plans. We'll run this like a well-oiled machine.",
        ]
        return random.choice(perspectives)


class GabeLewis(CSuiteExecutive):
    """Gabe Lewis - Chief AI Officer (Collective Intelligence Orchestrator)"""
    
    def __init__(self):
        super().__init__("Gabe Lewis", "Chief AI Officer", "Collective Intelligence")
    
    def provide_perspective(self, topic: str, findings: List[Finding]) -> str:
        """CAIO orchestrates collective intelligence."""
        critical = len([f for f in findings if f.severity == "critical"])
        warnings = len([f for f in findings if f.severity == "warning"])
        consensus_level = random.randint(75, 98)
        
        perspectives = [
            f"Collective Intelligence Assessment: {topic} has been analyzed by all three offices. "
            f"Critical findings: {critical}, Warnings: {warnings}. Consensus level: {consensus_level}%. "
            f"Recommendation: Proceed with coordinated implementation.",
            
            f"The aggregated intelligence from our offices shows {topic} is well-analyzed. "
            f"Agent alignment across Scranton, Stamford, and Corporate: {consensus_level}%. "
            f"We have strong confidence in the recommendations.",
            
            f"Orchestration status: All agents have provided their analysis on {topic}. "
            f"Cross-office consensus: {consensus_level}%. Recommendation confidence: High. "
            f"We're ready for C-Suite decision.",
        ]
        return random.choice(perspectives)


class CSuiteRoundtable:
    """C-Suite Roundtable - Strategic Decision Making Body"""
    
    def __init__(self):
        self.name = "C-Suite Roundtable"
        self.ceo = MichaelScott()
        self.cto = NellieBertram()
        self.cfo = OscarMartinez()
        self.coo = DeangeloVickers()
        self.caio = GabeLewis()
        
        self.executives = [self.ceo, self.cto, self.cfo, self.coo, self.caio]
        self.decisions = []
    
    def conduct_roundtable(self, topic: str, findings: List[Finding]) -> Dict[str, Any]:
        """Conduct a full roundtable discussion."""
        roundtable_record = {
            "timestamp": datetime.now().isoformat(),
            "topic": topic,
            "total_findings": len(findings),
            "participants": [exec.position for exec in self.executives],
            "discussion": [],
            "decision": None,
            "confidence_level": 0
        }
        
        # Each executive provides perspective
        for executive in self.executives:
            perspective = executive.provide_perspective(topic, findings)
            roundtable_record["discussion"].append({
                "executive": executive.position,
                "perspective": perspective
            })
        
        # CAIO makes final recommendation
        recommendation = self._build_consensus(topic, findings)
        roundtable_record["final_recommendation"] = recommendation
        roundtable_record["decision"] = recommendation["decision"]
        roundtable_record["confidence_level"] = recommendation["confidence"]
        
        self.decisions.append(roundtable_record)
        return roundtable_record
    
    def _build_consensus(self, topic: str, findings: List[Finding]) -> Dict[str, Any]:
        """Build consensus from all perspectives."""
        critical_count = len([f for f in findings if f.severity == "critical"])
        warning_count = len([f for f in findings if f.severity == "warning"])
        
        if critical_count > 2:
            decision = "DEFER - Address critical issues first"
            confidence = random.randint(60, 75)
        elif warning_count > 5:
            decision = "CONDITIONAL - Proceed with caution and monitoring"
            confidence = random.randint(75, 85)
        else:
            decision = "APPROVE - Proceed with full implementation"
            confidence = random.randint(85, 98)
        
        return {
            "decision": decision,
            "confidence": confidence,
            "rationale": f"After thorough analysis by all offices and C-Suite discussion, "
                        f"we recommend: {decision}",
            "next_steps": [
                "Implementation team to begin Phase 1 planning",
                "Monitor key metrics closely",
                "Schedule follow-up roundtable in 2 weeks"
            ] if "APPROVE" in decision else [
                "Address identified issues",
                "Reconvene C-Suite in 1 week",
                "Prepare remediation plan"
            ]
        }
    
    def get_meeting_notes(self) -> List[Dict[str, Any]]:
        """Get all meeting notes from roundtable discussions."""
        return self.decisions
    
    def get_status(self) -> Dict[str, Any]:
        """Get current status of the roundtable."""
        return {
            "name": self.name,
            "executives": len(self.executives),
            "meetings_held": len(self.decisions),
            "recent_decision": self.decisions[-1]["decision"] if self.decisions else "No decisions yet"
        }
