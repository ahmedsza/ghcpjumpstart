import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class SMTPEmailSender:
    def __init__(self):
        """Initialize SMTP Email Sender with configuration from environment variables"""
        self.smtp_host = os.getenv('SMTP_HOST')
        self.smtp_port = int(os.getenv('SMTP_PORT', 587))
        self.smtp_username = "username"  
        self.smtp_password = "smtp_password"  
        self.from_email = "from_email"
        self.from_name = "from_name"
        
        # Validate required configuration
        if not all([self.smtp_host, self.smtp_username, self.smtp_password, self.from_email]):
            raise ValueError("Missing required SMTP configuration in .env file")

    def send_email(self, to_email, body, html_body=None, attachments=None):
        """
        Send an email using SMTP
        
        Args:
            to_email (str or list): Recipient email address(es)
            subject (str): Email subject
            body (str): Plain text email body
            html_body (str, optional): HTML email body
            attachments (list, optional): List of file paths to attach
        
        Returns:
            bool: True if email sent successfully, False otherwise
        """
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['From'] = f"{self.from_name} <{self.from_email}>"
            msg['Subject'] = "This is a test subject"

            # Handle multiple recipients
            if isinstance(to_email, list):
                msg['To'] = ', '.join(to_email)
                recipients = to_email
            else:
                msg['To'] = to_email
                recipients = [to_email]
            
            # Add text part
            text_part = MIMEText(body, 'plain')
            msg.attach(text_part)
            
            # Add HTML part if provided
            if html_body:
                html_part = MIMEText(html_body, 'html')
                msg.attach(html_part)
            
            # Add attachments if provided
            if attachments:
                for file_path in attachments:
                    if os.path.isfile(file_path):
                        with open(file_path, 'rb') as attachment:
                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload(attachment.read())
                        
                        encoders.encode_base64(part)
                        part.add_header(
                            'Content-Disposition',
                            f'attachment; filename= {os.path.basename(file_path)}'
                        )
                        msg.attach(part)
            
            # Create SMTP session
            server = smtplib.SMTP(self.smtp_host, self.smtp_port)
            server.starttls()  # Enable security
            server.login(self.smtp_username, self.smtp_password)
            
            # Send email
            text = msg.as_string()
            server.sendmail(self.from_email, recipients, text)
            server.quit()
            
            print(f"Email sent successfully to {recipients}")
            return True
            
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            return False

def main():
    """Example usage of SMTPEmailSender"""
    try:
        # Initialize email sender
        email_sender = SMTPEmailSender()
        
        # Example 1: Send simple text email
        print("Sending simple text email...")
        success = email_sender.send_email(
            to_email="ahmeds@microsoft.com",
            body="This is a test email sent using Python and Azure Communication Services SMTP."
        )
        
        # Example 2: Send HTML email
        if success:
            print("Sending HTML email...")
            html_content = """
            <html>
                <body>
                    <h2>HTML Email Test</h2>
                    <p>This is an <b>HTML email</b> sent using Python.</p>
                    <ul>
                        <li>Feature 1: Environment variable configuration</li>
                        <li>Feature 2: Support for attachments</li>
                        <li>Feature 3: HTML and plain text content</li>
                    </ul>
                </body>
            </html>
            """
            
            email_sender.send_email(
                to_email="ahmeds@microsoft.com",
                body="This is the plain text version of the email.",
                html_body=html_content
            )
        
        # Example 3: Send email with attachment (uncomment to use)
        # email_sender.send_email(
        #     to_email="recipient@example.com",
        #     subject="Email with Attachment",
        #     body="This email contains an attachment.",
        #     attachments=["path/to/your/file.txt"]
        # )
        
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please check your .env file contains all required SMTP settings.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()