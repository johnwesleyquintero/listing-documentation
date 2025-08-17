# Daily Operations Standard Operating Procedure (SOP)

## Purpose
This document outlines the standard procedures for daily operations management across VAX PH brands (SecuLife and Speedtalk Mobile), including communication routines, reporting schedules, and system access protocols.

## Scope
This SOP applies to all team members responsible for daily operations management of:
- SecuLife (GPS tracking equipment and monitoring)
- Speedtalk Mobile (prepaid wireless MVNO)

## Responsibilities
- Maintain accurate time tracking in Slack
- Execute daily/weekly communication routines
- Generate and distribute required reports
- Follow proper system access protocols

### Slack Log Schedule Guide

**Procedure:**
1.  **Time In:** At the start of your shift (8:30 AM PST), log your "TIME IN" in Slack, specifying "VAX PH" and "Working on Stores."
    *Example: `TIME IN 8:30 AM PST | VAX PH | Working on Stores`*
2.  **Hourly Updates:** Every 30 minutes, provide a brief update on your activity in Slack.
    *Example: `9:00 AM PST | VAX PH | Working on Stores`*
3.  **Lunch Break:** Log your lunch break (1:00 PM PST) in Slack.
    *Example: `1:00 PM PST | VAX PH | Lunch`*
4.  **Time Out:** At the end of your shift (5:30 PM PST), log your "TIME OUT" in Slack, summarizing your work.
    *Example: `TIME OUT: 5:30 PM PST | VAX PH | Working on Store: [Brief summary of tasks completed]`*
---

## Troubleshooting and Common Issues

This section addresses common issues and provides troubleshooting steps to ensure smooth daily operations.

### 1. Report Delivery Failures

*   **Issue:** Reports are not being received by the intended recipients.
*   **Troubleshooting Steps:**
    1.  Verify the email addresses in the "Email Distribution Lists" section are correct.
    2.  Check your sent items to confirm the email was dispatched.
    3.  Confirm with recipients if the email landed in their spam/junk folder.
    4.  If issues persist, contact IT support for further investigation.

### 2. Azure Virtual Desktop Access Problems

*   **Issue:** Unable to access the Azure Virtual Desktop.
*   **Troubleshooting Steps:**
    1.  Ensure you have a stable internet connection.
    2.  Verify your login credentials are correct.
    3.  Confirm you are using the correct Azure Virtual Desktop link.
    4.  If the problem persists, contact IT support for assistance.

### 3. Slack Log Inconsistencies

*   **Issue:** Discrepancies in Slack time logs or activity updates.
*   **Troubleshooting Steps:**
    1.  Review the "Slack Log Schedule Guide" to ensure adherence to the correct format and frequency.
    2.  Ensure all required information (Time In/Out, VAX PH, Activity) is included in each log.
    3.  If a log was missed, add it retroactively with a note explaining the delay.

---
## Timezone Reference

**Key Time Zones:**
-   **PHT:** Philippine Standard Time
-   **PST:** Pacific Standard Time

**Operational Hours:**
-   **PST:** 8:30 AM - 5:30 PM (Working Hours)
-   **PHT:** 11:30 PM - 8:30 AM (Corresponding Working Hours)

**Note:** Refer to the Slack Log Schedule Guide for detailed activity timings within these operational hours.
---

### Communication Routine

This section details the routine communication protocols, including WhatsApp and Email templates, to ensure consistent and timely information dissemination.

#### WhatsApp Templates

**Purpose:** To provide quick, daily updates to relevant stakeholders.

**1. Daily Update (Frequency: Daily)**

*   **Template:**
    ```
    Hi @ [Recipient Name],

    I've attached the Daily KPI Report for Seculife and Speedtalk and sent it via email. I have also sent the Inventory and Sales Report via email. Will proceed to morning checks.
    ```

**2. Returns Report Update (Frequency: Every Tuesday)**

*   **Template:**
    ```
    Hi @ [Recipient Name], I just sent you an email with the Yesterday and Last 30 Days Returns Report for SecuLife Inc and Speedtalk.
    ```

**3. Weekly Removal Order Update (Frequency: Every Wednesday)**

*   **Template:**
    ```
    Hi @ [Recipient Name] @ [Recipient Name 2],

    I have completed the weekly recalled/removal order for SecuLife and STK.
    ```


---

#### Email Templates

**Purpose:** To provide formal reports and updates to relevant stakeholders via email.

**1. Inventory and Sales Report**

*   **Frequency:** Daily
*   **Template:**
    ```
    Hi Avi,

    I've attached the Inventory and Sales Report for Seculife and Speedtalk.

    Best regards,
    Wesley Quintero
    ```

**2. Returns Report**

*   **Frequency:** Every Tuesday
*   **Template:**
    ```
    Hi Avi,

    I've attached the Returns Report for Seculife and Speedtalk.

    Best regards,
    Wesley Quintero
    ```

**3. Daily KPI Report**

*   **Frequency:** Daily
*   **Template:**
    ```
    Hi Avi,

    I've attached the Daily KPI Report for Seculife and Speedtalk.

    Best regards,
    Wesley Quintero
    ```

**4. Removal Report**

*   **Frequency:** Every Wednesday
*   **Template:**
    ```
    Hi Avi,

    I've attached the Removal Report for Seculife and Speedtalk.

    Best regards,
    Wesley Quintero
    ```

---

#### Email Distribution Lists

**Purpose:** To ensure reports are sent to the correct stakeholders.

**1. Daily Reports (Inventory Sales, KPI)**

*   **Recipients:**
    *   `avi@mobilenetus.com`
    *   `anna@mobile-net.us`
    *   `javier.garcia@speedtalkmobile.com`
    *   `Shelley@noirincusa.com`
    *   `fernanda.cortes@speedtalkmobile.com`
    *   `ran.quinga@speedtalkmobile.com`
    *   `juan.manuel@seculife.us`

**2. Monthly Sales Report**

*   **Recipients:**
    *   `jennice@mobile-net.us`
    *   `javier.garcia@speedtalkmobile.com`
    *   `billing@mobilenetus.com`
    *   `avi@mobilenetus.com`
    *   `anna@mobile-net.us`

---

## Azure Virtual Desktop Access

**Purpose:** To provide secure access to virtualized environments for managing brand-specific operations.

**Policy:**
-   Azure Virtual Desktop provides access to virtual computers for each store.
-   **Crucially, always access the Amazon store from its related virtual computer.**
-   **DO NOT** access the SpeedTalk Amazon store from the SecuLife Azure computer, and vice versa.

**Access Link:**
[Azure Virtual Desktop](https://client.wvd.microsoft.com/arm/webclient/index.html)

---

## Email Distribution Group Setup

**Purpose:** To centralize email communications from multiple brands into a single primary inbox for streamlined management.

**Configuration Details:**

-   **Distribution Groups Created:**
    *   `john.wesley.quintero@joltmobile.com`
    *   `john.wesley.quintero@speedtalkmobile.com`

-   **Forwarding Rule:** All emails sent to the above distribution groups are automatically forwarded to the primary email address:
    *   **Main Inbox:** `john.wesley.quintero@seculife.us`

**Benefit:** This setup ensures that correspondence for Jolt Mobile and Speedtalk Mobile is consolidated within the SecuLife email environment, simplifying email management and response.

---



