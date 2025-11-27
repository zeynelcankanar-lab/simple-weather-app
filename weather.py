# Simple Weather App - Fake Data

weather_data = {
    "Ankara": "Güneşli - 25°C",
    "İstanbul": "Parçalı Bulutlu - 22°C",
    "İzmir": "Açık - 27°C",
    "Bursa": "Yağmurlu - 18°C"
}

print("=== Basit Hava Durumu Uygulaması ===")
city = input("Şehir adı giriniz: ")

if city in weather_data:
    print(f"{city} için hava durumu: {weather_data[city]}")
else:
    print("Bu şehir için veri bulunamadı.")
