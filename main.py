'''

Exercise 7c
URL-encode characters

In URLs, we often replace special and nonprintable
characters with a % followed by the character’s ASCII value in hexadecimal. For
example, if a URL is to include a space character (ASCII 32, aka 0x20), we
replace it with %20 . Given a string, URL-encode any character that isn’t a letter
or number. For the purposes of this exercise, we’ll assume that all characters
are indeed in ASCII (i.e., one byte long), and not multibyte UTF-8 characters. It
might help to know about the ord (http://mng.bz/EdnJ) and hex (http://mng
.bz/nPxg) functions.

'''

def url_encode(url):
    output = []
    for character in list(url):
        if character.lower() not in '1234567890abcdefghijklmnopqrstuvwxyz':
            output.append( f'%{str(hex(ord(character)))[2:]}' ) # conver char to url encoded code 
        else:
            output.append(character)
    return ''.join(output)

print('ORIGINAL STRING:      The mask hides a terrible secret.')
print(f"URL_ENCODED STRING:   {url_encode('The mask hides a terrible secret.')}")