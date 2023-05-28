__Back End__ 

__Alembic__

alembic과 sqlalchemy를 통한 ORM 맛보기
```
alembic init <folder name>
ex) alembic init migrations
```
migrations폴더가 생성되면서 여러 환경변수 설정 파일들이 생긴다.

기존 폴더 안에 `alembic.ini` 파일이 생성되고 해당 `.ini` 파일을 열어보면, `sqlalchemy.url = ....`로 설정되어 있을텐데,
이 부분을 `main.py`에서 설정해둔 경로로 변경하고 `migrations`폴더 내부의 `env.py`파일에서 `import models`를 통해 DataBase의 작업을 편하게 할 수 있다.

sqllite기준으로, 
```
sqlite:///./<databasename.db>
```

자동으로 `models.py`에 설정해둔 테이블이 생성되기 위해서

```
alembic revision --autogenerate
alembic upgrade head
```
를 통해 데이터 베이스의 테이블에 대해 처리를 진행할 수 있다.
