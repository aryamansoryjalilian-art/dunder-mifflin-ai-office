"""Collective Intelligence Hub - Aggregation and Consensus Engine."""

import random
from typing import List, Dict, Any, Tuple
from datetime import datetime
from models.agent import Finding
from roundtable.csuite import CSuiteRoundtable


class IntelligenceAggregator:
    """Aggregates findings from all offices."""
    
    def __init__(self):
        self.name = "Intelligence Aggregator"
        self.aggregated_findings = []
        self.analysis_log = []
    
    def aggregate(self, *office_findings_lists) -> Dict[str, Any]:
        """Aggregate findings from multiple offices."""
        all_findings = []
        office_names = ["Scranton", "Stamford", "Corporate"]
        
        for idx, findings_list in enumerate(office_findings_lists):
            all_findings.extend(findings_list)
        
        aggregation = {
            "timestamp": datetime.now().isoformat(),
            "total_findings": len(all_findings),
            "by_severity": self._categorize_by_severity(all_findings),
            "by_office": self._categorize_by_office(all_findings),
            "findings": all_findings,
            "aggregation_metrics": self._calculate_metrics(all_findings)
        }
        
        self.aggregated_findings = all_findings
        self.analysis_log.append(aggregation)
        return aggregation
    
    def _categorize_by_severity(self, findings: List[Finding]) -> Dict[str, int]:
        """Categorize findings by severity."""
        return {
            "critical": len([f for f in findings if f.severity == "critical"]),
            "warning": len([f for f in findings if f.severity == "warning"]),
            "info": len([f for f in findings if f.severity == "info"])
        }
    
    def _categorize_by_office(self, findings: List[Finding]) -> Dict[str, int]:
        """Categorize findings by office."""
        by_office = {}
        for finding in findings:
            office = finding.office.title()
            by_office[office] = by_office.get(office, 0) + 1
        return by_office
    
    def _calculate_metrics(self, findings: List[Finding]) -> Dict[str, Any]:
        """Calculate aggregation metrics."""
        return {
            "average_severity": "warning" if len([f for f in findings if f.severity == "warning"]) > 0 else "info",
            "requires_validation_count": len([f for f in findings if f.requires_validation]),
            "recommendation_count": len([f for f in findings if f.recommendation])
        }


class ConsensusEngine:
    """Builds consensus from multiple perspectives."""
    
    def __init__(self):
        self.name = "Consensus Engine"
        self.consensus_records = []
    
    def build_consensus(self, aggregated_findings: Dict[str, Any]) -> Dict[str, Any]:
        """Build consensus from aggregated findings."""
        findings = aggregated_findings["findings"]
        severity_breakdown = aggregated_findings["by_severity"]
        
        consensus_score = self._calculate_consensus_score(findings)
        recommendation = self._generate_recommendation(findings, consensus_score)
        
        consensus = {
            "timestamp": datetime.now().isoformat(),
            "total_findings_analyzed": len(findings),
            "consensus_score": consensus_score,
            "severity_breakdown": severity_breakdown,
            "recommendation": recommendation,
            "confidence_level": self._calculate_confidence(consensus_score),
            "next_action": self._determine_next_action(recommendation)
        }
        
        self.consensus_records.append(consensus)
        return consensus
    
    def _calculate_consensus_score(self, findings: List[Finding]) -> float:
        """Calculate consensus score (0-100)."""
        if not findings:
            return 100.0
        
        # Score based on agreement level
        critical = len([f for f in findings if f.severity == "critical"])
        warnings = len([f for f in findings if f.severity == "warning"])
        infos = len([f for f in findings if f.severity == "info"])
        
        # Start at 100 and deduct for issues
        score = 100.0
        score -= critical * 15  # Critical issues deduct more
        score -= warnings * 5
        score = max(0, min(100, score))  # Keep between 0-100
        
        return round(score, 1)
    
    def _generate_recommendation(self, findings: List[Finding], score: float) -> str:
        """Generate recommendation based on consensus."""
        if score >= 85:
            return "STRONG CONSENSUS: All offices align on findings and recommendations."
        elif score >= 70:
            return "MODERATE CONSENSUS: Offices generally agree with minor variations."
        elif score >= 50:
            return "WEAK CONSENSUS: Significant disagreements exist, needs further discussion."
        else:
            return "NO CONSENSUS: Major conflicts in findings, requires escalation."
    
    def _calculate_confidence(self, score: float) -> Dict[str, Any]:
        """Calculate confidence level."""
        if score >= 85:
            level = "Very High"
            percentage = random.randint(90, 99)
        elif score >= 70:
            level = "High"
            percentage = random.randint(75, 89)
        elif score >= 50:
            level = "Medium"
            percentage = random.randint(60, 74)
        else:
            level = "Low"
            percentage = random.randint(40, 59)
        
        return {"level": level, "percentage": percentage}
    
    def _determine_next_action(self, recommendation: str) -> str:
        """Determine next action based on recommendation."""
        if "STRONG" in recommendation:
            return "Proceed to C-Suite Roundtable for final approval"
        elif "MODERATE" in recommendation:
            return "Schedule follow-up discussion to resolve variations"
        elif "WEAK" in recommendation:
            return "Reconvene offices for deeper analysis"
        else:
            return "Escalate to executive leadership for conflict resolution"


