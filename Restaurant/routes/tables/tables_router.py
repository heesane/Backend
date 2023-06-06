from fastapi import APIRouter, Depends,Response
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from routes.tables import tables_crud, tables_schema

router = APIRouter(
    prefix="/api/table",
    tags=["Tables"]
)

@router.get("/list", response_model=tables_schema.TableList,summary="테이블 목록 전체 조회")
def table_list(db: Session = Depends(get_db)):
    total,table_list = tables_crud.get_table_list(db)
    
    return {
        'total': total,
        'table_list': table_list
    }
    
@router.get("/detail", response_model=tables_schema.Table,summary="특정 테이블 상세 조회")
def table_detail(table_id: int, db: Session = Depends(get_db)):
    table = tables_crud.get_table(db, table_id=table_id)
    return table

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT,summary="테이블 추가")
def table_create(_table_create: tables_schema.TableCreate,
                db: Session = Depends(get_db)):
    tables_crud.create_table(db=db, table_create=_table_create)
    return Response(status_code=status.HTTP_201_CREATED)

@router.put("/update", status_code=status.HTTP_204_NO_CONTENT,summary="테이블 수정")
def table_update(table_id:int,_table_update:tables_schema.TableUpdate,
                db: Session = Depends(get_db)):
    tables_crud.update_table(db=db, table_id=table_id, table_update=_table_update)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT,summary="테이블 삭제")
def table_delete(table_id: int, db: Session = Depends(get_db)):
    tables_crud.delete_table(db=db, table_id=table_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get("/pay/{table_id}",summary="결제")
def table_pay(table_id: int, db: Session = Depends(get_db)):
    tables_crud.pay_table(db=db, table_id=table_id)
    return "결제 완료"