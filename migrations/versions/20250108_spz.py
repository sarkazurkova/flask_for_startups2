"""spz

Revision ID: 20250108_spz
Revises: 20241210_v2
Create Date: 2025-01-08 11:29:02.539775+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20250108_spz'
down_revision = '20241210_v2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spz',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('spz', sa.String(length=50), nullable=False),
    sa.Column('typ_vozidla', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('spz')
    # ### end Alembic commands ###
