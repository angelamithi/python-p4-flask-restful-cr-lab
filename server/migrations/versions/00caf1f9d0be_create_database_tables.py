"""create database tables

Revision ID: 00caf1f9d0be
Revises: 67f5d67aea55
Create Date: 2023-12-27 11:05:15.639436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00caf1f9d0be'
down_revision = '67f5d67aea55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plants')
    # ### end Alembic commands ###
