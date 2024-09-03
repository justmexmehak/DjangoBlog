import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('mehaknauman23@gmail.com', 'bskhhvbhxcsdljlj')
    server.sendmail('mehaknauman23@gmail.com', 'mehaknauman23@gmail.com', 'Test email from smtplib')
    server.quit()
    print("Email sent successfully")
except Exception as e:
    print(f"Error: {e}")
