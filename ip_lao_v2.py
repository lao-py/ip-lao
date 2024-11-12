import requests
from pyfiglet import Figlet
import folium

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)

        data = {
            '[IP]': response.get('query'),
            '[INT. PR0V]': response.get('isp'),
            '[0RG]': response.get('org'),
            '[C0UNTRY]': response.get('country'),
            '[R3G10N NAME]': response.get('regionName'),
            '[C1TY]': response.get('city'),
            '[Z1P]': response.get('zip'),
            '[LAT]': response.get('lat'),
            '[L0N]': response.get('lon'),
        }

        for k, v in data.items():
            print(f'{k} : {v}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('[-]Check your internet connection')


def main():
    preview_text = Figlet(font='univers')
    print(preview_text.renderText('IP LAO'))
    print('')
    print('https://github.com/lao-py/ip-lao')
    ip = input('~l@osint 3NTER TARGET IP: ')

    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()
