"""empty message

Revision ID: 3ccc529aa1cb
Revises: bf03df5ba949
Create Date: 2021-07-27 17:52:37.589232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ccc529aa1cb'
down_revision = 'bf03df5ba949'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('report',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('application_id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['application_id'], ['planning_application.id'], ),
    sa.PrimaryKeyConstraint('id', 'application_id')
    )
    op.create_table('report_detail',
    sa.Column('report_id', sa.Integer(), nullable=False),
    sa.Column('tree_id', sa.String(length=100), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('targeted_pollutant', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['report_id'], ['report.id'], ),
    sa.ForeignKeyConstraint(['targeted_pollutant'], ['pollutant.id'], ),
    sa.ForeignKeyConstraint(['tree_id'], ['tree.id'], ),
    sa.PrimaryKeyConstraint('report_id', 'tree_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('report_detail')
    op.drop_table('report')
    # ### end Alembic commands ###
