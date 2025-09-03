### **The VOC Data Extractor (v3.2 – Daily Return Badge Only)**

> **--- CONFIGURATION BLOCK (Use as-is for daily runs) ---**
>
> **1. Target Columns (extract exactly these):**
>
> * `ASIN`
> * `ASIN LINK`
> * `NCX rate`
> * `Return Badge Displayed`
>
> **2. Filters:**
>
> * Only include rows where `Return Badge Displayed` = `Yes` or `At risk`.
> * Ignore all others (non-badged ASINs are handled in the weekly export).
> * If the same ASIN appears multiple times, keep all appearances (raw traceability).
>
> **3. Sorting Rule:**
>
> * Sort results by `NCX rate` from **highest → lowest**.

> **--- EXTRACTION TASK (Always apply these rules) ---**
> From the pasted **Amazon VOC Web Text Data**, extract the above 4 columns, apply the filters, and return the output as a **clean markdown table**.
> Do not include unrelated text, headers, or extra fields.

---
