'''This memory artifact extraction tool inputs a Google Meet memory dump to extract memory artifacts.
Dependencies include 1) Python, 2) Linux's strings.exe and 3) grep.
The subject tool is to be executed on a Linux Operating System with python installed.
'''


import subprocess
import sys
def extraction(command):
    p = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE)
    while True:
        out = p.stderr.read(1)
        decoded=out.decode()
        if decoded == '' and p.poll() != None:
            break
        if decoded != '':
            sys.stdout.write(decoded)
            sys.stdout.flush()
print('''1. Traces of usage
2. Meeting records
3. Communication records
4. Doc/image downloads
5. Correspondence emails''')
print('Extrating artifacts...')
extraction("strings memdump.mem | grep 'google meet.lnk' > Traces of usage.txt")
extraction("strings memdump.mem | grep 'bog_meetingsuiserver' > Meeting records.txt")
extraction("strings memdump.mem | grep '/devices/' > Communication records.txt")
extraction("strings memdump.mem | grep 'jamboard.google.com' > Doc image downloads.txt")
extraction("strings memdump.mem | grep 'recipientEmailAddresses' > Correspondence emails.txt")
print('done')
