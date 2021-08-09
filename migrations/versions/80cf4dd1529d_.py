"""empty message

Revision ID: 80cf4dd1529d
Revises: f0887a6d35f2
Create Date: 2021-08-08 21:59:20.792608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80cf4dd1529d'
down_revision = '737cc817b6ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('targeted_pollutant',
    sa.Column('report_id', sa.Integer(), nullable=False),
    sa.Column('tree_id', sa.String(length=255), nullable=False),
    sa.Column('targeted_pollutant_id', sa.String(length=255), nullable=False),
    sa.Column('target_type', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('report_id', 'tree_id', 'targeted_pollutant_id', name=op.f('pk_targeted_pollutant'))
    )
    with op.batch_alter_table('report', schema=None) as batch_op:
        batch_op.alter_column('application_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('report', schema=None) as batch_op:
        batch_op.alter_column('application_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    op.drop_table('targeted_pollutant')
    # ### end Alembic commands ###
