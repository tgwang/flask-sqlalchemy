"""empty message

Revision ID: c3b2317cd3b
Revises: 4302455b22d
Create Date: 2014-10-13 19:43:06.614385

"""

# revision identifiers, used by Alembic.
revision = 'c3b2317cd3b'
down_revision = '4302455b22d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'user_info', ['user_id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_info')
    ### end Alembic commands ###