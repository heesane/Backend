from sqlalchemy.orm import Session
from routes.stocks.stocks_schema import StocksCreate,StocksUpdate
from models import Stocks

# 재고 전체 리스트 조회
def get_stocks_list(db:Session):
    stocks_list = db.query(Stocks).all()
    total = db.query(Stocks).count()
    
    return total, stocks_list

# 재고 상세 조회
def get_stock(db:Session, stock_id:int=0,stock_name:str=""):
    if stock_id == 0:
        return db.query(Stocks).filter(Stocks.name == stock_name).first()
    elif stock_name == "":
        
        return db.query(Stocks).get(stock_id).first()

def create_stocks(db:Session, stock_create:StocksCreate):
    db_stock = Stocks(name=stock_create.name, price=stock_create.price, amount=stock_create.amount)
    db.add(db_stock)
    db.commit()
    
def update_stocks(db:Session, prev_stock:Stocks,stock_update:StocksUpdate):
    
    prev_stock.name = stock_update.name
    prev_stock.price = stock_update.price
    prev_stock.amount = stock_update.amount
    
    db.add(prev_stock)
    db.commit()
    
def delete_stocks(db:Session, stock:Stocks):
    db.delete(stock)
    db.commit()