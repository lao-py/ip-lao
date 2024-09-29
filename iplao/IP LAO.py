import requests
from pyfiglet import Figlet
import folium

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)

        data = {
            '[IP]': response.get('query'),
            '[1NT. PR0V]': response.get('isp'),
            '[0RG]': response.get('org'),
            '[C0UN7RY]': response.get('country'),
            '[R3G10N N4M3]': response.get('regionName'),
            '[C1TY]': response.get('city'),
            '[Z1P]': response.get('zip'),
            '[L4T]': response.get('lat'),
            '[L0N]': response.get('lon'),
        }

        for k, v in data.items():
            print(f'{k} : {v}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('[ERR]Check your internet connection')


def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP LAO'))
    print('by @c_lao, @laosint')
    ip = input('3NT3R T4RG3T IP: ')

    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()
