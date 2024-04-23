import requests
from bs4 import BeautifulSoup

def get_survey_numbers(district, mandal, village):
    url = "https://dharani.telangana.gov.in/knowLandStatus"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    data = {
        "district": district,
        "mandal": mandal,
        "village": village
    }

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        survey_numbers = soup.find("select", {"name": "surveyNumber"}).find_all("option")
        survey_numbers = [option.text.strip() for option in survey_numbers if option.text.strip()]
        return survey_numbers
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        return []

def main():
    district = input("Enter district: ")
    mandal = input("Enter mandal: ")
    village = input("Enter village: ")

    survey_numbers = get_survey_numbers(district, mandal, village)
    if survey_numbers:
        print("Survey Numbers:")
        for number in survey_numbers:
            print(number)
    else:
        print("No survey numbers found.")

if __name__ == "__main__":
    main()
