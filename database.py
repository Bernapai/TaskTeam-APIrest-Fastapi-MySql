from sqlalchemy import create_engine , MetaData

engine = create_engine('mysql+pymysql://root:Juanber123()@localhost:3306/taskteam')
meta = MetaData()
conn = engine.connect()