"""Migration

Revision ID: 715ad4e0a1d2
Revises: b04d772ae0e3
Create Date: 2022-05-15 18:03:15.556872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '715ad4e0a1d2'
down_revision = 'b04d772ae0e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('dateposted', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'dateposted')
    # ### end Alembic commands ###
