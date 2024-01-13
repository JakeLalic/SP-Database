from SPDb import SPDb
from SPGuiCtk import SPDbGuiCtk

def main():
    db = SPDb(init=False, dbName='SPDb.csv')
    app = SPDbGuiCtk(dataBase=db)
    app.mainloop()

if __name__ == "__main__":
    main()