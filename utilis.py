import sqlite3
import newspaper
from newspaper import Article


def get_all(query):
    conn = sqlite3.connect("../news/news.db")
    cursor = conn.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

def get_new_by_id(new_id):
    conn = sqlite3.connect("../news/news.db")
    sql = """
        SELECT news.subject, news.description , news.image, news.original_url, category.name
        FROM news inner join category on news.category_id = category.id
        where news.id = ?
    """
    cursor = conn.execute(sql, (new_id, )).fetchone()
    conn.close()
    return cursor

def get_news_url():
    cates = get_all("SELECT *FROM category")
    conn = sqlite3.connect("../news/news.db")
    for cate in cates:
        cate_id = cate[0]
        cate_url = cate[2]
        cate_paper = newspaper.build(cate_url)
        for category2 in cate_paper.articles:
            try:
                print(category2.url)
                add_news(conn,category2.url,cate_id)
            except Exception as  ex:
                print("Error"+ str(ex))
                pass
    conn.close()



def add_news(conn,url,cate_id):
    sql = '''
    INSERT INTO news(subject, description, image,original_url, category_id)
    VALUES(?,?,?,?,?)
    '''
    article = Article(url)
    article.download()
    article.parse()
    conn.execute(sql, (article.title, article.text, article.top_image, article.url,cate_id, ))
    conn.commit()


if __name__ == "__main__":
    #print(get_all("select *from category"))
    #print(get_new_by_id(0))
    get_news_url()
