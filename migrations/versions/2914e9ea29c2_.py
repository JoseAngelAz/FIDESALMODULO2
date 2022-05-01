"""empty message

Revision ID: 2914e9ea29c2
Revises: 7594da09cdda
Create Date: 2022-04-14 03:17:59.774098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2914e9ea29c2'
down_revision = '7594da09cdda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pais',
    sa.Column('idpais', sa.Integer(), nullable=False),
    sa.Column('pais', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('idpais')
    )
    op.add_column('usuario', sa.Column('pais_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'usuario', 'pais', ['pais_id'], ['idpais'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'usuario', type_='foreignkey')
    op.drop_column('usuario', 'pais_id')
    op.drop_table('pais')
    # ### end Alembic commands ###