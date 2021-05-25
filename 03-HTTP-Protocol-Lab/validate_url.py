from urllib import parse


def get_protocol(scheme):
    if scheme in ('http', 'https'):
        return scheme
    return None


def get_host_and_port(netloc, scheme):
    if '.' not in netloc:
        return (None, None)
    if ':' not in netloc:
        default_port = 80 if scheme == 'http' else 443
        netloc = f'{netloc}:{default_port}'

    return netloc.split(':')


def get_path(path):
    return path or '/'


def get_fragment(fragment):
    return fragment


def get_query(query):
    return query


def validate_url(url):
    components = parse.urlparse(url)
    protocol = get_protocol(components.scheme)
    host, port = get_host_and_port(components.netloc, components.scheme)
    path = get_path(components.path)
    fragment = get_fragment(components.fragment)
    query = get_query(components.query)
    if None in (protocol, host, port, path):
        return 'Invalid URL'
    return f'''Protocol: {protocol}
Host: {host}
Port: {port}
Path: {path}
Query: {query}
Fragment: {fragment}'''


url = input()

print(validate_url(url))
