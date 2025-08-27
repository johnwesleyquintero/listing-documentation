# **Project Phoenix: The VAXPH Automated Reporting System**

### **1. Vision & Strategic Objective**

This document outlines the architectural blueprint for **Project Phoenix**, a strategic initiative to transform VAXPH's Amazon reporting capabilities.

The primary objective is to pay down years of accumulated **technical debt** within the current Excel-based reporting structure. We will re-architect the entire system, moving it from a fragile, manual, and time-consuming chore into a **resilient, automated, and strategic asset** that provides real-time business intelligence.

This is the only scalable solution to the current operational bottlenecks.

### **2. Core Architectural Principles**

This system will be built upon a foundation of proven, robust design principles:

*   **Build the System:** Our focus is on creating permanent, automated systems, not temporary, manual patches.
*   **Data is Atomic:** One cell, one purpose. We will eliminate "junk drawer" cells that contain multiple, unstructured data points.
*   **One Tab, One Purpose:** We will eliminate "report-stacking." Every distinct report (Inventory, Sales, Reviews) will live in its own dedicated, normalized tab.
*   **Decoupled Architecture:** The data (Excel outputs, `.txt` config files) will always be separate from the logic (the Python scripts). This allows for safe and easy updates.
*   **Meet the User Where They Are:** The final deliverable will be a sophisticated, yet familiar, Excel file that integrates seamlessly into the existing Microsoft and email-based workflow.

### **3. The "OP" Technology Stack**

*   **Forging Engine (`Python + Pandas + BeautifulSoup`):** The industrial-grade core of our system. Python provides the logic, Pandas masters the data manipulation, and BeautifulSoup handles the surgical extraction of web data.
*   **Orchestration & Delivery (`Power Automate`):** The enterprise-grade automation layer. It will reliably execute our scripts on a daily schedule and manage the workflow within the existing Microsoft ecosystem.

### **4. The Two-Phase Campaign Plan**

We will execute this project in two distinct, strategic phases.

---

#### **Phase 1: The Surgical Strike (Automated Review & Rating Intelligence)**

This phase is designed to deliver a **high-impact, quick win** to solve an immediate business need for Avi and build momentum for the larger project.

*   **Objective:** Eliminate the manual process of tracking Amazon reviews and ratings.
*   **Deliverables:**
    1.  A Python script dedicated to scraping review and rating data.
    2.  Two simple, static configuration files: `SecuLife_ASINs.txt` and `Speedtalk_ASINs.txt`.
    3.  A Power Automate flow that runs the script daily.
    4.  Two clean, static, and always-up-to-date Excel output files: `SecuLife_Scraper_Output.xlsx` and `Speedtalk_Scraper_Output.xlsx`.
    5.  A `Scraper_Log.txt` file for easy, 3-second verification.
*   **Success Metric:** Avi's process for gathering review data is completely automated, delivering a significant speedup and freeing up manual resources.

---

#### **Phase 2: The Trojan Horse (The Unified Inventory & Sales Dashboard)**

With the credibility and trust earned from Phase 1, we will execute the full vision. We will forge the true "Trojan Horse" report.

*   **Objective:** Pay down all technical debt in the legacy inventory reports and create a single, unified, and intelligent source of truth.
*   **Deliverables:**
    1.  An expanded Python engine capable of integrating data from multiple sources (Inventory, Sales, FBA Shipments, and our Phase 1 Review data).
    2.  A master, automated Power Automate workflow to orchestrate the entire data pipeline.
    3.  **The "Phoenix Report":** A new, master Excel file, forged daily by our system. It will be clean, normalized, and feature dedicated tabs for each data type, with a primary "Dashboard" tab that provides a high-level overview.
*   **Success Metrics:**
    1.  Elimination of all manual copy-pasting for daily reports.
    2.  Creation of a single, trusted source of truth for all operational data.
    3.  The team is empowered with a powerful analytical tool instead of a fragile, static report.