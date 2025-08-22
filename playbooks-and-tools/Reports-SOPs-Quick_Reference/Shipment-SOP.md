### **Standard Operating Procedure (SOP): STK/SecuLife FBA Shipment Creation**

**Document Version:** 1.0 (Initial Draft)
**Date:** August 21, 2025
**Author:** John Wesley Quintero
**Source:** Initial briefing from Xavi

**1. Core Objective:**
To create and document FBA (Fulfillment by Amazon) shipments in a standardized manner, ensuring accurate labeling, timely processing, and correct internal tracking for all STK and SecuLife products.

---

### **2. Pre-Shipment Rules & Constraints**

*   **Standard Case Pack Quantity:** All products are packed **50 units per box.**
*   **Maximum Shipment Size (Smartwatches):** For smartwatch SKUs, a single shipment should contain a maximum of **3 boxes (150 units total).**
*   **Daily Cut-Off Time:** If the current time is **after 3:00 PM**, the shipment must be scheduled for the following business day.

---

### **3. Shipment Creation & Labeling Protocol**

**A. Naming Convention:**
*   All shipments must follow a standardized naming convention: `FBA SLXXX` (where `XXX` is the sequential shipment number, e.g., `FBA SL364`).

**B. Label Processing:**
1.  **Generate Barcodes:** Create the required FBA item barcodes.
2.  **Rename Barcode File:** The generated barcode PDF file must be renamed to follow the convention: `Barcode FBA SLXXX`.
3.  **Print Barcodes:** Print the barcode file using the "Letter Print" setting.
4.  **Generate Shipping Labels:** Create the final FBA shipping labels for the boxes.
5.  **Rename Shipping Label File:** The shipping label PDF must be renamed to follow the convention: `Shipping label - FBA SLXXX`.

**C. Screenshot for Records:**
1.  Take a screenshot of the finalized shipment for internal records.
2.  The screenshot file must be named: `Cover FBA SLXXX`.

---

### **4. Internal Communication & Tracking**

**A. Shipping Team Notification:**
*   **Action:** Send an email to the **Shipping Team** to formally request the shipment.
*   **CC:** `Ran` must be copied on this email.
*   **Subject Line Format:** `Shipping Request - FBA SLXXX`
*   **Body Format:** The email body must clearly list the shipment details in the following format:
    > `[Shipment Name] - [Product Name] - [ASIN] - [SKU] - [Total Units]`
    > **Example:** `FBA SL364 - SECULIFE KIDS M&M SMARTWATCH BLUE - B0DLLNXR9L - FBA-SL-24MEK-BLU - 150 units`

**B. Internal Portal Tracking:**
1.  **Login:** Access the internal portal (ecom tool).
2.  **Navigate:** Go to **Reports > FBAsl**.
3.  **Create Record:** Click **"Add a Record"** to create a new entry for the shipment.
4.  **Input Data:** Fill in all required shipment information into the portal.
5.  **Set NET SKU Field:** For all device shipments, the "NET SKU" field must always be set to **0**.
6.  **Set Status:** The initial status for all new shipments must be set to **"Working."**

---

### **5. Pending Information (To be added from video):**

*   Detailed navigation steps for the FBA shipment creation portal on Amazon.
*   Specific instructions on where to find the sequential shipment number (`SLXXX`).
*   Visual confirmation of the "ecom tool" portal interface.

---

**Document Naming Convention**
```
Shipping label FBA SLXXX
```
```
Barcode FBA SLXXX
```
```
Cover FBA SLXXX
```
