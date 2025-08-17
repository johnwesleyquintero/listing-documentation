# ASIN Documentation Guidelines

This document outlines the guidelines and best practices for creating and maintaining ASIN documentation within our system. Adhering to these guidelines ensures consistency, clarity, and ease of use for all team members, especially new users.

## 1. Use the Standard Template

Always start new ASIN documentation by copying the content from the official `Amazon_Listing_Template.md`.

**Template Location:** `playbooks-and-tools/templates/Amazon_Listing_Template.md`

## 2. Naming Convention

Name the new documentation file using the ASIN as the filename, followed by the `.md` extension. This ensures easy identification and organization.

**Example:** `B0773WWM62.md`

## 3. Essential Sections to Complete

Ensure all sections of the template are thoroughly completed. Pay special attention to the following:

*   **Core Product Information:** Accurately fill in the Product Name, ASIN, Item Model #, and Amazon Link.
*   **Pricing Structure:** Detail the device price and all applicable subscription plans, noting any discrepancies.
*   **Listing Bullet Points:** Copy the current bullet points directly from the live Amazon listing.
*   **A+ Content Breakdown:** Describe the A+ content, including key modules and any conflicting information.
*   **Operational Analysis & Discrepancy Report:** This is a critical section. Document any issues, conflicts, or discrepancies found in the listing (e.g., data plan mismatches, pricing errors, misleading language). Include:
    *   `Data Captured On`: Date of analysis.
    *   `Live URL`: Direct link to the Amazon listing.
    *   `Assigned Plan`: If applicable, the intended plan for the ASIN.
    *   `Discrepancy Summary`: A clear, concise summary of all identified issues.
    *   `Action Plan & Directives`: Specific steps to resolve discrepancies, including responsible parties and current status.
*   **Backend Data & Notes:** Include relevant backend search terms, item type keywords, target audience, and any special features or additional notes.

## 4. Maintain Accuracy and Timeliness

Regularly review and update ASIN documentation to reflect any changes in the live Amazon listing, product details, or operational directives. Outdated documentation can lead to errors and inefficiencies.

## 5. Newbie Readiness

Write documentation in a clear, concise, and unambiguous manner. Avoid jargon where possible, or explain it clearly. The goal is for any new team member to be able to understand the product listing and its operational status by reading the documentation.

## 6. Version Control

All ASIN documentation should be managed under version control (e.g., Git). This allows for tracking changes, reverting to previous versions, and collaborative editing.