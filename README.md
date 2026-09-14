# 🏢 Dunder Mifflin AI Office - Collective Intelligence Platform

> A multi-office AI agent system with C-Suite roundtable for enterprise-scale collective decision-making

## 🎯 Overview

This system simulates three interconnected AI office branches, each with specialized agents running on different LLM architectures, coordinated by a C-Suite roundtable for collective intelligence and strategic decision-making.

### 📍 Three Offices

1. **Scranton Office** 🔍
   - Focus: Functional Testing & User Experience
   - LLM Archetype: Claude-like (Creative, Detailed)
   - Lead Agent: Jim Halpert
   - Team: Pam (API), Dwight (Automation), Ryan (Documentation)

2. **Stamford Office** ⚙️
   - Focus: Infrastructure & Backend Systems
   - LLM Archetype: GPT-like (Analytical, Systematic)
   - Lead Agent: Josh Porter
   - Team: Karen (Performance), Val (Security), Hidetoshi (DevOps)

3. **Corporate Office** 🏛️
   - Focus: Strategy & Quality Assurance Review
   - LLM Archetype: Gemini-like (Holistic, Risk-aware)
   - Lead Agent: David Wallace
   - Team: Jan (Compliance), Charles (Architecture), Erin (Reporting)

### 🎭 C-Suite Roundtable

**Strategic Decision-Making Council:**
- **CEO** - Michael Scott (Vision & Direction)
- **CTO** - Nellie Bertram (Technical Authority)
- **CFO** - Oscar Martinez (Financial & Resource Impact)
- **COO** - Deangelo Vickers (Operations)
- **Chief AI Officer** - Gabe Lewis (Collective Intelligence Orchestrator)

## 🏗️ Architecture

```
dunder-mifflin-ai-office/
├── README.md
├── requirements.txt
├── config/
│   ├── __init__.py
│   └── settings.py
├── offices/
│   ├── scranton/
│   │   ├── __init__.py
│   │   ├── agents.py
│   │   └── tasks.py
│   ├── stamford/
│   │   ├── __init__.py
│   │   ├── agents.py
│   │   └── tasks.py
│   └── corporate/
│       ├── __init__.py
│       ├── agents.py
│       └── tasks.py
├── roundtable/
│   ├── __init__.py
│   ├── csuite.py
│   └── consensus_engine.py
├── collective_intelligence/
│   ├── __init__.py
│   ├── knowledge_hub.py
│   └── decision_maker.py
├── models/
│   ├── __init__.py
│   ├── llm_simulator.py
│   └── response_templates.py
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   └── validators.py
└── examples/
    ├── __init__.py
    ├── test_case_1.py
    └── run_roundtable.py
```

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/aryamansoryjalilian-art/dunder-mifflin-ai-office.git
cd dunder-mifflin-ai-office
pip install -r requirements.txt
```

### Run a Simple Example

```bash
python examples/run_roundtable.py
```

## 🔄 Workflow

1. **Task Submission** → Enters the system
2. **Office Processing** → Each office analyzes independently
3. **Findings Aggregation** → Results collected
4. **C-Suite Review** → Roundtable debates & analyzes
5. **Consensus Building** → Collective intelligence applied
6. **Final Decision** → Recommendation issued

## 🤖 Agent Types

### Office Agents
- **Discoverer** - Finds issues/opportunities
- **Investigator** - Deep analysis
- **Validator** - Verification & proof
- **Automator** - Solution implementation
- **Reporter** - Documentation & comms

### C-Suite Agents
- **Decision-Maker** - Strategic choices
- **Risk-Assessor** - Downside analysis
- **Resource-Manager** - Capacity planning
- **Consensus-Builder** - Agreement facilitator
- **Orchestrator** - System coordinator

## 📊 Features

- ✅ Multi-office distributed processing
- ✅ LLM-agnostic agent framework
- ✅ C-Suite consensus engine
- ✅ Evidence-based decision trails
- ✅ Collective intelligence knowledge hub
- ✅ Configurable agent personalities
- ✅ Full audit logging

## 🔗 Integration

This system is designed to integrate with:
- Multiple LLM providers (Claude, GPT, Gemini, etc.)
- Enterprise knowledge bases
- Test automation platforms
- CI/CD pipelines
- Reporting & analytics systems

## 📝 License

MIT

## 👥 Contributing

Contributions welcome! Please see CONTRIBUTING.md

---

**Built with ❤️ for Collective Intelligence**
