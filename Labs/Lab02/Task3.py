
def convert_url(url):
    if url.startswith('http://www.'):
        return url[len('http://www.'):]
    else:
        return 'Invalid URL format.'

user_input = input('Enter your URL starting with http://www.: ')

converted_url = convert_url(user_input)
print('Converted URL:', converted_url)
