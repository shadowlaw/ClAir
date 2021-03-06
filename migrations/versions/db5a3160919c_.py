"""empty message

Revision ID: db5a3160919c
Revises: 8a54cd45347c
Create Date: 2021-07-29 15:57:42.267486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db5a3160919c'
down_revision = '8a54cd45347c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('town', schema=None) as batch_op:
        batch_op.add_column(sa.Column('size', sa.Numeric()))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('town', schema=None) as batch_op:
        batch_op.drop_column('size')
    # ### end Alembic commands ###
