from geoip import geolite2

def get_country_from_ip(ip):
    match = geolite2.lookup(ip)
    if match:
        return match.country

    return 'N/A'