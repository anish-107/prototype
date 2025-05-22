# Appointment Form Feature Documentation

## 1. Current Status

The current appointment form is a static webpage served through the `/appointment` route. It provides a form where users can enter their:

* Full Name
* Email Address
* Preferred Date and Time
* Purpose or reason for the appointment

At this point, the form does **not** do anything when submitted. There is no backend to receive the data, no calendar integration, and no confirmation system. It acts as a placeholder and visual template for what will be built in the future.

---

## 2. What This Feature Will Do

The goal of this feature is to create a **fully working appointment booking system** that makes it easier for users to schedule time with the professor.

Here's how it should work once fully implemented:

1. A user fills out the form and submits their appointment request.
2. The backend receives the request and creates a **pending appointment** on the professor’s Google Calendar.
3. The professor sees this request in their calendar and either accepts or declines it.
4. If accepted, the user receives an automatic email confirmation.
5. If declined, the user is informed politely and encouraged to reschedule.

This would save everyone time and make the process much smoother—no back-and-forth emails.

---

## 3. How to Implement It Step-by-Step

To make this work, you'll need backend logic to handle form submissions, talk to the Google Calendar API, and send email notifications. Below is a breakdown of how to implement each part.

---

### Step 1: Enable Google Calendar API

Before anything, you need permission to add events to the professor’s calendar.

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create or open a project.
3. Enable the **Google Calendar API** for that project.
4. Set up **OAuth 2.0 credentials**. This will let your backend securely talk to Google.
5. Make sure you request scopes like:

   * `https://www.googleapis.com/auth/calendar.events`
   * `https://www.googleapis.com/auth/calendar`

Once done, download the credentials (usually a JSON file) and store them securely in your backend (not in frontend or public repo), if using a public repo make sure to use .env and mention it in the .gitignore file.

---

### Step 2: Backend Input Handling

When the form is submitted:

1. Send the form data to the backend using a POST request.
2. Validate the following:

   * The **email** is valid (contains `@` and domain).
   * The **date and time** are properly formatted.
   * The **name** and **message** are not empty.

You may also want to check if:

* The appointment time is not in the past.
* There’s no conflict with existing calendar events.

---

### Step 3: Create Calendar Event (as Tentative)

Use Google Calendar API to insert the event.

Here’s what the event object should include:

* **Summary**: e.g., “Appointment with John Doe”
* **Description**: Full purpose/reason provided by the user.
* **Start and End Time**: Format should match ISO 8601.
* **Attendees**: Add user’s email as a guest.
* **Status**: You can mark it as `"tentative"` to show it's awaiting approval.

Example payload:

```python
event = {
  "summary": f"Appointment with {name}",
  "description": purpose,
  "start": {"dateTime": start_time, "timeZone": "Asia/Kolkata"},
  "end": {"dateTime": end_time, "timeZone": "Asia/Kolkata"},
  "attendees": [{"email": user_email}],
  "status": "tentative"
}
```

Store the event ID if you plan to check back later for updates or cancellations.

---

### Step 4: Send Confirmation or Rejection Email

Once the event is accepted by the professor:

* Use a mail server (SMTP) to send a **confirmation email** to the user.
* The email should include:

  * Date and time of the meeting
  * Professor's name
  * Any location or link if it’s an online meeting

If the professor declines the event (or removes it), you can notify the user and offer to reschedule.

To check the event status, you can:

* Set up **Google push notifications**, or
* Periodically **poll the event status** using the event ID

---

### Step 5: Security Considerations

* **Protect API keys and credentials**: Store them in a `.env` file or secret vault.
* **Add CAPTCHA** to the form to prevent bots.
* Use **rate limiting** to prevent spam or abuse.
* Sanitize all inputs before using them in calendar events or email bodies.

---

### Step 6: Logging and Maintenance

* Keep logs of:

  * Who requested what appointment and when
  * Event creation success or failure
  * Emails sent
* Log any errors that happen when calling the Google API or sending emails.
* Monitor your Google API quota to avoid hitting usage limits.

---

## Final Thoughts

This feature adds real value to the site by letting users book time directly with the professor, and it does so in a professional and efficient way. Once connected to Google Calendar and email, it turns the static form into a fully working scheduling tool.

The frontend doesn’t need major changes—the logic can be added in the backend, keeping the interface simple and user-friendly.

If you're working in a team, make sure someone with access to the professor's Google account sets up the API integration and gives you the right credentials to use.

---
