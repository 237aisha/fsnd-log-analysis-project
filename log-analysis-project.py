import psycopg2
DBNAME = "forum"
    

def main():
    q1()
    q2()
    q3()


def q1():
    # connect to the database
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    # first query
    Q1 = """SELECT title, count(*) AS views 
    FROM articles, log 
    WHERE concat('/article/', articles.slug) = log.path
    GROUP BY log.path, articles.title 
    ORDER BY views DESC LIMIT 3;"""
    # excute and fetch querie
    c.execute(Q1)
    result = c.fetchall()
    # print the result 
    print("Most popular three articles of all time: ")
    for i in result:
        print("- {} -- {} {}".format(str(i[0]), str(i[1]), 'views'))
    print("\n")
    # close connection
    c.close()
    db.close()
    

def q2():
    # connect to the database
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    # second query
    Q2 = """SELECT authors.name, count(*) AS views 
    FROM authors,articles,log 
    WHERE articles.author = authors.id 
    AND concat('/article/', articles.slug) = log.path
    GROUP BY authors.name
    ORDER BY views DESC LIMIT 3;"""
    # excute and fetch querie
    c.execute(Q2)
    result = c.fetchall()
    # print the result
    print("Most popular article authors of all time: ")
    for i in result:
        print("- {} -- {} {}".format(str(i[0]), str(i[1]), 'views'))
    print("\n")
    # close connection
    c.close()
    db.close()


def q3():
    # connect to the database
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    # third query
    Q3 = """SELECT count_date.date , 
            (100.00*count_error.errors/count_date.count) AS percent_error 
            FROM count_error,count_date
            WHERE count_date.date = count_error.date 
            AND (100.00*count_error.errors/count_date.count) >1
            ORDER BY date;"""
    # excute and fetch querie
    c.execute(Q3)
    result = c.fetchall()
    print("Days with more than 1% of error requests: ")
    for i in result:
        print("{} -- {}{}".format(str(i[0]), str(round(i[1], 2)), '% errors'))
    # close connection
    c.close()
    db.close()

if __name__ == "__main__":
    main()


