# Appointment Form Feature Documentation

## 1. Current Functionality

The current appointment feature consists of a frontend form served through the `/appointment` route. This form allows users to provide relevant details to request an appointment with the professor. The form likely includes fields such as:

- Full Name
- Email Address
- Date and Time of Appointment
- Purpose or Description

At this stage, the form is static and operates only on the client-side. There is no backend logic implemented to handle, store, or process the form data. It serves as a visual placeholder and template for future integration.

---

## 2. Intended Feature

The vision for this feature is to make appointment booking seamless and integrated. The full workflow is expected to function as follows:

### Step-by-Step Goal

1. A user fills out the appointment form and submits it.
2. The server receives the form data and creates a **tentative calendar event** on the professor's Google Calendar using the **Google Calendar API**.
3. The professor reviews the appointment request and either accepts or declines it.
4. Upon acceptance, the system sends an **automated confirmation email** to the user via the mail server.
5. Optionally, if declined, the system can notify the user with a polite rejection message and suggest rescheduling.

This process eliminates back-and-forth email coordination, streamlines calendar scheduling, and makes the system more efficient and user-friendly.

---

## 3. Guidelines for Future Implementation (Google Calendar Integration)

Someone who has authorized access to the professor’s Google Calendar and the appropriate API credentials can extend this functionality by integrating the Google Calendar API. The following outlines the key concepts and best practices for such an enhancement.

### a) Enable Google Calendar API

- Use Google Cloud Console to enable the **Google Calendar API** for the project.
- Set up OAuth 2.0 credentials to authorize access to the professor’s calendar.
- Ensure the necessary scopes are granted to allow event creation and response tracking.

### b) Capture and Validate Input

- On form submission, capture all required information.
- Validate date, time, and email format server-side.
- Prevent invalid or duplicate appointments.

### c) Create Event as "Pending"

- Construct a calendar event object that includes:
  - Summary (appointment subject)
  - Description (purpose of visit)
  - Start and End time
  - Attendee email
  - Status: `"tentative"` or `"needsAction"` to signal pending approval

- Insert the event using the Calendar API, marking it as not yet confirmed.
- Optionally, store the event ID for future reference or updates.

### d) Approval and Confirmation Logic

- The professor can accept the appointment via Google Calendar manually.
- When the event is marked as "accepted," a trigger or polling mechanism can be used to detect this status change.
- On acceptance, automatically send a **confirmation email** to the user through the mail server, informing them of the successful booking.

### e) Email Notification System

- Integrate with the existing mail server to send user-friendly and professional notifications.
- The email should include:
  - Confirmation message
  - Date and time of the appointment
  - Optional link to view/cancel the booking
- Ensure reliable delivery and fallback handling for failures.

### f) Security and Permissions

- Protect the form from spam submissions using CAPTCHA or throttling.
- Store Google API credentials securely and never expose them in frontend code. (use .env)
- Ensure only authorized personnel can access the calendar and event data.

### g) Logging and Maintenance

- Log appointment requests and event insertions for auditing purposes.
- Maintain error logs for troubleshooting failed requests or API issues.
- Monitor Google API quota usage and optimize requests accordingly.

---

## Summary

This feature is designed to bridge website interactions with real-time scheduling through Google Calendar. It saves time, reduces manual effort, and enhances the professionalism of the booking experience.

Anyone with access to the professor's calendar and credentials should be able to fully realize this workflow with minimal changes to the frontend. All backend hooks and integrations can be layered seamlessly on top of the existing static form template.

This modular setup allows non-technical staff to approve meetings via Google Calendar while giving users a modern and responsive appointment system.
