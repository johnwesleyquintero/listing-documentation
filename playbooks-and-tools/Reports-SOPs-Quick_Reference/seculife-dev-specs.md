# **SecuLife/SecuPro Device & App Feature Compendium v1.0**

This document provides a comprehensive breakdown of features for the S-series tracking devices and a detailed user guide for the SecuPro mobile application.

---

## **Part 1: Device Feature Breakdown**

This section outlines the specific features available for each device model.

### **S8 Features**
- Small screen to show time, date, battery, and connectivity
- SOS calling
- Tracking
- Geofence
- Alarms and reminders
- Find My Device
- Fall Alerts
- Hands Free answering
- Long battery life (up to 8 days with 1 hour intervals)
- IP67 Waterproof

### **S9 Features**
- SOS calling
- Tracking
- Geofence
- Alarms and reminders
- Find My Device
- Fall Alerts
- Hands Free answering
- Fast SOS Calling (Will call SOS number instantly)
- Heart rate reader, Blood pressure reader, Blood Oxygen reader, and a pedometer
- Waterproof IPX8

### **SL16 Features**
- Small Display on watch
- 2-way calling
- SOS calling
- Tracking
- Geofence
- Alarms and reminders
- Fall Alerts
- Hands Free answering
- Heart rate reader, Blood pressure reader, temperature reader, and a pedometer
- IP67 Waterproof
- In-app text and voice messaging
- Do not disturb / Classroom time

### **SL17 Features**
- SOS calling
- Tracking
- Geofence
- Alarms and reminders
- Fall Alerts
- Hands Free answering
- Heart rate reader, Blood pressure reader, temperature reader, and a pedometer (Note: App visibility only, developer implementation is TBD)
- IP67 Waterproof
- App user can send voice messages to the SL16
- Do not disturb / Classroom time

---

## **Part 2: SecuPro App User Guide**

This section provides a detailed walkthrough of the SecuPro mobile application's features and functionality.

### **1. Account & Device Setup**

#### **Login Page**
- You cannot create an account directly from this page; account creation occurs during device activation.
- You must accept the terms and conditions to log in.
- You can reset your password using the "Forgot Password" link.

#### **How to Bind a Device to the App**
- You must input or scan the device's IMEI number (not a registration code).
- Input a nickname for the device (e.g., "Mom's Watch").
- Select your relationship to the watch user from a list of options.
- Tap "Confirm" when finished.
- The button on the bottom right is for logging out to switch accounts.

### **2. Main Interface**

#### **Homepage**
- Only features supported by the currently selected device will be shown on the main page.
- You can select which device to view by tapping the device picture in the top left.
- The device nickname and phone number are displayed at the top (phone number is added automatically).

#### **Device List**
- Displays all devices bound to your account.
- Bind another device by tapping the plus sign (+) on the top right.
- You can scroll down if you have more than 5 devices.
- Tapping on a device allows you to change its picture, nickname, and your relationship to the user.

#### **Profile Page**
- View your account details here.
- Unbind devices via the "Device List" menu item.
- Check Call Records, SMS Details, Refill your account, and access customer support.

### **3. Core App Features**

#### **Chat**
- Only available for supported devices.
- Functionality is similar to CarePro+ chat.
- Send text or voice messages to the device.
- Invite other people with the app to the group chat by adding their email and nickname.

#### **Remote Photo**
- Only available for supported devices.
- The first page shows previously taken remote photos.
- Tap "Take Photos" on the top right to go to the camera page.
- Tap the green camera icon in the middle to take a new remote photo.

#### **Call Device**
- Automatically inputs the device's phone number (MDN) into your phone's dialer for easy calling.
- The MDN is automatically assigned in the app upon device activation.

#### **Map**
- Similar to the CarePro+ map.
- Displays device battery, device location, last update time, and location at the bottom.
- Get an immediate location update by tapping the "Update Location" button on the bottom right.
- **Map Icons (Top to Bottom):**
    - **Person Icon:** Shows the location of your smartphone.
    - **Marker Icon:** Centers the map on the device's location (Red Marker).
    - **Phone Icon:** Opens the dialpad with the MDN pre-filled.
    - **Double Circle Icon:** Create a Geofence.
    - **Rewind Icon:** Shows tracking history.
    - **Two Square Icon:** Toggles map appearance (Normal, Satellite, Traffic).

