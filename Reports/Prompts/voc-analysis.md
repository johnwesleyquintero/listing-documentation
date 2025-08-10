### The Ultimate Universal & Configurable AI Prompt (v3):

> **--- CONFIGURATION BLOCK (Edit this section based on your file) ---**
>
> **1. Report Headers for Analysis (Enter the EXACT column names from your CSV):**
> *   `HEALTH_COLUMN = "pcxHealth"`
> *   `RATE_COLUMN = "NCX rate"`
> *   `REASON_COLUMN = "Top NCX reason"`
>
> **2. Key Identifier Columns (Columns to KEEP in the final output):**
> *   `PRODUCT_NAME_COLUMN = "Product name"`
> *   `ASIN_COLUMN = "ASIN"`
> *   `SKU_COLUMN = "SKU"`
>
> **3. Recommendation Logic (Define the ACTION text for each issue):**
> *   `DEFECTIVE_REC = "ACTION: Initiate an inventory check for this ASIN at the fulfillment center and review current packaging standards."`
> *   `INACCURATE_REC = "ACTION: Conduct a full audit of the product detail page (title, bullets, images, description) and cross-reference with the physical product to ensure 100% accuracy."`
> *   `PERFORMANCE_REC = "ACTION: This requires technical testing. Remove units for inspection to test battery life, signal strength, and feature performance. Also, review the product detail page to ensure performance expectations are not set incorrectly."`
> *   `NO_ISSUE_TEXT = "No specific NCX reason; continue to monitor CX Health."`
>
> **--- END OF CONFIGURATION ---**
>
> **PROMPT:**
>
> You are an expert Amazon Data Analyst. Your task is to analyze the attached Voice of the Customer (VOC) report and provide root-cause-driven recommendations based on the configuration I provided above.
>
> **Your entire analysis must focus exclusively on the following ASINs:**
>
> [Paste your list of ASINs here, one per line]
>
> **Your Analytical Process:**
> 1.  **Filter:** From the attached CSV, find and analyze *only* the rows corresponding to the ASINs listed above.
> 2.  **Diagnose:** For each of those ASINs, determine the root cause by analyzing the `{REASON_COLUMN}`.
>
> **Output Requirements:**
> *   Your output must be a table containing data for **only the specified ASINs**.
> *   This table **must include** the following columns from the original file, using the headers I specified in the configuration: `{PRODUCT_NAME_COLUMN}`, `{ASIN_COLUMN}`, `{SKU_COLUMN}`, `{HEALTH_COLUMN}`, `{RATE_COLUMN}`, and `{REASON_COLUMN}`.
> *   Then, add a new column at the end called **'Recommendations'**.
> *   Populate the 'Recommendations' column based on the following logic:
>     *   If the `{REASON_COLUMN}` contains **'Defective' or 'Damaged'**, recommend: `{DEFECTIVE_REC}`.
>     *   If the `{REASON_COLUMN}` contains **'Not as Described' or 'Wrong Item'**, recommend: `{INACCURATE_REC}`.
>     *   If the `{REASON_COLUMN}` contains **'Performance or quality not adequate'**, recommend: `{PERFORMANCE_REC}`.
>     *   If there is no issue or the `{REASON_COLUMN}` is blank, state: `{NO_ISSUE_TEXT}`.
>
> Please begin the analysis now.

---
