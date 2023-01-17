

def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == '!hello' or p_message == '<@1064172616568541227> hello':
        return 'Hey there!'

    if p_message.split()[0] == '!googlesearch':
        return '**Processing links, wait one moment...**'

    if p_message == '!help':
        return '''
```       
$ Say !help for list with all commands.

$ Say !hello or **@quartz hello** and quartz bot will reply you.  

$ Use **!googlesearch {text}** to receive links with the most helpful information.

$ Use **?** before every command, to receive private message *(direct message)*
- Examples: ?!googlesearch *text*, ?!help, ?!hello.
```
'''


def google_search(p_message):
    try:

        from googlesearch import search

    except ImportError:

        print("No module named 'google' found")

    query = ''.join(p_message.split()[1:])
    result = '\n'.join([f'<{j}>' for j in search(query, tld="co.in", num=10, stop=10, pause=2)])
    return f'''
**`Found Results`**:
{result}
'''
