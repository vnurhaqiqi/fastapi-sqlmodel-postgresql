"""add relation genre to film

Revision ID: 7a3822d18836
Revises: 8dbf1cdc38f7
Create Date: 2021-10-29 13:13:22.050185

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7a3822d18836'
down_revision = '8dbf1cdc38f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('film', sa.Column('genre_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_film_genre_id'), 'film', ['genre_id'], unique=False)
    op.create_foreign_key(None, 'film', 'genre', ['genre_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'film', type_='foreignkey')
    op.drop_index(op.f('ix_film_genre_id'), table_name='film')
    op.drop_column('film', 'genre_id')
    # ### end Alembic commands ###