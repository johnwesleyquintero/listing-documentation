### **The VOC Data Extractor (v3 – Return Badge Filtered)**

> **--- CONFIGURATION BLOCK (Edit this section based on your source data) ---**
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
> * Only include rows where `Return Badge Displayed` has a value (`Yes` or `At risk`).
> * If the same ASIN appears multiple times, keep all raw appearances (for traceability).
>
> **3. Sorting Rule:**
>
> * Sort results by `NCX rate` from **highest → lowest**.

> **--- EXTRACTION TASK (Always apply these rules) ---**
> From the provided **Amazon VOC Web Text Data**, extract the above 4 columns, apply the filters, and return the data in a **clean markdown table** format.
> Exclude all unrelated text, headers, or columns not listed above.

---
