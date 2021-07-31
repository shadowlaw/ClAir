"""add folio number column to planning application

Revision ID: 03e1ad96712c
Revises: 1b4cbb1961dd
Create Date: 2021-07-30 13:16:29.031996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03e1ad96712c'
down_revision = '1b4cbb1961dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planning_application', schema=None) as batch_op:
        batch_op.add_column(sa.Column('folio_number', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planning_application', schema=None) as batch_op:
        batch_op.drop_column('folio_number')

    # ### end Alembic commands ###
