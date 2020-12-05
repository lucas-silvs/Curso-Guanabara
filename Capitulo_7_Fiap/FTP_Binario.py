from ftplib import  *
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
ftp.login()
ftp.cwd('pub')

