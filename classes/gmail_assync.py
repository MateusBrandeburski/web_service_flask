from aiosmtplib import SMTP
import os

EMAIL_ADDRESS = os.environ["EMAIL"]
EMAIL_PASSWORD = os.environ["SENHA"]

async def send_email(subject, message):
    async with SMTP(hostname="smtp.gmail.com", port=465, use_tls=True) as smtp:
        await smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        await smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, f"Subject: {subject}\n\n{message}")