class CollectiveIntelligenceHub:
    """Main hub coordinating all intelligence operations."""
    
    def __init__(self):
        self.name = "Collective Intelligence Hub"
        self.aggregator = IntelligenceAggregator()
        self.consensus_engine = ConsensusEngine()
        self.roundtable = CSuiteRoundtable()
        self.operations_log = []
    
    def process_all_findings(self, scranton_findings: List[Finding], 
                            stamford_findings: List[Finding],
                            corporate_findings: List[Finding]) -> Dict[str, Any]:
        """Process all findings through the complete intelligence pipeline."""
        
        operation = {
            "timestamp": datetime.now().isoformat(),
            "stage_1_aggregation": None,
            "stage_2_consensus": None,
            "stage_3_roundtable": None,
            "final_decision": None
        }
        
        # Stage 1: Aggregation
        aggregated = self.aggregator.aggregate(
            scranton_findings,
            stamford_findings,
            corporate_findings
        )
        operation["stage_1_aggregation"] = aggregated
        
        # Stage 2: Consensus Building
        consensus = self.consensus_engine.build_consensus(aggregated)
        operation["stage_2_consensus"] = consensus
        
        # Stage 3: C-Suite Roundtable
        topic = self._generate_topic(aggregated)
        roundtable_decision = self.roundtable.conduct_roundtable(
            topic,
            aggregated["findings"]
        )
        operation["stage_3_roundtable"] = roundtable_decision
        
        # Final Decision
        operation["final_decision"] = roundtable_decision["decision"]
        operation["confidence_level"] = roundtable_decision["confidence_level"]
        operation["next_steps"] = roundtable_decision["final_recommendation"]["next_steps"]
        
        self.operations_log.append(operation)
        return operation
    
    def _generate_topic(self, aggregated: Dict[str, Any]) -> str:
        """Generate roundtable topic based on findings."""
        total = aggregated["total_findings"]
        severity = aggregated["by_severity"]
        
        if severity["critical"] > 0:
            return f"Critical Issues Review - {total} findings require immediate attention"
        elif severity["warning"] > 3:
            return f"System Status Update - {total} findings with {severity['warning']} warnings"
        else:
            return f"Standard Review - {total} findings, all offices reporting nominal status"
    
    def get_intelligence_report(self) -> Dict[str, Any]:
        """Get comprehensive intelligence report."""
        if not self.operations_log:
            return {"status": "No operations processed yet"}
        
        latest_op = self.operations_log[-1]
        
        return {
            "timestamp": datetime.now().isoformat(),
            "hub_name": self.name,
            "total_operations": len(self.operations_log),
            "latest_operation": latest_op,
            "aggregator_status": {
                "total_findings_aggregated": len(self.aggregator.aggregated_findings),
                "aggregations_performed": len(self.aggregator.analysis_log)
            },
            "consensus_status": {
                "consensuses_built": len(self.consensus_engine.consensus_records),
                "average_consensus_score": self._calculate_average_score()
            },
            "roundtable_status": self.roundtable.get_status()
        }
    
    def _calculate_average_score(self) -> float:
        """Calculate average consensus score."""
        if not self.consensus_engine.consensus_records:
            return 0.0
        
        total = sum(r["consensus_score"] for r in self.consensus_engine.consensus_records)
        return round(total / len(self.consensus_engine.consensus_records), 1)
    
    def get_status(self) -> Dict[str, Any]:
        """Get hub operational status."""
        return {
            "name": self.name,
            "operational": True,
            "components": {
                "aggregator": self.aggregator.name,
                "consensus_engine": self.consensus_engine.name,
                "roundtable": self.roundtable.name
            },
            "operations_processed": len(self.operations_log),
            "last_operation": self.operations_log[-1]["timestamp"] if self.operations_log else "None"
        }
