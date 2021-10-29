"""create genre table

Revision ID: 8dbf1cdc38f7
Revises: 27a6b90d4f0f
Create Date: 2021-10-29 10:32:22.037285

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '8dbf1cdc38f7'
down_revision = '27a6b90d4f0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genre',
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('id', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_genre_id'), 'genre', ['id'], unique=False)
    op.create_index(op.f('ix_genre_name'), 'genre', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_genre_name'), table_name='genre')
    op.drop_index(op.f('ix_genre_id'), table_name='genre')
    op.drop_table('genre')
    # ### end Alembic commands ###
