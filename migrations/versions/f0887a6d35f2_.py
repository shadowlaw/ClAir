"""add pollutant limit status table and field

Revision ID: f0887a6d35f2
Revises: 03e1ad96712c
Create Date: 2021-07-30 13:43:34.875952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0887a6d35f2'
down_revision = '03e1ad96712c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pollutant_limit_status',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_pollutant_limit_status'))
    )
    with op.batch_alter_table('planning_application_area_pollutant', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status_id', sa.String(length=100), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_planning_application_area_pollutant_status_id_pollutant_limit_status'), 'pollutant_limit_status', ['status_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planning_application_area_pollutant', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_planning_application_area_pollutant_status_id_pollutant_limit_status'), type_='foreignkey')
        batch_op.drop_column('status_id')

    op.drop_table('pollutant_limit_status')
    # ### end Alembic commands ###