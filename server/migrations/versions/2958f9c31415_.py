"""empty message

Revision ID: 2958f9c31415
Revises: 
Create Date: 2022-08-24 12:42:40.787898

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2958f9c31415'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('stats', 'date',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('stats', 'score',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('stats', 'fairways',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('stats', 'gir',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('stats', 'threep',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('stats', 'threep',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('stats', 'gir',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('stats', 'fairways',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('stats', 'score',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('stats', 'date',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###
