"""Migration

Revision ID: b04d772ae0e3
Revises: b8e6b7e47cb8
Create Date: 2022-05-15 18:03:04.541025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b04d772ae0e3'
down_revision = 'b8e6b7e47cb8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'dateposted')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('dateposted', sa.DATE(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
