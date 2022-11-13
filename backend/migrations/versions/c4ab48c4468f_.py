"""empty message

Revision ID: c4ab48c4468f
Revises: 
Create Date: 2022-11-13 15:32:39.111106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4ab48c4468f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Posts', sa.Column('postTitle', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Posts', 'postTitle')
    # ### end Alembic commands ###
