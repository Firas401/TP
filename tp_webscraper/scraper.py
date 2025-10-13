import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def main():
    url = "https://news.ycombinator.com/item?id=42919502"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Trouver les éléments avec indentation 0
    elements = soup.find_all(class_="ind", indent=0)
    comments = [e.find_next(class_="comment") for e in elements]

    # Dictionnaire des langages à rechercher
    keywords = {"python": 0, "javascript": 0, "typescript": 0, "go": 0, "c#": 0, "java": 0, "rust": 0}

    # Parcourir chaque commentaire
    for comment in comments:
        words = {w.strip(".,/:;!@") for w in comment.get_text().lower().split(" ")}
        for k in keywords:
            if k in words:
                keywords[k] += 1

    # Afficher les résultats
    print(keywords)

    # Afficher un graphique
    plt.bar(keywords.keys(), keywords.values())
    plt.xlabel("Language")
    plt.ylabel("# of Mentions")
    plt.title("Programming Languages Mentioned in HN Job Posts")
    plt.show()

if __name__ == "__main__":
    main()
