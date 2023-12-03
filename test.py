from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()  # Edge tarayıcısı için webdriver kullanın


file = open("iphone12blue.txt", "w", encoding="utf-8")
file.close()

driver.get("https://www.trendyol.com/apple/iphone-12-128-gb-mavi-cep-telefonu-aksesuarsiz-kutu-apple-turkiye-garantili-p-66403057/yorumlar?boutiqueId=61&merchantId=427578")


time.sleep(3)




for i in range(1, 4000):
    uni_path = f"/html/body/div[1]/div[3]/div/div/div/div/div[3]/div/div/div[3]/div[2]/div[{i}]/div[2]/p"

    try:
        # By.XPATH ile find_element kullanın
        uni_name = driver.find_element(By.XPATH, uni_path).text

        with open("iphone12blue.txt", "a", encoding="utf-8") as f:   

         f.write(f"\n('{i} - {uni_name}  . ')")
         driver.execute_script("window.scrollTo(0,document.body.scrollHeight-1500)")
        
        print(uni_name)
      
       
       
        
    except Exception as e:
        print(f"{i}. veri alınırken hata oluştu: {e}")

driver.quit()
