"""empty message

Revision ID: 737cc817b6ee
Revises: f0887a6d35f2
Create Date: 2021-07-30 23:06:09.738797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '737cc817b6ee'
down_revision = 'f0887a6d35f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('role')

    # ### end Alembic commands ###
