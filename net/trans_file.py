import paramiko

def secure_file_transfer(source_file, destination_file, hostname, port, username, password):
    try:
        transport = paramiko.Transport((hostname, port))
        transport.connect(username=username, password=password)
        
        sftp = transport.open_sftp()
        sftp.put(source_file, destination_file)
        
        sftp.close()
        transport.close()
        
        print("File transferred successfully.")
    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials.")
    except paramiko.SSHException as e:
        print(f"SSH error: {str(e)}")
    except paramiko.SFTPException as e:
        print(f"SFTP error: {str(e)}")
    except Exception as e:
        print(f"Error occurred during file transfer: {str(e)}")

source_file = ''
destination_file = ''
hostname = 'viesoc.com'
port = 22
username = ''
password = ''

secure_file_transfer(source_file, destination_file, hostname, port, username, password)