"""empty message

Revision ID: 94d78c9fce15
Revises: 
Create Date: 2022-06-12 01:30:00.188557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94d78c9fce15'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.add_column('persons', sa.Column('completed', sa.Boolean(), nullable=False))
    op.add_column('persons', sa.Column('completed', sa.Boolean(), nullable=True))
    op.execute('UPDATE persons SET completed = False WHERE completed IS NULL;')
    op.alter_column('persons', 'completed', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('persons', 'completed')
    # ### end Alembic commands ###