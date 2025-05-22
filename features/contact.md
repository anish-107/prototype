# Contact Form Feature Documentation

## 1. Current Functionality

The current contact form implementation provides a user interface where visitors can submit their:

- Name
- Email address
- Subject of the message
- Message content

When the form is submitted, the input data is sent asynchronously to the backend server using JavaScript. The server receives the data, performs basic validation to ensure all required fields are present, and then logs the received information for debugging purposes.

Currently, the backend does **not** send an email or store the submission in a database; instead, it responds with a success message indicating that the message has been received.

This implementation primarily serves as a placeholder and proof-of-concept for handling contact form submissions.

---

## 2. Intended Feature

The ultimate goal is for the contact form to actively send a formatted email to a specified recipient (such as the professor or department staff) whenever a visitor submits the form.

The email should include all submitted details, structured in a clear and readable format, allowing the recipient to:

- Easily identify the sender’s name and contact email
- Understand the subject and the content of the message
- Respond or take appropriate follow-up actions

This feature would provide a direct communication channel from the website visitors to the responsible personnel without requiring manual intervention or database queries.

---

## 3. Guidelines for Implementation with a Mail Server

When a mail server is available, the contact form feature can be enhanced to send emails by integrating the backend with the server’s SMTP or equivalent mail protocol.

The key steps and considerations for this enhancement are:

### a) Input Validation and Sanitization

- Rigorously validate the format of the email address to prevent malformed inputs.
- Optionally, implement CAPTCHA or rate-limiting to prevent abuse of the form.

### b) Email Composition

- Construct the email message in a structured format, clearly labeling each piece of information (e.g., Name, Email, Subject, Message).
- Use appropriate content types (plain text or HTML) to enhance readability.
- Consider adding metadata such as timestamps or IP addresses for audit trails.

### c) Mail Server Configuration

- Connect securely to the mail server using encrypted protocols (e.g., TLS or SSL) to protect credentials and email content.
- Authenticate using valid credentials or certificates as required by the mail server.
- Handle server responses and errors gracefully to provide meaningful feedback to users.

### d) Error Handling and Logging

- Implement error handling to capture failures in sending emails.
- Inform users if their message could not be sent due to technical problems.

### e) Security and Privacy

- Avoid exposing sensitive credentials in the codebase; use environment variables (.env) or secure configuration management.

---
