"""empty message

Revision ID: 86c391ade161
Revises: aa4af546c151
Create Date: 2023-06-04 23:02:28.240383

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '86c391ade161'
down_revision = 'aa4af546c151'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tables', 'is_paid')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tables', sa.Column('is_paid', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    # ### end Alembic commands ###