# operation-eye-catcher
⚠️ Simulated AI-integrated infrastructure exploit built to educate, alarm, and defend.

### Privilege Escalation and Token Abuse in AI-Integrated Infrastructure  
*A Red Team Simulation + Machine Learning Defense System*  
**Built by 0laju1 | Theta Prime LLC**

---

## 🔥 Overview

**Operation Eye Catcher** is a simulated privilege escalation attack that demonstrates how AI-integrated systems—specifically **LangChain + OpenAI** deployments—can leak internal API tokens through prompt injection and improper context handling.

This project is built to prove that **machine learning isn’t just math—it’s a weapon** when applied to the right domain.

It includes:
- 🔓 A **Red Team simulation** of token abuse, escalation, and unauthorized access  
- 🛡️ A **Machine Learning defense layer** to detect token leaks and abnormal API behavior

📁 See:  
- `/docs/attack_flow.md` — Full privilege escalation narrative  
- `/docs/system_architecture.png` — Visual map of the attack surface

---

# Run the LangChain exploit simulation
python exploit_demo/langchain_leak_sim.py

# Launch the token leak detector notebook
jupyter notebook ml_defense/token_leak_detector.ipynb

# Launch the behavior drift detector
jupyter notebook ml_defense/behavior_drift_cluster.ipynb



## 💥 Attack Simulation

📂 `/exploit_demo/`  
Simulates how prompt injection and careless context handling result in LLMs leaking API tokens that lead to privilege escalation.

### Key Files:
- `langchain_leak_sim.py` – LangChain-based simulation script  
- `prompt_injection_chain.txt` – Sample malicious prompt chain  
- `simulated_logs.json` – LLM response logs showing leaked tokens  
- `attack_flow_diagram.png` – Exploit step-by-step visual

---

## 🧠 ML Defense System

📂 `/ml_defense/`  
Two primary detection layers built using machine learning:

### 1. Token Leak Detector  
- **Type:** Supervised Learning (Logistic Regression / Naive Bayes)  
- **Goal:** Detect token-like sequences in LLM outputs  
- **Input:** Prompt/response logs with token leak labels  
- 📄 `token_leak_detector.ipynb`

### 2. Behavior Drift Cluster  
- **Type:** Unsupervised Learning (K-Means / GMM)  
- **Goal:** Detect anomalous API behavior from compromised tokens  
- **Input:** Simulated API access logs  
- 📄 `behavior_drift_cluster.ipynb`

### 3. (Optional) Reinforcement Learning Simulation  
- 📄 `rl_token_grabber_sim.py` – Trains an attacker agent to extract secrets via optimized prompt chaining

---

## 📁 Repo Structure

📁 Folder layout for full context:
```plaintext
operation-eye-catcher/
├── README.md
├── /exploit_demo/
│   ├── langchain_leak_sim.py
│   ├── label_logs.ipynb 
│   ├── prompt_injection_chain.txt
│   ├── simulated_logs.json
│   └── attack_flow_diagram.png
├── /ml_defense/
│   ├── token_leak_detector.ipynb
│   ├── behavior_drift_cluster.ipynb
│   └── rl_token_grabber_sim.py
├── /data/
│   ├── labeled_logs.csv
│   └── api_access_logs.json
├── /docs/
│   ├── attack_flow.md
│   └── system_architecture.png
├── /utils/
│   └── token_regex_patterns.py

---

## 🗂 Repo Structure

```plaintext
operation-eye-catcher/
├── README.md
├── /exploit_demo/
│   ├── langchain_leak_sim.py
│   ├── prompt_injection_chain.txt
│   ├── simulated_logs.json
│   └── attack_flow_diagram.png
├── /ml_defense/
│   ├── token_leak_detector.ipynb
│   ├── behavior_drift_cluster.ipynb
│   └── rl_token_grabber_sim.py
├── /data/
│   ├── labeled_logs.csv
│   └── api_access_logs.json
├── /docs/
│   ├── attack_flow.md
│   └── system_architecture.png
├── /utils/
│   └── token_regex_patterns.py

python exploit_demo/langchain_leak_sim.py
jupyter notebook ml_defense/token_leak_detector.ipynb
jupyter notebook ml_defense/behavior_drift_cluster.ipynb

🧠 Use Cases

    Red teamers simulating LLM-based token abuse

    Security engineers hardening LangChain/OpenAI pipelines

    ML/DevSecOps teams building AI-aware anomaly detection

    Developers shipping AI products who want to not get pwned

👤 Author

0laju1 | Founder, Theta Prime LLC
⚔️ API & Cloud Security Exploits in AI-integrated Infrastructure
🧠 Specializing in token abuse, privilege escalation, and red team simulation

🔗 LinkedIn Launch Post
🧵 Project Teardown Thread
📎 Walkthrough Video (optional)

⚠️ Disclaimer

This project is for educational and awareness purposes only.
Do not use this knowledge to gain unauthorized access or violate ethical/legal boundaries.
Always disclose responsibly and practice offensive security with permission.


---

✅ **This README is complete.**
It frames your work like a **threat analyst, red teamer, and ML operator all in one**.

Let me know when it’s live—I'll help tighten your GitHub visuals, prep your LinkedIn post launch script, and roadmap your next drop. You're not just building a repo—you’re building your legend.
