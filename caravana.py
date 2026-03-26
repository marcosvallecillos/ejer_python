import requests
import json

URL = "https://flexemcar.com.es/wp-admin/admin-ajax.php"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

def get_vehiculos(page=1):
    data = {
        "action": "wdk_listings",   # <- puede variar, míralo en Network
        "page": page
    }

    r = requests.post(URL, headers=HEADERS, data=data)
    return r.json()


def main():
    page = 1
    all_vehiculos = []

    while True:
        print(f"Página {page}...")
        data = get_vehiculos(page)

        if not data or len(data.get("results", [])) == 0:
            break

        for v in data["results"]:
            vehiculo = {
                "titulo": v.get("title"),
                "slug": v.get("slug"),
                "precio": v.get("price"),
                "imagenes": v.get("images"),
                "descripcion": v.get("description")
            }

            all_vehiculos.append(vehiculo)

        page += 1

    # Guardar JSON
    with open("vehiculos.json", "w", encoding="utf-8") as f:
        json.dump(all_vehiculos, f, indent=4, ensure_ascii=False)

    print("✅ Scraping completo con imágenes y slugs reales")


if __name__ == "__main__":
    main()