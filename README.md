# Project BlackKey
⚠️ Simulated AI-integrated infrastructure exploit built to educate, alarm, and defend.

### Privilege Escalation and Token Abuse in AI-Integrated Infrastructure  
*A Red Team Simulation + Machine Learning Defense System*  
**Built by Trevor Brown | Theta Prime LLC**

---

## 🔥 Overview

**Project BlackKey** is a simulated privilege escalation attack that demonstrates how AI-integrated systems—specifically **LangChain + OpenAI** deployments—can leak internal API tokens through prompt injection and improper context handling.

This project proves that **machine learning isn’t just math—it’s a weapon** when applied to the right domain.

It includes:
- 🔓 A **Red Team simulation** of token abuse, escalation, and unauthorized access  
- 🛡️ A **Machine Learning defense layer** to detect token leaks and abnormal API behavior

📁 See:  
- `/docs/attack_flow.md` — Full privilege escalation narrative  
- `/docs/system_architecture.png` — Visual map of the attack surface  
- `/docs/rl_agent_report.md` — Reinforcement learning attacker agent writeup

---

## 🛠 How to Run

```bash
# Run the LangChain exploit simulation
python exploit_demo/langchain_leak_sim.py

# Launch the token leak detector notebook
jupyter notebook ml_defense/token_leak_detector.ipynb

# Launch the behavior drift detector notebook
jupyter notebook ml_defense/behavior_drift_cluster.ipynb

project-blackkey/
├── README.md
├── /exploit_demo/
│   ├── langchain_leak_sim.py
│   ├── prompt_injection_chain.txt
│   ├── simulated_logs.json
│   └── attack_flow_diagram.png
├── /ml_defense/
│   ├── token_leak_detector.ipynb
│   ├── behavior_drift_cluster.ipynb
│   ├── rl_token_grabber_sim.py
│   ├── token_leak_detector.pkl
│   └── vectorizer.pkl
├── /data/
│   ├── label_log_builder.ipynb
│   ├── labeled_logs.csv
│   └── api_access_logs.json
├── /docs/
│   ├── attack_flow.md
│   ├── rl_agent_report.md
│   └── system_architecture.png
├── /utils/
│   └── token_regex_patterns.py
