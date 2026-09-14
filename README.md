# 🎬 Dunder Mifflin AI Office System

> A fictional AI office simulation inspired by *The Office*, featuring three regional offices with specialized AI agents, collective intelligence hub, and C-Suite decision-making body.

## 🏢 System Overview

The Dunder Mifflin AI Office System is a sophisticated multi-agent framework that simulates how three different regional offices (each with distinct AI analysis styles) collaborate through a collective intelligence hub to make strategic decisions.

### Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│          DUNDER MIFFLIN AI OFFICE SYSTEM v1.0.0                 │
└─────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   🏢 SCRANTON           🏢 STAMFORD          🏢 CORPORATE
   (Claude-style)        (GPT-style)          (Gemini-style)
   UI Testing Hub        Infrastructure Hub    Strategy Hub
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                         │
        ┌─────────────────v─────────────────┐
        │ COLLECTIVE INTELLIGENCE           │
        │  HUB (Aggregation &              │
        │  Consensus Building)             │
        └─────────────────┬─────────────────┘
                  │
        ┌─────────────────v─────────────────┐
        │  C-SUITE ROUNDTABLE              │
        │  (5 Executives)                  │
        └─────────────────┬─────────────────┘
                  │
        ┌─────────────────v─────────────────┐
        │  INTERACTIVE                     │
        │  DASHBOARD (CLI)                 │
        └──────────────────────────────────┘
```

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/aryamansoryjalilian-art/dunder-mifflin-ai-office.git
cd dunder-mifflin-ai-office

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the system
python main.py
```

## 📊 Where to See Results

### 📋 Interactive Menu Options

When you run `python main.py`, you'll get this menu:

```
1. Run demo with example tasks
2. Process a custom task  
3. View system status
4. Exit
```

### 🔍 Results for Each Option

**Option 1: Run Demo** 🎬
- Processes 2 complete example tasks
- Shows full workflow for each task
- Displays beautiful colored output
- Shows all stages: offices → intelligence hub → C-suite → dashboard
- Each stage prints real-time updates

**Option 2: Custom Task**
- Enter your own task description
- System processes it through all 3 offices
- Shows aggregated findings
- Displays consensus score
- Shows C-Suite decision
- Beautiful formatted report

**Option 3: System Status**
- Shows operational status
- Total tasks processed
- Total findings collected
- System uptime

## ✨ Key Features You'll See

### 💬 Office Analysis
Each office analyzes tasks from their perspective:
- **Scranton**: Creative, detail-focused (like Claude)
- **Stamford**: Technical, systematic (like GPT)  
- **Corporate**: Strategic, holistic (like Gemini)

### 🧠 Intelligence Aggregation
- Combines findings from all 3 offices
- Categorizes by severity
- Breaks down by office
- Calculates metrics

### 📋 Consensus Building
- Builds consensus score (0-100)
- Generates recommendations
- Calculates confidence level
- Determines next action

### 👔 C-Suite Roundtable
- 5 executives discuss findings
- Each provides unique perspective
- Final decision with rationale
- Implementation next steps

### 🎨 Beautiful Dashboard
- Color-coded output (Blue, Green, Magenta)
- Formatted tables
- Status indicators
- Real-time updates

## 📁 Project Structure

```
dunder-mifflin-ai-office/
├─ models/              # Data models (Agent, Finding)
├─ offices/             # 3 Offices (Scranton, Stamford, Corporate)
├─ roundtable/          # C-Suite executives
├─ intelligence/        # Collective Intelligence Hub
├─ dashboard/           # CLI visualization
├─ app/                 # Main orchestrator
├─ main.py             # Entry point (👈 START HERE)
├─ requirements.txt     # Python dependencies
└─ README.md            # This file
```

## 📑 What Each File Does

| File | Purpose |
|------|----------|
| `main.py` | **Entry point** - Start here! |
| `app/system.py` | Orchestrates all components |
| `offices/scranton/agents.py` | Scranton office agents |
| `offices/stamford/agents.py` | Stamford office agents |
| `offices/corporate/agents.py` | Corporate office agents |
| `roundtable/csuite.py` | C-Suite executives |
| `intelligence/hub.py` | Aggregation & consensus |
| `dashboard/cli.py` | Beautiful CLI visualization |
| `models/agent.py` | Agent & Finding classes |

## 💼 Running Examples

### Demo Run
```bash
python main.py
# Select option 1
# Processes 2 complete tasks automatically
```

### Custom Task
```bash
python main.py  
# Select option 2
# Enter: "Implement JWT authentication for API"
# Watch as all offices analyze it
```

### Direct Python
```python
from app.system import DunderMifflinAIOfficeSystem

system = DunderMifflinAIOfficeSystem()
result = system.process_task("Your task here")
system.display_full_report(result)
```

## 👥 Meet the Team

### Scranton Office (Claude-style)
- Jim Halpert, Pam Beesly, Dwight Schrute, Ryan Howard

### Stamford Office (GPT-style)  
- Josh Baskin, Karen Filippelli, Val Bertrand, Hidetoshi Hasagawa

### Corporate Office (Gemini-style)
- David Wallace, Jan Levinson, Charles Miner, Erin Hannon

### C-Suite
- Michael Scott (CEO)
- Nellie Bertram (CTO)
- Oscar Martinez (CFO)
- Deangelo Vickers (COO)
- Gabe Lewis (Chief AI Officer)

## ⚙️ Technologies Used

- **Python 3.8+** - Core language
- **colorama** - Colored terminal output
- **tabulate** - ASCII tables
- **pydantic** - Data validation
- **OOP** - Object-oriented design

## 📚 Learn From This Project

1. **Multi-agent systems** - How agents with different styles work together
2. **Consensus algorithms** - Building consensus from multiple perspectives
3. **CLI design** - Creating beautiful terminal interfaces
4. **Architecture patterns** - Layered system design
5. **Workflow orchestration** - Coordinating complex processes

## 👨‍💻 Author

**Aryaman Sory Jalilian**
- GitHub: [@aryamansoryjalilian-art](https://github.com/aryamansoryjalilian-art)
- Email: aryamansoryjalilian@gmail.com

## 🎉 Fun Facts

- 🎬 Inspired by "The Office" TV series
- 🧠 Demonstrates collective intelligence concepts
- 🏢 Shows how different perspectives lead to better decisions
- 📋 Models real corporate decision-making processes
- 🎨 Beautiful terminal design with colors and tables

---

## 🚀 START HERE

```bash
# 1. Clone
git clone https://github.com/aryamansoryjalilian-art/dunder-mifflin-ai-office.git
cd dunder-mifflin-ai-office

# 2. Install  
pip install -r requirements.txt

# 3. Run
python main.py

# 4. Select option 1 to see the demo!
```

**Watch as the system processes tasks through all offices and makes decisions together!** 🎬
