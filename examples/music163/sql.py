import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='sjq258369',
                             db='singer',
                             port = 3306,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
def insert_singer(singer_id, singer_name):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `singer` (`SINGER_ID`, `SINGER_NAME`) VALUES (%s, %s)"
        cursor.execute(sql, (singer_id, singer_name))
    connection.commit()
