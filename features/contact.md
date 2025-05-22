#  Contact Form Feature

##  1. What the Contact Form Does Right Now

Currently, the contact form on the website allows visitors to fill in the following fields:

*  Their **Name**
*  Their **Email Address**
*  The **Subject** of their message
*  The actual **Message Content**

When the user clicks **Submit**, the form:

* Sends the data to the backend using **JavaScript (AJAX)** without reloading the page.
* The backend:

  * **Checks** if all required fields are filled.
  * **Prints** the data to the console (for testing).

 **Note:** Right now, the backend does **not** send emails or save anything in a database. It just shows a “Message received” response to the user.

---

## 🚀 2. What We Want to Add (The Goal)

We want to make the contact form actually **send an email** to the professor or department whenever someone submits it.

Here’s what we want the email to contain:

* Name of the sender
* Their email address
* The subject of the message
* The full message
* (Optional) The time and date the message was sent

This will help the staff receive messages directly in their inbox and reply quickly, **without checking the website backend** or a database.

---

## 3. How to Implement the Email Feature 

We will use a **mail server** (like Gmail, SendGrid, or an institutional SMTP server) to send emails directly from our backend.

###  A) Step 1 – Validate the Form Input

Before sending anything, we must make sure:

* All fields (Name, Email, Subject, Message) are **filled out**.
* The email address is in a **valid format** (like `example@email.com`).

Example

```python
import re

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)
```

Optional:

* Add a **CAPTCHA** (like Google reCAPTCHA) to prevent bots.
* Use **rate limiting** (e.g., max 5 messages/hour) to prevent spam.

---

###  B) Step 2 – Format the Email

Once input is valid, build the message in a readable format.

Example:

```plaintext
New Contact Form Submission:

Name: John Doe
Email: john@example.com
Subject: Collaboration Opportunity
Message:
Hi, I’m interested in collaborating on your research...

Sent on: 2025-05-22 14:10
```


---

###  C) Step 3 – Send the Email via SMTP

Use a mailing library (like `smtplib` in Python) to send the email.

#### Example in Python using `smtplib`:

```python
import smtplib
from email.mime.text import MIMEText

# Your credentials
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USERNAME = 'your-email@gmail.com'
EMAIL_PASSWORD = 'your-app-password'  # Use app-specific password or env variable

def send_contact_email(name, email, subject, message):
    body = f"""New Contact Form Message:

Name: {name}
Email: {email}
Subject: {subject}
Message:
{message}
"""

    msg = MIMEText(body)
    msg['Subject'] = f"New Contact Form Message: {subject}"
    msg['From'] = EMAIL_USERNAME
    msg['To'] = 'professor@university.edu'

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.send_message(msg)
```

👉 **Important:**

* Do **not hardcode credentials**. Store them in a `.env` file:

```env
EMAIL_USERNAME=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
```

Use libraries like `python-dotenv` to read `.env` files securely.

---

###  D) Step 4 – Handle Errors Gracefully

Sometimes, sending the email might fail (e.g., network issues, wrong SMTP credentials). So:

* Wrap the send code in a `try-except` block
* If it fails, return a message like:

```json
{ "status": "error", "message": "We couldn't send your message right now. Please try again later." }
```


### E) Step 5 – Security and Privacy

* Use **environment variables** for email credentials.
* Never expose email passwords in frontend or public code.
* Use **TLS/SSL** to encrypt the email.
* (Optional) Save email logs for security auditing.

---

##  4. Extra: Success Message and UI Feedback

After sending the email successfully:

* Show a success message on the website:

  ```
   Thank you! Your message has been sent.
  ```
* Optionally, disable the form or reset the fields.

If there’s an error, show a friendly error like:

```
 Sorry, there was a problem sending your message.
```

---

