import smtplib  # imports stmp library used for accessing emails


def main():
    email = input("Enter your email address:\n")  # gathers user email address
    who = input("What email address are you sending too?\n")  # gets email address of the person receiving the email
    password = input("Enter your password\n")  # gets users password
    message(email, password, who)  #passes info to the message builder method


def message(e, p, w):
    text = input("Enter your message:")  # gets the message
    if len(text) > 2500:  # if the email is too big it won't send it
        print("Message is too long, enter a shorter message:")
        message(e, p, w)  # recalls itself
    server_sender(e, p, w, text)  # passes data to the sender


def server_sender(e, p, w, text):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(e, p)  # logs in
    server.sendmail(e, w, text)  # sends the message
    server.quit()


main()
