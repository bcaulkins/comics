#Comics database and reference app
#Author Brian Caulkins 7.27.2024
#v0.1.0

import mokkari, sqlite3

#Metron username/password stored in separate config file
from config import username, password

#sets the Metron api info using the username/password from the config file
m = mokkari.api(username,password)

#opens a file called barcodes. File has one barcode per line
file = open('/home/brian/comics/barcodes.txt','r')
content = file.readlines()

#removes newline from barcode file and puts them into a new list called res
res = []
for sub in content:
    res.append(sub.replace("\n", ""))

#print(content)
#print(res)

#closes file after reading in the barcodes
file.close()

#upc = '70985301166806611'

#database code

# def create_sqlite_database(filename):
#     """ create a database connection to an SQLite database """
#     conn = None
#     try:
#         conn = sqlite3.connect(filename)
#         print(sqlite3.sqlite_version)
#     except sqlite3.Error as e:
#         print(e)
#     finally:
#         if conn:
#             conn.close()


# if __name__ == '__main__':
#     create_sqlite_database("comics.db")


entries = {}
#this section uses the barcodes to search the Metron database and return different pieces of data
for i in res:
        #searches the issues_list schema using the upc field
        comics = m.issues_list({"upc":i})
        for i in comics:
              #print(f"{i.id} {i.issue_name}")
              
              #returns the issue id
              c_id = m.issue(i.id)

              #returns the series id using the issue schema series id field
              s_id = m.series(c_id.series.id)

              #returns the publiser id using the issue schema publisher id field
              p_id = m.publisher(c_id.publisher.id)
              
              entries[c_id.upc]={"metron_id":c_id.id,
                              "issue":i.issue_name,
                              "price":c_id.price,
                              "series":s_id.name,
                              "publisher":p_id.name,
                              "issue_num":c_id.number,
                              "cover_img_url":c_id.image,
                              "upc":c_id.upc}
              #returns all the data using the issue, series and publisher calls
              print('Metron ID: '+ str(c_id.id) + 
                    '\n Issue: '+ i.issue_name +
                    '\n Price: ' + str(c_id.price)+
                    '\n Series: ' + s_id.name +
                    '\n Publisher: '+ p_id.name +
                    '\n Issue #: '+str(c_id.number)+
                    '\n Img URL: '+c_id.image +
                    '\n')
print(entries)