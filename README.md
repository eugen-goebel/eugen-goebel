# Hi, I'm Eugen

Business Informatics (Wirtschaftsinformatik) graduate building production-grade portfolio projects across quantitative finance and real-time data systems, AI agents, full-stack web apps, data engineering, and applied machine learning for cybersecurity.

**Education:** B.Sc. Business Informatics (Wirtschaftsinformatik), graduated 2026. Currently pursuing an M.Sc. in Wirtschaftsinformatik part-time at FernUniversität in Hagen while available for full-time work. Bachelor thesis on a digital immune system approach to defending against drone-based cyberattacks.
**Looking for:** **Full-time entry-level / junior positions** in Data Analytics, AI Engineering, Backend, or Cybersecurity. Frankfurt area or remote.

---

## GitHub Stats

[![Eugen's GitHub stats](https://github-readme-stats.vercel.app/api?username=eugen-goebel&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true)](https://github.com/eugen-goebel)
[![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=eugen-goebel&layout=compact&theme=tokyonight&hide_border=true&langs_count=8)](https://github.com/eugen-goebel)

---

## Featured Projects

### Quantitative Finance & Real-Time Systems

| Project | Description | Tech |
|---------|-------------|------|
| [**Portfolio Risk Analytics**](https://github.com/eugen-goebel/portfolio-risk-analytics) ([🚀 **Live Demo**](https://eugen-goebel-portfolio-risk-analytics.streamlit.app/)) | Market data platform: ingests real daily prices (Yahoo, ECB), computes risk and tail-risk metrics (volatility, Sharpe, drawdown, VaR, expected shortfall), benchmark analytics, Markowitz optimization, **volatility forecasting with a walk-forward model comparison**, Monte Carlo simulation and drift monitoring, served through a dashboard, REST API and a scheduled live-data pipeline | Python, FastAPI, PostgreSQL, SQLAlchemy, pandas, NumPy, Streamlit, Docker |
| [**Market Stream Monitor**](https://github.com/eugen-goebel/market-stream-monitor) | Real-time monitor: consumes live trades from the Coinbase and Binance websocket feeds through one provider abstraction, folds them into streaming one-minute bars with VWAP, and raises **anomaly alerts** on volume spikes, price jumps, VWAP dislocations and trade-rate bursts, with a live dashboard and offline replay | Python, asyncio, websockets, PostgreSQL, SQLAlchemy, Streamlit, Docker |

### Full-Stack & Data Engineering

| Project | Description | Tech |
|---------|-------------|------|
| [**Inventory Management Dashboard**](https://github.com/eugen-goebel/inventory-management) | Full-stack inventory system: JWT auth with RBAC (admin/staff/viewer), paginated + sortable product tables (7 sortable columns incl. joined supplier name), CSV import/export, toast notifications, React/TypeScript + FastAPI | React, TypeScript, FastAPI, SQLAlchemy, JWT, Tailwind CSS |
| [**Personal Finance Tracker**](https://github.com/eugen-goebel/personal-finance-tracker) | Full-stack finance app: REST API, dashboard, intelligent transaction categorization, MT940 / OFX bank-statement import, and **savings goals** with progress tracking and required-monthly-contribution maths | Python, FastAPI, Streamlit, SQLAlchemy |
| [**ShopFlow ETL Pipeline**](https://github.com/eugen-goebel/etl-pipeline) ([🚀 **Live Demo**](https://eugen-goebel-etl-pipeline-app-4shwqu.streamlit.app/)) | Multi-agent ETL pipeline: star schema warehouse, 15 SQL analytics queries (window functions, CTEs, NTILE), and a **Pipeline Runs** observability tab tracking duration / success rate / phase timings | Python, SQLAlchemy, SQLite, pandas, Streamlit |
| [**BI Data Analyst Agent**](https://github.com/eugen-goebel/bi-data-analyst) | Multi-agent system that transforms CSV/Excel data into intelligence reports: trends, correlations, outliers, seasonality, plus **ABC / Pareto analysis** to surface the 80/20 contributors | Python, pandas, matplotlib, Anthropic SDK |

### AI Agents & LLM Applications

| Project | Description | Tech |
|---------|-------------|------|
| [**Smart Document Q&A**](https://github.com/eugen-goebel/smart-doc-qa) ([🚀 **Live Demo**](https://eugen-goebel-smart-doc-qa-app-av3twb.streamlit.app/)) | RAG system for PDF / DOCX / TXT: source-grounded answers, persistent ChromaDB vector store, and **multi-turn conversation memory** so follow-up questions resolve against prior context | Python, ChromaDB, Streamlit, Anthropic SDK |
| [**Market Research Agent**](https://github.com/eugen-goebel/market-research-agent) | Automated market research with side-by-side competitor comparison: SWOT, **Porter's Five Forces** with rating-coloured tables, trends, and DOCX or PDF output in under 2 minutes | Python, Anthropic SDK, Pydantic |
| [**Tech Trend Report Agent**](https://github.com/eugen-goebel/tech-trend-agent) | Technology trend reports with multi-technology comparison mode, market analysis, strategic outlook, and a `--format docx/pdf/both` flag for portable distribution | Python, Anthropic SDK, python-docx, fpdf2 |

### Machine Learning & Cybersecurity

| Project | Description | Tech |
|---------|-------------|------|
| [**Network Threat Analyzer**](https://github.com/eugen-goebel/network-threat-analyzer) ([🚀 **Live Demo**](https://eugen-goebel-network-threat-analyzer.streamlit.app/)) | Multi-agent threat detection combining rule-based signatures (port scans, DDoS, brute force, suspicious connections, **DNS tunneling**) with ML anomaly detection (Isolation Forest, LOF, One-Class SVM). Supports PCAP files, server logs, and live interface capture | Python, scapy, scikit-learn, Streamlit |
| [**Predictive Analytics Agent**](https://github.com/eugen-goebel/predictive-analytics-agent) ([🚀 **Live Demo**](https://eugen-goebel-predictive-analytics-agent-app-l05zcc.streamlit.app/)) | Automated ML pipeline: data profiling, preprocessing, hyperparameter tuning (GridSearchCV), and model evaluation with **model-agnostic permutation importance** so linear and KNN models also get interpretability charts | Python, scikit-learn, Streamlit |

---

## Open Source Contributions

Code merged into widely used Python libraries through their normal review process:

| Project | Contribution |
|---------|-------------|
| [py-pdf/fpdf2](https://github.com/py-pdf/fpdf2/pull/1866) | Preserve leading spaces in `<pre>` blocks when rendering HTML |
| [py-pdf/fpdf2](https://github.com/py-pdf/fpdf2/pull/1870) | Add an `optional_content()` context manager for screen-only / print-only PDF layers |
| [plotly/plotly.py](https://github.com/plotly/plotly.py/pull/5625) | Raise a clear error for unsupported marginal plot types |
| [secdev/scapy](https://github.com/secdev/scapy/pull/5022) | Surface the libpcap error when a BPF filter fails to compile |
| [rthalley/dnspython](https://github.com/rthalley/dnspython/pull/1276) | Render unnamed DNS flag bits instead of dropping them |
| [python-websockets/websockets](https://github.com/python-websockets/websockets/pull/1719) | Add a `text` argument to `broadcast()` so callers can force the frame type |

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat&logo=sqlalchemy&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat&logo=pydantic&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=flat&logo=jsonwebtokens&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FFCB1F?style=flat&logoColor=black)
![Anthropic](https://img.shields.io/badge/Anthropic-CC785C?style=flat&logoColor=white)

---

## Contact

- **Email:** eugen-goebel@hotmail.de
- **LinkedIn:** [linkedin.com/in/eugen-goebel](https://www.linkedin.com/in/eugen-goebel)
- **GitHub:** [github.com/eugen-goebel](https://github.com/eugen-goebel)

---

## Auf Deutsch

Frisch abgeschlossener **Bachelor of Science in Wirtschaftsinformatik** (Bachelorarbeit: Abwehr drohnenbasierter Cyberangriffe nach dem Paradigma des digitalen Immunsystems). Aktuell mache ich berufsbegleitend meinen Master (M.Sc. Wirtschaftsinformatik) an der FernUni Hagen und bin in Vollzeit verfügbar. Auf der Suche nach einer **Vollzeitstelle als Berufseinsteiger / Junior** im Bereich Datenanalyse, KI-Entwicklung, Backend oder Cybersecurity. Standort: Frankfurt oder remote. **Kein Werkstudenten- oder Praktikumsplatz.**

Mein Portfolio umfasst **Full-Stack-Webanwendungen** (FastAPI + React mit JWT-Auth, paginierte / sortierbare Tabellen, CSV-Import/Export), **Data-Engineering-Pipelines** (Star-Schema-Warehouse, 15 SQL-Analytics-Queries, Pipeline-Observability-Dashboard), **Multi-Agent-LLM-Systeme** (Anthropic SDK, RAG mit ChromaDB und Mehrturn-Konversationen) sowie **angewandtes Machine Learning** (Anomalie-Erkennung mit Isolation Forest, LOF, One-Class SVM und modell-agnostische Permutation Importance für Interpretierbarkeit).

Zusätzlich klassische **Strategie-Frameworks** in den Reporting-Agents (SWOT, Porter's Five Forces, ABC/Pareto-Analyse) als strukturierter Output statt Freitext.

Außerdem habe ich zu etablierten Open-Source-Bibliotheken beigetragen (fpdf2, plotly, scapy, dnspython, websockets), jeweils über den regulären Review-Prozess gemergt.

Bei Interesse einfach per E-Mail melden.
