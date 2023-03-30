
def mail(us,pw,md):
    import smtplib as smtp
    s = smtp.SMTP('smtp.gmail.com',587)
    s.starttls()
    print("started ttls")
    s.login(us,pw.decode('utf-8'))
    print("logged in")
    receiver_email_id= input("Who should I send the email to :")
    message = input("Enter message")
    s.sendmail(us,receiver_email_id,message)
    s.quit()
    output = f"Message send to {receiver_email_id}"
    return output
