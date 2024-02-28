import feedparser
import ssl
from langchain.llms import Ollama
from datetime import datetime

ssl._create_default_https_context = ssl._create_unverified_context

def getNews(url):
    feed = feedparser.parse(url)
    return [(entry.title, entry.summary) for entry in feed.entries] if not feed.bozo else None

def generate_summary(title, excerpt):
    prompt = " Below is an excerpt from an article on a current topic. Provide me with a concise but precise summary of this article. Ensure that the summary contains sufficient information about the topic, especially if there are unique or surprising aspects, so that it's not necessary to read the full article. Make sure your response is written in French.(if it's not in French, translate it into French without giving me the english version)"
    llm = Ollama(model="llama2")
    return llm.predict(prompt + title + excerpt)

def main():
    sources = {
        'futura': "https://www.futura-sciences.com/rss/high-tech/actualites.xml",
        'cnews': "https://www.cnews.fr/rss/categorie/monde",
        'bfmtv': "https://www.bfmtv.com/rss/tech/"
    }

    today = datetime.today().strftime('%d-%m-%Y')
    print(f"Voici l'actualité du jour : {today}\n")

    for source, url in sources.items():
        news_data = getNews(url)
        
        print(f"Source : {source}")
        if news_data:
            print(f"Nombre d'articles : {len(news_data)}\n")
        else:
            print("Aucun article trouvé\n")

        for title, excerpt in news_data:
            print(f"Titre : {title}")

            try:
                article_summary = generate_summary(title, excerpt)
                print(f"{article_summary}\n-----------------------------------\n")

            except Exception as e:
                print(f"Erreur lors de la génération du résumé : {e}")

    print(f"Fin des résumés de l'actualité du jour : {today}")

if __name__ == "__main__":
    main()
