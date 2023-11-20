from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://pfm.smartcitylk.org/wp-admin/profile.php")

username_field = driver.find_element(By.NAME, "log")
password_field = driver.find_element(By.NAME, "pwd")

username_field.send_keys("user id")
password_field.send_keys("password")

login_button = driver.find_element(By.ID, "wp-submit")
login_button.click()

wait = WebDriverWait(driver, 10)

provinces = ["Northern", "North Central", "Eastern", "Uva", "Southern", "Western", "North Western", "Central", "Sabaragamuwa"]
districts = [
    ["Jaffna", "Kilinochchi", "Mullaitivu", "Mannar", "Vavuniya"],
    ["Polonnaruwa", "Anuradhapura"],
    ["Trincomalee", "Ampara", "Batticaloa"],
    ["Badulla", "Moneragala"],
    ["Galle", "Matara", "Hambantota"],
    ["Colombo", "Gampaha", "Kalutara"],
    ["Kurunegala", "Puttalam"],
    ["Kandy", "Matale", "Nuwara-Eliya"],
    ["Kegalle", "Ratnapura"]
]

type_of_las = ["PS", "UC", "MC"]

local_authorities = [
    "Chavakachcheri PS", "Chavakachcheri UC", "Delft PS", "Jaffna MC", "Karainagar PS", 
    "Kayts PS", "Nallur PS", "Point Pedro PS", "Point Pedro UC", "Vadamaradchi South West PS", 
    "Valikamam East PS", "Valikamam North PS", "Valikamam South PS", "Valikamam South West PS", 
    "Valikamam West PS", "Valvetithurai UC", "Velanai PS", "Karachchi PS", "Pachchilaipalli PS", 
    "Poonakary PS", "Manthai East PS", "Maritimepattu PS", "Puthukudiyiruppu PS", "Thunukkai PS", 
    "Mannar PS", "Mannar UC", "Manthai West PS", "Musali PS", "Nanattan PS", "Vavuniya North PS", 
    "Vavuniya South (Sinhala) PS", "Vavuniya South (Tamil) PS", "Vavuniya UC", "Vengalasettikula PS", 
    "Anuradhapura MC", "Galenbindunuwewa PS", "Galnewa PS", "Horowpothana PS", "Ipalogama PS", 
    "Kahatagasdigiliya PS", "Kebithigollewa PS", "Kekirawa PS", "Medawachchiya PS", "Mihintale PS", 
    "Nochchiyagama PS", "Nuwaragam Palatha Central PS", "Nuwaragam Palatha East PS", "Padaviya PS", 
    "Palagala PS", "Rajanganaya PS", "Rambewa PS", "Talawa PS", "Tirappane PS", "Dimbulagala PS", 
    "Elehera PS", "Hingurakgoda PS", "Lankapura PS", "Medirigiriya PS", "Polonnaruwa MC", 
    "Polonnaruwa PS", "Welikanda PS", "Gomarankadawala PS", "Kantale PS", "Kinniya PS", 
    "Kinniya UC", "Kuchchaweli PS", "Morawewa PS", "Muttur PS", "Padavisiripura PS", "Seruvila PS", 
    "Thambalagamuwa PS", "Trincomalee Town and Gravets PS", "Trincomalee UC", "Verugal PS", 
    "Addalachenai PS", "Akkaraipattu MC", "Akkaraipattu PS", "Alaiyadivembu PS", "Ampara UC", 
    "Damana PS", "Dehiattakandiya PS", "Irakkamam PS", "Kalmunai MC", "Karaitivu PS", "Lahugala PS", 
    "Maha Oya PS", "Namal Oya PS", "Naveethanveli PS", "Ninthavur PS", "Padiyatalawa PS", "Pottuvil PS", 
    "Sammanthurai PS", "Thirukkovil PS", "Uhana PS", "Batticaloa MC", "Eravur Pattu PS", "Eravur UC", 
    "Kattankudi UC", "Koralaipattu North PS", "Koralaipattu PS", "Koralepattu West PS", 
    "Manmunal Pattu PS", "Manmunal South and Eruvil Pattu PS", "Manmunal South West PS", 
    "Manmunal West (Vavunatheev) PS", "Porativpattu PS", "Badulla MC", "Badulla PS", "Bandarawela MC", 
    "Bandarawela PS", "Ealla PS", "Haldummulla PS", "Hali-Ela PS", "Haputale PS", "Haputale UC", 
    "Kandeketiya PS", "Lunugala PS", "Mahiyanganaya PS", "Meegahakivula PS", "Passara PS", 
    "Ridimaliyadda PS", "Soranathota PS", "Uva-Paranagama PS", "Welimada PS", "Badalkumbura PS", 
    "Bibila PS", "Buttala PS", "Kataragama PS", "Madulla PS", "Medagama PS", "Moneragala PS", 
    "Siyambalanduwa PS", "Tanamalwila PS", "Wellawaya PS", "Ambalangoda PS", "Karandeniya PS", 
    "Rajgama PS", "Akmeemana PS", "Baddegama PS", "Niyagama PS", "Bentota PS", "Elpitiya PS", 
    "Galle MC", "Habaraduwa PS", "Hikkaduwa PS", "Karapitiya PS", "Nagoda PS", "Ambagamuwa PS", 
    "Balangoda PS", "Imbulpe PS", "Kolonne PS", "Kotakethana PS", "Ratnapura MC", "Weligepola PS",
    "Ayagama PS", "Balangoda PS", "Embilipitiya UC", "Rathnapura MC"
]



while True:
    change_button = wait.until(EC.element_to_be_clickable((By.ID, "change")))
    change_button.click()

    for province in provinces:
        province_select_element = wait.until(EC.presence_of_element_located((By.NAME, "province")))
        province_select = Select(province_select_element)
        province_select.select_by_visible_text(province)

        for j in range(9):
            for district in districts[j]:
                dis_select_element = wait.until(EC.presence_of_element_located((By.NAME, "district")))
                dis_select = Select(dis_select_element)
                dis_select.select_by_visible_text(district)

                for type_of_la in type_of_las:
                    Tla_select_element = wait.until(EC.presence_of_element_located((By.NAME, "type_of_la")))
                    Tla_select = Select(Tla_select_element)
                    Tla_select.select_by_visible_text(type_of_la)

                    for la in local_authorities:
                        la_select_element = wait.until(EC.presence_of_element_located((By.NAME, "la_name")))
                        la_select = Select(la_select_element)
                        

                        if not la_select_element.find_element(By.XPATH, f"//option[text()='{la}']").is_enabled():
                            print(f"Skipping disabled option: {la}")
                            continue
                        
                        la_select.select_by_visible_text(la)

                        change_button1 = driver.find_element(By.ID, "submit")
                        change_button1.click()

                        change_button1 = driver.find_element(By.ID, "submit")
                        change_button1.click()

