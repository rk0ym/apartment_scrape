from bs4 import BeautifulSoup4
import requests


class GetSuumo():
    def __init__(self):
        self.target_url = "https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ra=013&cb=0.0&ct=8.0&co=1&et=15&cn=20&mb=20&mt=9999999&kz=1&kz=2&kz=4&tc=0400501&tc=0400601&tc=0400301&tc=0400903&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=&ek=004317640&ek=004339010&ek=004380835&ek=004319690&ek=004350015&ek=004380840&ek=004380845&ek=004302060&ek=004308710&ek=004321350&ek=004314950&rn=0043&ek=022017640&ek=022021850&ek=022027580&ek=022040640&ek=022007660&ek=022026730&ek=022018410&rn=0220"

    def get_items_info(self):
        res = requests.get(self.target_url)
        soup = BeautifulSoup(res.text, 'lxml')
        apartment_list = soup.find_all('//div[@class="cassetteitem"]')

        for apartment in apartment_list:
            self.get_description(apartment)

    def get_description(self, apartment):
        title = apartment.find('//div[@class="cassetteitem_content-title"]')
        area = apartment.find('//li[@class="cassetteitem_detail-col1"]')
        nearest_stations = apartment.find_all('//div[@class="cassetteitem_detail-text"]')
        nearest_stations = [s.text for s in nearest_stations]
        age = apartment.find('//li[@class="cassetteitem_detail-col3"]/div[0]')
        stories = apartment.find('//li[@class="cassetteitem_detail-col3"/div[1]')
        floor = apartment.find('//tr[@class="js-cassette_link"]/td[2]')
        
