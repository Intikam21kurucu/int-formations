import requests

# Function to get the username input
def get_username():
    return input("Please enter the username you want to check: ")

# List of URLs for social media and popular platforms to check the username presence.
PLATFORM_URLS = {
    'Facebook': 'https://www.facebook.com/{}',
    'Twitter': 'https://www.twitter.com/{}',
    'Instagram': 'https://www.instagram.com/{}',
    'YouTube': 'https://www.youtube.com/{}',
    'GitHub': 'https://api.github.com/users/{}',
    'LinkedIn': 'https://www.linkedin.com/in/{}',
    # You can add other popular sites here.
}

def get_github_user_info(username):
    url = PLATFORM_URLS['GitHub'].format(username)
    response = requests.get(url)
    if response.status_code == 200:
        user_info = response.json()
        return user_info.get('avatar_url'), user_info.get('email')
    return None, None

def check_platform_presence(username):
    found_accounts = {}
    profile_image, email = get_github_user_info(username)
    if profile_image:
        found_accounts['GitHub'] = {'profile_image': profile_image, 'email': email}
    for platform, url in PLATFORM_URLS.items():
        if platform != 'GitHub':  # GitHub has already been checked.
            try:
                response = requests.get(url.format(username))
                if response.status_code == 200:
                    found_accounts[platform] = url.format(username)
                else:
                    found_accounts[platform] = None
            except requests.exceptions.RequestException as e:
                found_accounts[platform] = f'Error: {e}'
    return found_accounts

# Main function
def main():
    username = get_username()
    accounts = check_platform_presence(username)

    for platform, info in accounts.items():
        if isinstance(info, dict):  # For GitHub information
            print(f'{platform} account found: {info["profile_image"]}')
            if info['email']:
                print(f'Email address: {info["email"]}')
        elif info:
            print(f'{platform} account found: {info}')
        else:
            print(f'{platform} account not found or an error occurred.')

if __name__ == "__main__":
    main()