#### **Geofence**
- Tap the orange button on the bottom to create a Geofence.
- Tap again to place a green marker, which will be the center of the Geofence (only circle Geofences are available).
- You can name the Geofence and adjust its range from 300m to 3000m.
- You can create 5+ Geofences.
- To delete a Geofence, swipe left on the one you want to delete.
- You can disable a Geofence by tapping the blue button to the right of the Geofence.

#### **Track History**
- Select a Start and End Time for the history you want to view.
- The "History" view shows all locations where the device updated.
- The "Replay" view shows the tracker's path in chronological order.

#### **Block Unknown Calls**
- Only available for supported devices.
- Works just like CarePro+.
- Tap the green button to enable call rejection.
- When enabled, only numbers in the device's phonebook can call it.
- Tap the button again (it will be red) to disable call rejection.

#### **Alarms**
- Only available for supported devices.
- Shows all alarms on the first page.
- Tap "Add Alarm" to create a new one.
- You can set the alarm type: Regular, Medication, Drink Water, or Sedentary.
- Set a specific date and time for the alarm to go off.

#### **Alerts**
- Shows the history of alerts and notifications sent by the device.
- Currently shows alerts for the selected device, but may have a toggle option in the future to show alerts from all devices.

#### **Tracking Interval**
- Choose how often the device reports its location (e.g., 1 minute, 15 minutes, 60 minutes) and press Save.
- More interval options may be added later.

#### **Find My Device**
- Plays a sound on the device until the SOS button is pressed.
- Useful if the device is misplaced or lost.

### **4. Device Settings**

- Different devices will have different features available on the settings page.

#### **SOS/Family Numbers**
- Supports up to three SOS numbers.
- When the SOS feature is triggered, it will call each number in order (1 to 3) until a call is answered.
- If only one number is entered, it will call that one number repeatedly.

#### **Account Members**
- Invite family members or friends who have the SecuPro app to bind to your device.
- This allows multiple people to monitor a single device.
- Enter their email address and name to send an invitation.

#### **Alert Settings**
- Choose what types of alerts to receive:
    - **App Notification:** Pop-up notifications on your phone.
    - **Email Notification:** Sends alerts to up to 3 email addresses.
    - **SMS Notification:** Sends alerts to up to 3 phone numbers.

#### **Fall Alerts**
- Allows you to enable or disable fall alerts (disabled by default).
- You can set the sensitivity of the fall detection.
- When triggered, the device will call the SOS numbers.

#### **Phonebook**
- Add multiple contacts to your device.
- You can set the name and number for each contact.
- Swipe left on a contact to delete it.

#### **Time Zone**
- Set different time zones and enable/disable daylight savings.

#### **Sync Assistant**
- Syncs settings from one device to another.
- Selecting a device from the list will change the current device's settings to match the selected one.

#### **Remote Shutdown and Factory Reset**
- **Remote Shutdown:** Turns off the device from the app (device must be online).
- **Factory Reset:** Wipes all data from the device and unbinds it from your account automatically.

### **5. Account Management**

#### **Personal Info**
- Edit the nickname of your account.

#### **Change Password**
- Change your SecuPro account password here.

#### **Device List (in Profile)**
- Functions like the main "Device List" but allows you to unbind devices by tapping "Edit" on the top right.

#### **Delete Account**
- You can permanently delete your SecuPro account here.
- This action is irreversible. You must create a new account if you wish to use the service again.

#### **Call Detail Records (CDR)**
- Shows records of calls, SMS, and data usage.
- Displays records for a maximum of the last 7 days.

#### **Refill Topup**
- A convenient way for the customer to refill their account.

#### **Contact Support**
- Takes you to the support page where you can open a ticket.

#### **Logout**
- Signs you out of your account and brings you back to the login page.
