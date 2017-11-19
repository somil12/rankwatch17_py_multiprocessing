import smtplib #to use smtp library function
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import csv #this module using for csv
import multiprocessing  # the module we will be using for multiprocessing



def send_mail(info):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = info[1]
    msg.attach(MIMEText(info[2], 'plain'))
    text = msg.as_string()
    server.sendmail(fromaddr, info[0], text)

if __name__ == "__main__":  # Allows for the safe importing of the main module
    filename = "fcku.csv" 
    print("There are %d CPUs on this machine" % multiprocessing.cpu_count())
    number_processes = 2
    pool = multiprocessing.Pool(number_processes)
    info = []
    with open(filename, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                info.append(row)
    fromaddr = "YOUR ADDRESS" # you can put your email address whatever you want
    server = smtplib.SMTP('smtp.gmail.com', 587) # to put server and port number
    server.starttls()
    server.login(fromaddr, "YOUR PASSWORD")#for password setup
    
    results = pool.map_async(send_mail, info)
    pool.close()
    pool.join()
